#!/usr/bin/env python3
"""Rendu image par image (Pillow + numpy) -> un segment MP4 par ligne (en parallèle) -> concat ffmpeg.
Usage : render_video.py [--only L05] [--fast]   (--fast = 1/2 résolution temporelle pour les tests)"""
import math, random, re, subprocess, sys
from multiprocessing import Pool
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from common import *

BG, GREEN, AMBER, RED, DIM, WHITE, PANEL = (7, 9, 12), (57, 255, 136), (255, 176, 0), (255, 59, 78), (130, 148, 162), (230, 237, 243), (14, 19, 25)
FD = "/usr/share/fonts/truetype/dejavu/"
_f = {}
def font(size, mono=False, bold=False):
    k = (size, mono, bold)
    if k not in _f: _f[k] = ImageFont.truetype(FD + ("DejaVuSansMono" if mono else "DejaVuSans") + ("-Bold" if bold else "") + ".ttf", size)
    return _f[k]
def ease(x): x = max(0, min(1, x)); return x * x * (3 - 2 * x)
def seg(t, a, b): return ease((t - a) / (b - a)) if b > a else 1.0
def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    return lines + ([cur] if cur else [])
def tc(d, xy, text, f, fill, anchor="la"): d.text(xy, text, font=f, fill=fill, anchor=anchor)
def fade(c, a): return tuple(int(BG[i] + (c[i] - BG[i]) * max(0, min(1, a))) for i in range(3))

# ---------------------------------------------------------------- visuels
def v_terminal(d, t, T, kv, fl):
    lines = kv.get("lines", "").split("|")
    x0, y0, x1, y1 = 80, 110, 1200, min(590, 110 + 70 + 56 * len(lines))
    d.rounded_rectangle((x0, y0, x1, y1), 10, fill=PANEL, outline=(30, 40, 50), width=2)
    d.rectangle((x0, y0, x1, y0 + 34), fill=(20, 28, 36))
    for i, c in enumerate((RED, AMBER, GREEN)): d.ellipse((x0 + 14 + i * 22, y0 + 11, x0 + 26 + i * 22, y0 + 23), fill=c)
    tc(d, (x1 - 14, y0 + 8), "reconstitution · logs simulés", font(15, True), DIM, "ra")
    typed = max(0, (t - TERM_START) * TERM_CPS); y = y0 + 58; f = font(25, True); used = 0
    for ln in lines:
        n = int(max(0, min(len(ln), typed - used))); used += len(ln) + 6
        if n <= 0: break
        col = WHITE
        if re.search(r"OK|\[x\]", ln): col = GREEN
        if re.search(r"mint|ACCEPTED|CONFIRMED|END OF LOG", ln, re.I): col = RED if "mint" in ln.lower() or "ACCEPT" in ln or "CONFIRM" in ln else AMBER
        if re.match(r"^\d\d \w+", ln): col = AMBER
        for k, sub in enumerate(wrap(d, ln[:n], f, x1 - x0 - 70)):
            tc(d, (x0 + 28, y), ("› " if k == 0 else "  ") + sub, f, col); y += 40
        y += 6
    if int(t * 2) % 2 == 0 and typed < used + 3: d.rectangle((x0 + 30, y, x0 + 46, y + 26), fill=GREEN)

def v_bignum(d, t, T, kv, fl):
    big, small = kv.get("big", ""), kv.get("small", "")
    m = re.match(r"^([\d ]+)(.*)$", big)
    if m and len(m.group(1).strip()) > 3:
        val = int(m.group(1).replace(" ", "")); cur = int(val * seg(t, 0.4, 2.2)); s = f"{cur:,}".replace(",", " ") + " " + m.group(2).strip()
    else: s = big
    sz = 120
    while font(sz, True, True).getlength(s) > W - 160 and sz > 40: sz -= 4
    a = seg(t, 0.1, 0.5); col = RED if "BNB" in big else AMBER
    tc(d, (W / 2, 290), s, font(sz, True, True), fade(col, a), "mm")
    for k, ln in enumerate(wrap(d, small, font(30), W - 260)): tc(d, (W / 2, 400 + k * 42), ln, font(30), fade(WHITE, seg(t, 0.9, 1.5)), "ma")

