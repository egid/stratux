#!/usr/bin/env python


from PIL import ImageDraw, ImageFont

from PIL import Image

import sys


font2 = ImageFont.truetype('../fonts/C&C Red Alert [INET].ttf', 12)

uat_current = 123
uat_max = 1230

es_current = 5920
es_max = 9000

im = Image.new("1", (128, 64), "black")

draw = ImageDraw.Draw(im)

pad = 2 # Two pixels on the left and right.
text_margin = 25
# UAT status.
draw.text((50, 0), "UAT", font=font2, fill=255)
# "Status bar", 2 pixels high.
status_bar_width_max = 128 - (2 * pad) - (2 * text_margin)
status_bar_width = int((float(uat_current) / uat_max) * status_bar_width_max)
draw.rectangle((pad + text_margin, 14, pad + text_margin + status_bar_width, 20), outline=255, fill=255) # Top left, bottom right.
# Draw the current (left) and max (right) numbers.
draw.text((pad, 14), str(uat_current), font=font2, fill=255)
draw.text(((2*pad) + text_margin + status_bar_width_max, 14), str(uat_max), font=font2, fill=255)
# ES status.
draw.text((44, 24), "1090ES", font=font2, fill=255)
status_bar_width = int((float(es_current) / es_max) * status_bar_width_max)
draw.rectangle((pad + text_margin, 34, pad + text_margin + status_bar_width, 40), outline=255, fill=255) # Top left, bottom right.
# Draw the current (left) and max (right) numbers.
draw.text((pad, 34), str(es_current), font=font2, fill=255)
draw.text(((2*pad) + text_margin + status_bar_width_max, 34), str(es_max), font=font2, fill=255)
# Other stats.
draw.text((pad, 45), "CPU: 45.0C, Towers: 8", font=font2, fill=255)



del draw

im.save(sys.stdout, "PNG")
