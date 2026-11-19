#!/usr/bin/env python3
"""Build the 19 November 2026 world-news poster (entry.png, 1024x1024).

Drawn programmatically with PIL so every word is crisp, real text.
Run:  python3 build_poster.py   ->  writes entry.png next to this script.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
MARGIN = 36

NAVY = (16, 42, 67)
GOLD = (201, 162, 39)
IVORY = (246, 241, 231)
WHITE = (255, 255, 255)
INK = (24, 28, 36)
GREY = (92, 96, 104)
CARD = (255, 255, 255)
BORDER = (214, 206, 190)

PINK = (226, 20, 110)      # GTA VI
TEAL = (0, 128, 128)       # ICJ
DBLUE = (30, 64, 175)      # Jeffries / US politics
ORANGE = (217, 119, 6)     # Cyclone
DRED = (185, 28, 28)       # US-Iran
PURPLE = (109, 40, 217)    # Voyager

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
RED = (198, 40, 40)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Wrap text to lines that fit max_w pixels."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def icon_controller(d, x, y, s, col):
    # rounded gamepad body + buttons, white on colour
    d.rounded_rectangle([x, y + s * 0.30, x + s, y + s * 0.85], radius=s * 0.18,
                        fill=WHITE)
    d.ellipse([x + s * 0.18, y + s * 0.48, x + s * 0.32, y + s * 0.62], fill=col)
    d.ellipse([x + s * 0.68, y + s * 0.48, x + s * 0.82, y + s * 0.62], fill=col)
    d.rectangle([x + s * 0.44, y + s * 0.44, x + s * 0.56, y + s * 0.66], fill=col)


def icon_scales(d, x, y, s, col):
    # scales of justice: post, beam, two pans
    cx = x + s / 2
    d.rectangle([cx - 3, y + s * 0.10, cx + 3, y + s * 0.80], fill=WHITE)
    d.rectangle([x + s * 0.08, y + s * 0.22, x + s * 0.92, y + s * 0.28], fill=WHITE)
    for px in (x + s * 0.08, x + s * 0.92):
        d.polygon([(px - s * 0.16, y + s * 0.55), (px + s * 0.16, y + s * 0.55),
                   (px, y + s * 0.28)], outline=WHITE, width=4)
    d.ellipse([cx - s * 0.09, y + s * 0.02, cx + s * 0.09, y + s * 0.14], fill=WHITE)
    d.rectangle([x + s * 0.30, y + s * 0.80, x + s * 0.70, y + s * 0.88], fill=WHITE)


def icon_capitol(d, x, y, s, col):
    d.pieslice([x + s * 0.30, y + s * 0.08, x + s * 0.70, y + s * 0.48],
               180, 360, fill=WHITE)
    d.rectangle([x + s * 0.28, y + s * 0.46, x + s * 0.72, y + s * 0.52], fill=WHITE)
    for i in range(4):
        cx = x + s * (0.32 + i * 0.13)
        d.rectangle([cx - 3, y + s * 0.54, cx + 3, y + s * 0.78], fill=WHITE)
    d.rectangle([x + s * 0.22, y + s * 0.78, x + s * 0.78, y + s * 0.86], fill=WHITE)


def icon_cyclone(d, x, y, s, col):
    # spiral of arcs
    for i, r in enumerate([0.42, 0.33, 0.24, 0.15]):
        rr = s * r
        d.arc([x + s / 2 - rr, y + s / 2 - rr, x + s / 2 + rr, y + s / 2 + rr],
              start=40 + i * 55, end=300 + i * 55, fill=WHITE, width=6)


def icon_rocket(d, x, y, s, col):
    cx = x + s / 2
    d.polygon([(cx, y + s * 0.06), (cx - s * 0.16, y + s * 0.42),
               (cx + s * 0.16, y + s * 0.42)], fill=WHITE)
    d.rectangle([cx - s * 0.16, y + s * 0.42, cx + s * 0.16, y + s * 0.68], fill=WHITE)
    d.polygon([(cx - s * 0.16, y + s * 0.68), (cx - s * 0.26, y + s * 0.86),
               (cx - s * 0.06, y + s * 0.68)], fill=WHITE)
    d.polygon([(cx + s * 0.16, y + s * 0.68), (cx + s * 0.26, y + s * 0.86),
               (cx + s * 0.06, y + s * 0.68)], fill=WHITE)
    d.polygon([(cx, y + s * 0.94), (cx - s * 0.08, y + s * 0.70),
               (cx + s * 0.08, y + s * 0.70)], fill=(255, 214, 64))


def icon_planet(d, x, y, s, col):
    cx, cy = x + s / 2, y + s / 2
    d.ellipse([cx - s * 0.26, cy - s * 0.26, cx + s * 0.26, cy + s * 0.26],
              fill=WHITE)
    d.arc([x + s * 0.04, cy - s * 0.10, x + s * 0.96, cy + s * 0.16],
          start=195, end=345, fill=WHITE, width=5)
    d.ellipse([x + s * 0.78, y + s * 0.10, x + s * 0.86, y + s * 0.18], fill=WHITE)


img = Image.new("RGB", (W, H), IVORY)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 148], fill=NAVY)
d.rectangle([0, 148, W, 153], fill=RED)
f_kicker = font(FB, 30)
f_date = font(SERIF, 68)
d.text((MARGIN, 16), "WORLD NEWS", font=f_kicker, fill=RED)
d.text((MARGIN, 54), "19 NOVEMBER 2026", font=f_date, fill=WHITE)
d.text((W - MARGIN - d.textlength("THURSDAY", font=f_kicker), 16),
       "THURSDAY", font=f_kicker, fill=GOLD)

# ---------- lead story: GTA VI ----------
lead_y, lead_h = 170, 208
d.rounded_rectangle([MARGIN, lead_y, W - MARGIN, lead_y + lead_h], radius=10,
                    fill=CARD, outline=BORDER, width=2)
# pink art block on the left
d.rounded_rectangle([MARGIN, lead_y, MARGIN + 210, lead_y + lead_h], radius=10,
                    fill=PINK)
d.rounded_rectangle([MARGIN + 150, lead_y, MARGIN + 210, lead_y + lead_h],
                    radius=0, fill=PINK)  # square off the right edge of the block
icon_controller(d, MARGIN + 55, lead_y + 28, 100, PINK)
gta_label = "GTA VI"
d.text((MARGIN + (210 - d.textlength(gta_label, font=font(FB, 38))) / 2,
        lead_y + 140), gta_label, font=font(FB, 38), fill=WHITE)
lx = MARGIN + 236
f_tag = font(FB, 22)
d.text((lx, lead_y + 16), "CULTURE  •  GAMING", font=f_tag, fill=PINK)
d.text((lx, lead_y + 46), "GTA VI IS HERE", font=font(SERIF, 58), fill=INK)
deck = ("After a 13-year wait, Rockstar's blockbuster launches at "
        "midnight in every time zone — critics score it 99/100.")
f_deck = font(FR, 24)
y = draw_lines(d, wrap(d, deck, f_deck, W - MARGIN - lx - 24),
               lx, lead_y + 118, f_deck, (58, 62, 70), 32)

# ---------- story grid (2 x 2) ----------
stories = [
    ("WORLD  •  LAW", TEAL, icon_scales,
     "World court rules on Rohingya genocide",
     "ICJ delivers its verdict in Gambia v. Myanmar — the first "
     "time it could hold a state guilty of genocide."),
    ("USA  •  POLITICS", DBLUE, icon_capitol,
     "Jeffries set to be first Black Speaker",
     "House Democrats nominate Hakeem Jeffries; he takes the gavel "
     "on 3 January."),
    ("ASIA  •  WEATHER", ORANGE, icon_cyclone,
     "Cyclone Akvan bears down on India",
     "The severe storm nears the Andhra Pradesh and Odisha coasts; "
     "states are on red alert."),
    ("MIDDLE EAST  •  CONFLICT", DRED, icon_rocket,
     "US–Iran strikes widen across the Gulf",
     "Iran hits a US base in Kuwait and Bahrain again; the US struck "
     "a missile site on Qeshm Island."),
]
col_w = (W - 2 * MARGIN - 20) // 2
row_h, row_gap = 176, 14
grid_y0 = 390
for i, (tag, col, icon, head, body) in enumerate(stories):
    cx = MARGIN + (i % 2) * (col_w + 20)
    cy = grid_y0 + (i // 2) * (row_h + row_gap)
    d.rounded_rectangle([cx, cy, cx + col_w, cy + row_h], radius=10,
                        fill=CARD, outline=BORDER, width=2)
    # colour chip with icon
    d.rounded_rectangle([cx, cy, cx + 96, cy + row_h], radius=10, fill=col)
    d.rounded_rectangle([cx + 60, cy, cx + 96, cy + row_h], radius=0, fill=col)
    icon(d, cx + 18, cy + 14, 60, col)
    tx = cx + 112
    d.text((tx, cy + 12), tag, font=font(FB, 19), fill=col)
    f_head = font(FB, 26)
    lines = wrap(d, head, f_head, col_w - 128)
    y = draw_lines(d, lines, tx, cy + 38, f_head, INK, 30)
    f_body = font(FR, 19)
    draw_lines(d, wrap(d, body, f_body, col_w - 128), tx, y + 6, f_body,
               (58, 62, 70), 23)

# ---------- Voyager band (full width) ----------
voy_y, voy_h = 770, 108
d.rounded_rectangle([MARGIN, voy_y, W - MARGIN, voy_y + voy_h], radius=10,
                    fill=NAVY)
icon_planet(d, MARGIN + 16, voy_y + 19, 70, NAVY)
d.text((MARGIN + 104, voy_y + 12), "SPACE  •  SCIENCE", font=font(FB, 19),
       fill=GOLD)
d.text((MARGIN + 104, voy_y + 36), "Voyager 1 reaches a light-day from Earth",
       font=font(FB, 29), fill=WHITE)
d.text((MARGIN + 104, voy_y + 72),
       "After nearly 50 years in space, NASA's probe crosses a record "
       "distance.",
       font=font(FR, 20), fill=(205, 214, 224))

# ---------- also today ----------
also_y = 890
d.text((MARGIN, also_y), "ALSO TODAY", font=font(FB, 22), fill=INK)
d.line([MARGIN + 158, also_y + 12, W - MARGIN, also_y + 12], fill=BORDER, width=2)
d.text((MARGIN, also_y + 28), "EU proposes a €45bn loan for Ukraine",
       font=font(FR, 21), fill=(58, 62, 70))
d.text((MARGIN, also_y + 54),
       "Pew: Islam set to be the world's largest faith by 2035",
       font=font(FR, 21), fill=(58, 62, 70))

# ---------- footer ----------
d.text((MARGIN, 980), "World news of 19 November 2026",
       font=font(FB, 20), fill=GREY)
d.text((W - MARGIN - d.textlength("Reports published 19 Nov 2026",
                                  font=font(FR, 20)), 980),
       "Reports published 19 Nov 2026",
       font=font(FR, 20), fill=GREY)

img.save(OUT, "PNG", optimize=True)
print("saved", OUT, img.size, os.path.getsize(OUT), "bytes")