def v_quote(d, t, T, kv, fl):
    lines = kv.get("text", "").split("|"); y = 190; d.rectangle((110, 170, 116, 170 + 70 * len(lines) + 20), fill=RED if "glitch" in fl else AMBER)
    step = max(1.0, min(2.2, (T - 2.5) / max(1, len(lines))))
    for i, ln in enumerate(lines):
        a = seg(t, 0.4 + i * step, 0.9 + i * step); last = i == len(lines) - 1 and len(lines) > 1
        col = (RED if "glitch" in fl else AMBER) if last else WHITE
        sz = 42 if len(ln) < 44 else 34
        for sub in wrap(d, ln, font(sz, bold=last), W - 300): tc(d, (150, y), sub, font(sz, bold=last), fade(col, a)); y += sz + 22
        y += 10

BOXES = {"b": (70, 250, 380, 430, "BEACON CHAIN", "BEP2 · code Cosmos"), "h": (470, 270, 810, 410, "TOKEN HUB", "pont · IAVL"), "s": (900, 250, 1210, 430, "SMART CHAIN", "BSC · compatible EVM")}
def box(d, k, col, a=1.0, label2=None):
    x0, y0, x1, y1, n, sub = BOXES[k]
    d.rounded_rectangle((x0, y0, x1, y1), 14, fill=fade(PANEL, 1), outline=fade(col, a), width=3)
    tc(d, ((x0 + x1) / 2, y0 + 50), n, font(26, True, True), fade(col, a), "mm"); tc(d, ((x0 + x1) / 2, y0 + 92), label2 or sub, font(18, True), fade(DIM, 1), "mm")
def arrow(d, a, b, col, w=4):
    d.line((a, b), fill=col, width=w); ang = math.atan2(b[1] - a[1], b[0] - a[0])
    for s in (-0.45, 0.45): d.line((b, (b[0] - 18 * math.cos(ang + s), b[1] - 18 * math.sin(ang + s))), fill=col, width=w)
def chip(d, xy, text, col, fill=PANEL, sz=22):
    f = font(sz, True, True); w = f.getlength(text) + 30
    d.rounded_rectangle((xy[0] - w / 2, xy[1] - 22, xy[0] + w / 2, xy[1] + 22), 10, fill=fill, outline=col, width=2); tc(d, xy, text, f, col, "mm")

