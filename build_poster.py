#!/usr/bin/env python3
"""Build the 19 November 2026 world-news poster v2 (entry.png, 1024x1024).

Premium newspaper front page, drawn programmatically with PIL so every
word is crisp, real text. Two lead stories (GTA VI + ICJ verdict), a
2x3 story grid, a Voyager band and an ALSO TODAY strip.

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
EMERALD = (4, 120, 87)     # Summit
DRED = (185, 28, 28)       # US-Iran
PURPLE = (109, 40, 217)    # Crimea Bridge
DBLUE = (30, 64, 175)      # Jeffries / US politics
ORANGE = (217, 119, 6)     # Cyclone
SKY = (2, 132, 199)        # Anthropic IPO

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
RED = (198, 40, 40)

# ---------------------------------------------------------------- ICJ verdict
# Verdict read 19 Nov 2026 (~16:00-17:30 WIB): court found Myanmar committed
# genocide against the Rohingya — first state ever found guilty (Al Jazeera
# breaking; BBC/TBS live blog: ~10,000 violently killed, 815,000 targeted).
ICJ_HEAD = "MYANMAR GUILTY OF GENOCIDE"
ICJ_DECK = ("First state ever found guilty of genocide. "
            "~10,000 Rohingya killed in 2017.")


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


def icon_summit(d, x, y, s, col):
    # three leaders at a table: heads + shoulders + table line
    for i, fx in enumerate((0.20, 0.50, 0.80)):
        cx = x + s * fx
        cy = y + s * (0.30 if i != 1 else 0.22)
        r = s * (0.11 if i != 1 else 0.13)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE)
        d.pieslice([cx - s * 0.14, cy + s * 0.12, cx + s * 0.14,
                    cy + s * 0.44], 180, 360, fill=WHITE)
    d.rectangle([x + s * 0.06, y + s * 0.74, x + s * 0.94, y + s * 0.82],
                fill=WHITE)


def icon_bridge(d, x, y, s, col):
    # suspension bridge: deck, arch, pillars, suspenders
    d.rectangle([x + s * 0.04, y + s * 0.62, x + s * 0.96, y + s * 0.70],
                fill=WHITE)
    d.arc([x + s * 0.10, y + s * 0.18, x + s * 0.90, y + s * 0.86],
          start=180, end=360, fill=WHITE, width=5)
    for px in (x + s * 0.16, x + s * 0.84):
        d.rectangle([px - 3, y + s * 0.30, px + 3, y + s * 0.66], fill=WHITE)
    for fx in (0.32, 0.50, 0.68):
        d.line([x + s * fx, y + s * 0.30, x + s * fx, y + s * 0.62],
               fill=WHITE, width=3)


def icon_chart(d, x, y, s, col):
    # ascending bars + trend arrow
    bars = [(0.12, 0.42), (0.38, 0.62), (0.64, 0.82)]
    for fx, fh in bars:
        d.rectangle([x + s * fx, y + s * (0.92 - fh), x + s * (fx + 0.16),
                     y + s * 0.92], fill=WHITE)
    d.line([x + s * 0.08, y + s * 0.30, x + s * 0.92, y + s * 0.06],
           fill=WHITE, width=5)
    d.polygon([(x + s * 0.92, y + s * 0.06), (x + s * 0.74, y + s * 0.06),
               (x + s * 0.92, y + s * 0.24)], fill=WHITE)


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

# ---------- lead row: two heroes ----------
def hero(x, y, w, h, col, icon, label, tag, head, deck, head_size):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10,
                        fill=CARD, outline=BORDER, width=2)
    bw = 148  # art block width
    d.rounded_rectangle([x, y, x + bw, y + h], radius=10, fill=col)
    d.rounded_rectangle([x + bw - 40, y, x + bw, y + h], radius=0, fill=col)
    icon(d, x + 34, y + 22, 80, col)
    lab = label
    lf = font(FB, 30)
    d.text((x + (bw - d.textlength(lab, font=lf)) / 2, y + h - 52),
           lab, font=lf, fill=WHITE)
    tx = x + bw + 18
    tw = x + w - tx - 14
    d.text((tx, y + 14), tag, font=font(FB, 19), fill=col)
    f_head = font(SERIF, head_size)
    hy = draw_lines(d, wrap(d, head, f_head, tw), tx, y + 40, f_head, INK,
                    head_size + 6)
    f_deck = font(FR, 18)
    draw_lines(d, wrap(d, deck, f_deck, tw), tx, hy + 6, f_deck,
               (58, 62, 70), 23)

hero_y, hero_h = 168, 232
hero_w = (W - 2 * MARGIN - 20) // 2
hero(MARGIN, hero_y, hero_w, hero_h, PINK, icon_controller, "GTA VI",
     "CULTURE  •  GAMING", "GTA VI IS HERE",
     "After a 13-year wait, Rockstar's epic launches at midnight worldwide "
     "— 99/100 on Metacritic, tying Ocarina of Time. 17.1m copies pre-sold "
     "for $1.5bn.",
     30)
hero(MARGIN + hero_w + 20, hero_y, hero_w, hero_h, TEAL, icon_scales, "ICJ",
     "WORLD  •  LAW", ICJ_HEAD, ICJ_DECK, 28)

# ---------- story grid (2 x 3) ----------
stories = [
    ("DIPLOMACY  •  APEC", EMERALD, icon_summit,
     "Trump, Xi and Putin meet in Shenzhen",
     "First trilateral of the nuclear powers, on the APEC sidelines — arms, "
     "Ukraine and Iran."),
    ("MIDDLE EAST  •  CONFLICT", DRED, icon_rocket,
     "Trump: Iran eyeing chemical, bio weapons",
     "Trump says Tehran is 'looking at gases, looking at bio' — and vows to "
     "'wipe them out'."),
    ("EUROPE  •  WAR", PURPLE, icon_bridge,
     "Crimea Bridge hit a third time in a week",
     "Traffic halted again after the overnight strike; a 227-metre section "
     "fell into the sea."),
    ("USA  •  POLITICS", DBLUE, icon_capitol,
     "Jeffries set to be first Black Speaker",
     "House Democrats nominate Hakeem Jeffries, 251–11; the full House votes "
     "on 3 January."),
    ("ASIA  •  WEATHER", ORANGE, icon_cyclone,
     "47,000 flee as Cyclone Akvan nears India",
     "Odisha evacuates 47,000 before Friday landfall; the third severe "
     "cyclone in a month."),
    ("BUSINESS  •  TECH", SKY, icon_chart,
     "Anthropic's $81bn IPO — the biggest ever",
     "Claude's maker debuts on Nasdaq today as ANT at $83 a share; valued "
     "at $1.5 trillion."),
]
col_w = (W - 2 * MARGIN - 20) // 2
row_h, row_gap = 112, 10
grid_y0 = 410
for i, (tag, col, icon, head, body) in enumerate(stories):
    cx = MARGIN + (i % 2) * (col_w + 20)
    cy = grid_y0 + (i // 2) * (row_h + row_gap)
    d.rounded_rectangle([cx, cy, cx + col_w, cy + row_h], radius=10,
                        fill=CARD, outline=BORDER, width=2)
    # colour chip with icon
    d.rounded_rectangle([cx, cy, cx + 84, cy + row_h], radius=10, fill=col)
    d.rounded_rectangle([cx + 54, cy, cx + 84, cy + row_h], radius=0, fill=col)
    icon(d, cx + 20, cy + 12, 44, col)
    tx = cx + 100
    d.text((tx, cy + 8), tag, font=font(FB, 14), fill=col)
    f_head = font(FB, 20)
    y = draw_lines(d, wrap(d, head, f_head, col_w - 116), tx, cy + 27,
                   f_head, INK, 23)
    f_body = font(FR, 14)
    draw_lines(d, wrap(d, body, f_body, col_w - 116), tx, y + 3, f_body,
               (58, 62, 70), 16)

# ---------- Voyager band (full width) ----------
voy_y, voy_h = 776, 80
d.rounded_rectangle([MARGIN, voy_y, W - MARGIN, voy_y + voy_h], radius=10,
                    fill=NAVY)
icon_planet(d, MARGIN + 14, voy_y + 12, 56, NAVY)
d.text((MARGIN + 88, voy_y + 10), "SPACE  •  SCIENCE", font=font(FB, 16),
       fill=GOLD)
d.text((MARGIN + 88, voy_y + 30), "Voyager 1 is now a light-day from Earth",
       font=font(FB, 26), fill=WHITE)
d.text((MARGIN + 88, voy_y + 58),
       "Signals take a full day to reach NASA's 1977 probe, 16 billion "
       "miles out.",
       font=font(FR, 17), fill=(205, 214, 224))

# ---------- also today ----------
also_y = 868
d.text((MARGIN, also_y), "ALSO TODAY", font=font(FB, 20), fill=INK)
d.line([MARGIN + 158, also_y + 11, W - MARGIN, also_y + 11], fill=BORDER, width=2)
also_items = [
    "EU proposes a €45bn loan for Ukraine",
    "EU–Indonesia trade pact approved — duties cut on 90% of goods",
    "Pew: Islam set to be the world's largest faith by 2035",
]
y = also_y + 26
for item in also_items:
    d.text((MARGIN, y), item, font=font(FR, 19), fill=(58, 62, 70))
    y += 24

# ---------- footer ----------
d.text((MARGIN, 978), "World news of 19 November 2026",
       font=font(FB, 20), fill=GREY)
d.text((W - MARGIN - d.textlength("Reports published 19 Nov 2026",
                                  font=font(FR, 20)), 978),
       "Reports published 19 Nov 2026",
       font=font(FR, 20), fill=GREY)

img.save(OUT, "PNG", optimize=True)
print("saved", OUT, img.size, os.path.getsize(OUT), "bytes")
