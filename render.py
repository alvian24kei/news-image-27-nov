#!/usr/bin/env python3
"""Draw "The World Today" — an original 1024x1024 front page summing up
Friday 27 November 2026. Every illustration is drawn from scratch with PIL
primitives; no photos, logos or copied images. Type is set in Noto Serif /
Noto Sans. Run: python3 render.py  ->  writes entry.png next to this file."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (22, 22, 22)
RED = (168, 28, 48)
NAVY = (24, 68, 112)
GREY = (96, 92, 84)
CARD = (255, 253, 248)
CARD_BLUE = (231, 238, 245)
CARD_GOLD = (248, 238, 224)
CARD_GREEN = (232, 240, 230)
ORANGE = (214, 92, 22)
GOLD = (238, 182, 48)

SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
SERIF_D = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"

canvas = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(canvas)


def font(path, size):
    return ImageFont.truetype(path, size)


def width_of(text, fnt):
    return d.textlength(text, font=fnt)


def flow(text, fnt, max_w):
    """Split text into lines that fit max_w."""
    out, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if width_of(trial, fnt) <= max_w:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def block(text, fnt, x, y, max_w, gap, fill=INK):
    for line in flow(text, fnt, max_w):
        d.text((x, y), line, font=fnt, fill=fill)
        y += gap
    return y


def hline(x0, y, x1, thick=2, fill=INK):
    d.line([(x0, y), (x1, y)], fill=fill, width=thick)


def tag(text, x, y, colour=RED, size=19):
    d.text((x, y), text, font=font(SANS_B, size), fill=colour)
    return y + size + 7


# ---------------- Masthead ----------------
hline(34, 24, 990, 4)
d.text((512, 36), "THE WORLD TODAY", font=font(SERIF_D, 86), fill=INK, anchor="ma")
d.text((512, 128), "F R I D A Y,  2 7  N O V E M B E R  2 0 2 6", font=font(SANS_B, 22), fill=INK, anchor="ma")
hline(34, 164, 990, 2)
d.text((34, 172), "FIVE STORIES FROM AROUND THE WORLD", font=font(SANS_B, 17), fill=GREY)
d.text((990, 172), "FRIDAY EDITION", font=font(SANS_B, 17), fill=GREY, anchor="ra")
hline(34, 198, 990, 4)

# ---------------- Lead: Kuwait drone strike ----------------
y = 218
y = tag("MIDDLE EAST  •  KUWAIT", 34, y)
y = block("DRONE STRIKE IN KUWAIT KILLS TWO ITALIANS",
          font(SERIF_B, 46), 34, y, 560, 52)
y += 6
block("Iranian drones hit a vital site in Kuwait, killing two Italian "
      "technicians working for defence group Rheinmetall. Kuwait blames "
      "Iran; Tehran denies it.",
      font(SERIF, 20), 34, y, 560, 26)

# Lead art: night sky, drones, blast over a rooftop (original drawing)
AX, AY, AW, AH = 622, 218, 368, 262
d.rounded_rectangle([AX, AY, AX + AW, AY + AH], radius=8,
                    fill=(30, 34, 66), outline=INK, width=2)
for sx, sy in [(650, 250), (700, 236), (760, 258), (830, 240), (900, 252),
               (950, 238), (680, 300), (940, 300), (740, 330), (880, 330)]:
    d.ellipse([sx, sy, sx + 3, sy + 3], fill=(250, 250, 240))
# rooftops
d.rectangle([AX, AY + AH - 58, AX + AW, AY + AH], fill=(52, 52, 66))
d.rectangle([AX + 30, AY + AH - 96, AX + 110, AY + AH - 58], fill=(44, 44, 58))
d.rectangle([AX + 250, AY + AH - 84, AX + 330, AY + AH - 58], fill=(44, 44, 58))
for wx in range(AX + 42, AX + 100, 16):
    d.rectangle([wx, AY + AH - 88, wx + 8, AY + AH - 78], fill=(238, 182, 48))
# blast
bx, by = AX + 190, AY + 130
d.polygon([(bx - 58, by + 52), (bx - 34, by - 6), (bx - 12, by + 22),
           (bx, by - 48), (bx + 14, by + 16), (bx + 36, by - 10),
           (bx + 56, by + 52)], fill=ORANGE, outline=(245, 196, 60), width=2)
d.polygon([(bx - 24, by + 52), (bx - 8, by + 14), (bx + 6, by + 32),
           (bx + 22, by + 52)], fill=GOLD)
# drones
for dx, dy in [(AX + 60, AY + 66), (AX + 300, AY + 52)]:
    d.ellipse([dx - 12, dy - 6, dx + 12, dy + 6], fill=(200, 200, 210), outline=INK, width=2)
    d.line([dx - 22, dy - 8, dx + 22, dy - 8], fill=(200, 200, 210), width=3)
    d.line([dx - 22, dy + 8, dx + 22, dy + 8], fill=(200, 200, 210), width=3)
d.text((AX + AW // 2, AY + AH - 30), "KUWAIT UNDER FIRE",
       font=font(SANS_B, 16), fill=(247, 242, 231), anchor="ma")

hline(34, 500, 990, 2)


# ---------------- Story cards ----------------
def card(x, y, w, h, fill, tag_text, head, body, draw_art, tcolour=RED):
    d.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=fill,
                        outline=INK, width=2)
    tx, tw = x + 16, w - 148
    ty = y + 12
    ty = tag(tag_text, tx, ty, colour=tcolour, size=17)
    ty = block(head, font(SERIF_B, 26), tx, ty, tw, 30)
    block(body, font(SERIF, 16), tx, ty + 4, tw, 20)
    ax0 = x + w - 132
    d.line([(ax0, y + 12), (ax0, y + h - 12)], fill=(182, 177, 166), width=1)
    draw_art(ax0 + 12, y + 12, 108, h - 24)


def art_falling_chart(x, y, w, h):
    cx, cy = x + w // 2, y + h // 2
    base = cy + 44
    for i, ht in enumerate([96, 74, 52, 30]):
        x0 = cx - 52 + i * 28
        d.rectangle([x0, base - ht, x0 + 20, base], fill=RED if i == 0 else NAVY,
                    outline=INK, width=2)
    d.line([cx - 56, base, cx + 56, base], fill=INK, width=3)
    d.line([cx - 52, cy - 56, cx + 52, cy - 6], fill=RED, width=4)
    d.polygon([(cx + 52, cy - 6), (cx + 34, cy - 8), (cx + 50, cy + 12)],
              fill=RED)


def art_missile_stop(x, y, w, h):
    cx, cy = x + w // 2, y + h // 2
    d.polygon([(cx - 46, cy - 8), (cx + 30, cy - 8), (cx + 48, cy),
               (cx + 30, cy + 8), (cx - 46, cy + 8)], fill=NAVY, outline=INK, width=2)
    d.polygon([(cx - 40, cy - 8), (cx - 28, cy - 26), (cx - 18, cy - 8)], fill=NAVY)
    d.ellipse([cx - 52, cy - 52, cx + 52, cy + 52], outline=RED, width=5)
    d.line([cx - 37, cy + 37, cx + 37, cy - 37], fill=RED, width=5)


def art_bank(x, y, w, h):
    cx, cy = x + w // 2, y + h // 2
    d.polygon([(cx - 52, cy - 34), (cx, cy - 56), (cx + 52, cy - 34)],
              fill=NAVY, outline=INK, width=2)
    for i in range(4):
        x0 = cx - 48 + i * 26
        d.rectangle([x0, cy - 26, x0 + 14, cy + 34], fill=(247, 242, 231),
                    outline=INK, width=2)
    d.rectangle([cx - 56, cy + 34, cx + 56, cy + 46], fill=NAVY,
                outline=INK, width=2)
    d.text((cx, cy + 6), "€", font=font(SERIF_B, 30), fill=GOLD, anchor="mm")


def art_down_arrow(x, y, w, h):
    cx, cy = x + w // 2, y + h // 2
    for i, ht in enumerate([30, 52, 74, 96]):
        x0 = cx - 52 + i * 28
        d.rectangle([x0, cy + 44 - ht, x0 + 20, cy + 44], fill=NAVY,
                    outline=INK, width=2)
    d.line([cx - 52, cy - 44, cx + 52, cy + 6], fill=RED, width=4)
    d.polygon([(cx + 52, cy + 6), (cx + 30, cy + 2), (cx + 48, cy + 26)],
              fill=RED)


card(34, 514, 462, 196, CARD_BLUE,
     "TRADE  •  WASHINGTON",
     "ALLIES REJECT NEW TARIFF CASE",
     "Partners dismiss the new US case for duties on 14 countries. "
     "World stocks slide as the tariff fight rattles markets.",
     art_falling_chart)
card(528, 514, 462, 196, CARD_GOLD,
     "WAR IN UKRAINE",
     "NORTH KOREA HALTS ARMS TO RUSSIA",
     "Pyongyang pauses KN-23 missile and artillery shipments and bars "
     "Russian military flights, Ukraine's intelligence says.",
     art_missile_stop)
card(34, 724, 462, 196, CARD_GREEN,
     "EUROPE  •  FRANKFURT",
     "EUROPE PICKS DE COS TO LEAD THE ECB",
     "Eurozone leaders choose Spain's Pablo Hernández de Cos to succeed "
     "Christine Lagarde, who steps down in February.",
     art_bank, tcolour=NAVY)
card(528, 724, 462, 196, CARD,
     "BRITAIN  •  LONDON",
     "UK MIGRATION FALLS TO 77,000",
     "Net migration drops to its lowest since 1997 outside the pandemic, "
     "ONS figures show — down from 204,000 a year earlier.",
     art_down_arrow, tcolour=NAVY)

# ---------------- Ticker ----------------
TY = 934
d.rectangle([0, TY, 1024, TY + 44], fill=INK)
d.text((34, TY + 11), "ALSO TODAY", font=font(SANS_B, 19), fill=GOLD)
ticker = ("Bangkok refinery blast hurts 9  •  13 dead in Indonesia mine flood  •  "
          "Ebola passes 12,000 in Congo  •  Black Friday crowds pack the shops")
size = 17
while width_of(ticker, font(SANS, size)) > 990 - 200 and size > 11:
    size -= 1
d.text((200, TY + 12), ticker, font=font(SANS, size), fill=(247, 242, 231))

# ---------------- Footer ----------------
d.text((512, 996), "Sources: Reuters, WSJ, BBC, CNN — 26–27 November 2026. "
       "All artwork drawn for this page.", font=font(SANS, 13), fill=GREY,
       anchor="ma")

canvas.save("entry.png")
print("saved entry.png")