def v_diagram(d, t, T, kv, fl):
    st = int(kv.get("stage", 0)); P = lambda k: ((BOXES[k][0] + BOXES[k][2]) / 2, (BOXES[k][1] + BOXES[k][3]) / 2)
    pulse = 0.6 + 0.4 * math.sin(t * 4)
    if st == 0:
        for k in "bhs": box(d, k, GREEN if k != "h" else AMBER, seg(t, 0.2 + "bhs".index(k) * 0.5, 0.8 + "bhs".index(k) * 0.5))
        arrow(d, (385, 340), (465, 340), DIM); arrow(d, (815, 340), (895, 340), DIM)
    elif st == 1:
        box(d, "b", GREEN); box(d, "h", AMBER); box(d, "s", GREEN)
        chip(d, (225, 190), "VERROUILLER  🔒".replace("  🔒", ""), AMBER, sz=24); chip(d, (1055, 190), "CRÉER (mint)", GREEN, sz=24)
        arrow(d, (385, 340), (465, 340), AMBER); arrow(d, (815, 340), (895, 340), GREEN)
        a = seg(t, 1.5, 2.3); tc(d, (W / 2, 560), "jetons verrouillés  =  jetons créés   →   total constant", font(28, True), fade(WHITE, a), "mm")
    elif st == 2:
        box(d, "b", GREEN); box(d, "h", AMBER, label2="vérifie la preuve"); box(d, "s", DIM, label2="ne voit pas la Beacon Chain")
        d.line((225, 470, 1055, 470), fill=(30, 40, 50), width=3)
        x = 225 + (1055 - 225) * seg(t, 0.8, 5.5); d.rounded_rectangle((x - 45, 452, x + 45, 488), 6, fill=(30, 40, 50), outline=WHITE, width=2); tc(d, (x, 470), "preuve", font(17, True), WHITE, "mm")
        chip(d, (640, 560), "module IAVL (preuve de Merkle)", AMBER, sz=24); arrow(d, (640, 536), (640, 418), AMBER)
    elif st == 3:
        box(d, "b", GREEN); box(d, "h", AMBER); box(d, "s", GREEN)
        steps = ["1 · verrouiller", "2 · relayer", "3 · vérifier", "4 · créer"]
        for i, s in enumerate(steps):
            on = t > 0.6 + i * 1.8; chip(d, (180 + i * 308, 560), s, GREEN if on else DIM, sz=22)
    elif st == 4:
        box(d, "s", RED, label2="2 000 000 BNB créés"); chip(d, (225, 340), "adresse attaquante", RED, sz=22); arrow(d, (370, 340), (895, 340), RED)
        for i, (n, pos, src, dst) in enumerate((("autre chaîne A", (1110, 130), (1055, 252), (1100, 158)), ("autre chaîne B", (1110, 530), (1055, 428), (1100, 506)), ("échanges", (640, 530), (940, 428), (700, 506)))):
            a = seg(t, 1.0 + i * 0.9, 1.8 + i * 0.9)
            if a > 0.05: chip(d, pos, n, fade(AMBER, a), sz=22); arrow(d, src, dst, fade(AMBER, a), 3)
    elif st == 5:
        box(d, "h", AMBER, label2="verify_proof(IAVL)")
        for i, (lab, col, msg) in enumerate((("preuve valide", GREEN, "→ OK"), ("preuve forgée", RED, "→ OK"))):
            cx = 330 + i * 620; d.rounded_rectangle((cx - 230, 440, cx + 230, 590), 10, fill=PANEL, outline=col, width=3)
            tc(d, (cx, 465), lab.upper(), font(22, True, True), col, "mm"); tc(d, (cx, 510), "a3f9…c07e  4b1d…92aa", font(20, True), DIM, "mm"); tc(d, (cx, 558), msg, font(30, True, True), GREEN, "mm")
            arrow(d, (cx, 438), (640 + (cx - 640) * 0.3, 415), col, 3)
        a = seg(t, 3.0, 4.0); tc(d, (W / 2, 190), "même verdict, deux réalités", font(34, True), fade(RED, a), "mm")
    elif st == 6:
        cx, cy = 640, 360; r = 190
        for i in range(9):
            ang = i / 9 * 2 * math.pi - 1.57; x, y = cx + r * 1.5 * math.cos(ang), cy + r * 0.95 * math.sin(ang)
            on = t > 0.6 + i * 0.35; d.ellipse((x - 22, y - 22, x + 22, y + 22), outline=RED if on else GREEN, width=4, fill=PANEL)
            d.line((cx, cy, x, y), fill=fade(RED if on else GREEN, 0.35), width=2)
        chip(d, (cx, cy), "BNB SMART CHAIN", WHITE, sz=26)
        tc(d, (cx, 640), "validateurs : « suspendez la chaîne »  →  HALT", font(26, True), fade(RED, seg(t, 3.5, 4.5)), "mm")

