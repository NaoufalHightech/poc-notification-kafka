#!/usr/bin/env python3
"""Miniature YouTube 1280x720 -> assets/visuals/thumbnail.jpg"""
import numpy as np
from PIL import Image, ImageDraw
from render_video import font, tc, BG, RED, AMBER, WHITE, DIM, GREEN
from common import *
img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
for y in range(0, H, 3): d.line((0, y, W, y), fill=(10, 13, 17))
d.rectangle((0, 0, 18, H), fill=RED)
d.rounded_rectangle((70, 60, 420, 118), 8, fill=RED); tc(d, (245, 89), "INCIDENT LOG", font(36, True, True), (255, 255, 255), "mm")
tc(d, (440, 89), "6 OCT. 2022", font(36, True, True), AMBER, "lm")
tc(d, (70, 200), "2 000 000 BNB", font(104, True, True), RED)
tc(d, (70, 335), "créés de nulle part", font(60, True), WHITE)
tc(d, (70, 440), "verify_proof(IAVL) ... OK", font(40, True), GREEN)
tc(d, (70, 520), "Le pont a cru une fausse preuve.", font(46, True, True), AMBER)
tc(d, (70, 650), "BINANCE · BSC TOKEN HUB · reconstitution", font(28, True), DIM)
a = np.asarray(img, np.float32); yy, xx = np.mgrid[0:H, 0:W]; a *= (1 - 0.35 * (((xx - W / 2) / (W / 2)) ** 2))[..., None]
Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(ASSETS / "visuals" / "thumbnail.jpg", quality=90)