def v_chart(d, t, T, kv, fl):
    mode, label = kv.get("mode", "flat"), kv.get("label", ""); x0, y0, x1, y1 = 120, 150, 1160, 520
    d.rectangle((x0, y0, x1, y1), outline=(30, 40, 50), width=2)
    for i in range(1, 5): d.line((x0, y0 + i * (y1 - y0) / 5, x1, y0 + i * (y1 - y0) / 5), fill=(20, 28, 36))
    tc(d, (x0, y0 - 30), label, font(22, True), DIM)
    if mode in ("flat", "spike"):
        rnd = random.Random(7); n = 120; shown = int(n * seg(t, 0.3, min(T - 1.5, 5.5))); pts = []
        for i in range(shown):
            x = x0 + (x1 - x0) * i / (n - 1); v = 0.12 + 0.03 * math.sin(i * 0.9) + rnd.uniform(-0.01, 0.01)
            if mode == "spike":
                if i > 60: v += 0.35
                if i > 85: v += 0.35
            pts.append((x, y1 - v * (y1 - y0) / 0.9 * 1.0 - 10))
        if len(pts) > 1: d.line(pts, fill=GREEN if mode == "flat" else RED, width=4)
        if mode == "spike":
            if shown > 62: tc(d, (x0 + (x1 - x0) * 60 / 119 - 10, y0 + 140), "+1 000 000 BNB", font(22, True), RED, "ra")
            if shown > 87: tc(d, (x0 + (x1 - x0) * 85 / 119 - 10, y0 + 40), "+1 000 000 BNB", font(22, True), RED, "ra")
        if mode == "flat" and shown > 100: chip(d, (W / 2, 590), "aucune alerte · aucune anomalie", GREEN, sz=24)
    else:  # range : 570 M$ total, 100-130 sortis
        total = 570; bw = x1 - x0; a = seg(t, 0.4, 2.0)
        d.rectangle((x0, 250, x0 + bw * a, 340), fill=(30, 40, 50)); tc(d, (x0 + 10, 360), "0", font(20, True), DIM)
        s0, s1 = 100 / total, 130 / total
        d.rectangle((x0, 250, x0 + bw * s0 * a, 340), fill=RED)
        for i in range(0, int(bw * (s1 - s0) * a), 10): d.line((x0 + bw * s0 + i, 340, x0 + bw * s0 + i + 8, 250), fill=RED, width=3)
        if t > 2.2:
            tc(d, (x0, 225), "▲ rouge : sorti de la chaîne (estimation)", font(22, True), RED, "lm")
            tc(d, (x0, 400), "gris : reste bloqué ou gelé sur la Smart Chain (≈ 440 M$, selon les sources)", font(22, True), WHITE, "lm")
            tc(d, (x1, 360), "≈ 570 M$", font(22, True), AMBER, "ra")
            tc(d, (W / 2, 480), "les chiffres divergent selon les sources", font(30, True), AMBER, "mm")

EVENTS = [("05 OCT", "100 BNB → adresse neuve", AMBER), ("06 OCT · 20:43 UTC", "créations de BNB", RED), ("06 OCT · 23:51 UTC", "suspension annoncée", AMBER), ("07 OCT · ≈ 06:40 UTC", "reprise de la chaîne", GREEN)]
def v_timeline(d, t, T, kv, fl):
    up = int(kv.get("upto", 0)); y = 340; xs = [220 + i * 280 for i in range(4)]
    d.line((100, y, 1180, y), fill=(30, 40, 50), width=4)
    for i, ((dt, lab, col), x) in enumerate(zip(EVENTS, xs)):
        if i > up: d.ellipse((x - 10, y - 10, x + 10, y + 10), outline=DIM, width=2); continue
        a = 1.0 if i < up else seg(t, 0.2, 0.9)
        if i > 0: d.line((xs[i - 1], y, xs[i - 1] + (x - xs[i - 1]) * (1 if i < up else a), y), fill=fade(col, 1), width=5)
        r = 12 + (6 * math.sin(t * 5) if i == up else 0); d.ellipse((x - r, y - r, x + r, y + r), fill=fade(col, a))
        yy = y - 110 if i % 2 == 0 else y + 60
        tc(d, (x, yy), dt, font(22, True, True), fade(AMBER, a), "mm"); tc(d, (x, yy + 36), lab, font(22), fade(WHITE, a), "mm")

VIS = dict(terminal=v_terminal, bignum=v_bignum, quote=v_quote, diagram=v_diagram, chart=v_chart, timeline=v_timeline)

# ---------------------------------------------------------------- post-traitement
_scan = None
def overlay():
    global _scan
    if _scan is None:
        s = np.ones((H, W, 1), np.float32); s[::3] = 0.9
        yy, xx = np.mgrid[0:H, 0:W]; v = 1 - 0.4 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) ** 1.4
        _scan = s * np.clip(v, 0.25, 1)[..., None].astype(np.float32)
    return _scan
def post(img, t, fl, rnd, frame_i):
    a = np.asarray(img, np.float32) * overlay()
    if "scan" in fl: a[1::2] *= 0.82
    a += rnd.normal(0, 3.0, (H, W, 1)).astype(np.float32)
    g = ("glitch" in fl and (t < 0.7 or (frame_i % 29) in (0, 1, 2))) or (frame_i % 211) == 0
    if g:
        for _ in range(rnd.integers(3, 8)):
            y0 = int(rnd.integers(0, H - 40)); h = int(rnd.integers(6, 40)); a[y0:y0 + h] = np.roll(a[y0:y0 + h], int(rnd.integers(-60, 60)), axis=1)
        a[..., 0] = np.roll(a[..., 0], 6, axis=1); a[..., 2] = np.roll(a[..., 2], -6, axis=1)
    return np.clip(a, 0, 255).astype(np.uint8)

def chrome(d, l, t, g_t):
    tc(d, (40, 26), "INCIDENT LOG", font(20, True, True), RED); tc(d, (200, 26), "·  BINANCE / BSC TOKEN HUB  ·  6 OCT. 2022", font(20, True), DIM)
    tc(d, (W - 40, 26), l["section"].upper(), font(18, True), DIM, "ra"); d.line((40, 60, W - 40, 60), fill=(30, 40, 50))
    m, s = divmod(int(g_t), 60); tc(d, (40, H - 26), f"{l['id']}  ·  {m:02d}:{s:02d}", font(17, True), DIM, "lm")
    tc(d, (W - 40, H - 26), "reconstitution pédagogique · logs simulés", font(17, True), DIM, "rm")

def frame(l, t, T, i, rnd):
    kind, fl, kv = parse_rendu(l["rendu"]); img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    VIS[kind](d, t, T, kv, fl); chrome(d, l, t, l["start"] + t)
    # sous-titres
    f = font(26); sub = l["texte"].replace("I A V L", "IAVL").replace("U T C", "UTC"); lines = wrap(d, sub, f, W - 200)
    words = sub.split(); vis = int(len(words) * ((t - LEAD) / max(0.1, l["voice_dur"]))) if t > LEAD else 0
    if vis > 0:
        cur = " ".join(words[:vis]); shown = wrap(d, cur, f, W - 200)
        total = len(lines); idx = max(0, len(shown) - 2); block = shown[idx:]
        for k, ln in enumerate(block): tc(d, (W / 2, 606 + k * 34), ln, f, WHITE, "ma")
    fade_in = seg(t, 0, 0.25) if l["id"] == "L01" else 1.0; out = post(img, t, fl, rnd, i)
    if fade_in < 1: out = (out * fade_in).astype(np.uint8)
    return out

def render_line(args):
    l, fast = args; T = l["dur"]; n = int(round(T * FPS)); rnd = np.random.default_rng(int(l["id"][1:])); out = BUILD / "seg" / f"{l['id']}.mp4"
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-preset", "veryfast" if not fast else "ultrafast", "-crf", "20", "-pix_fmt", "yuv420p", str(out)], stdin=subprocess.PIPE)
    for i in range(n): p.stdin.write(frame(l, i / FPS, T, i, rnd).tobytes())
    p.stdin.close(); p.wait(); return l["id"]

if __name__ == "__main__":
    tl = timeline()["lines"]; only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    (BUILD / "seg").mkdir(parents=True, exist_ok=True); todo = [(l, "--fast" in sys.argv) for l in tl if not only or l["id"] == only]
    with Pool() as pool:
        for k in pool.imap_unordered(render_line, todo): print("rendu", k, flush=True)
    if not only:
        lst = BUILD / "seg" / "list.txt"; lst.write_text("".join(f"file '{l['id']}.mp4'\n" for l in tl))
        # 1 s de noir au début est déjà couvert : le 1er segment démarre à t=1.0 -> on préfixe un noir
        subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"color=c=0x07090c:s={W}x{H}:r={FPS}:d=1", "-c:v", "libx264", "-pix_fmt", "yuv420p", str(BUILD / "seg" / "_intro.mp4")])
        lst.write_text("file '_intro.mp4'\n" + lst.read_text())
        subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(BUILD / "video_silent.mp4")])
        print("OK build/video_silent.mp4")
