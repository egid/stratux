#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PIL import ImageDraw, ImageFont
from PIL import Image
from sparkblocks import spark

font = ImageFont.truetype('font/basis33/basis33.ttf', 15)
font2 = ImageFont.truetype('font/C&C Red Alert [INET].ttf', 13)
font3 = ImageFont.truetype('font/pixel_unicode/Pixel-UniCode.ttf', 15)

im = Image.new("1", (128, 64), "black")
draw = ImageDraw.Draw(im)


# Debug values
uat_current = 123
uat_max = 1230

es_current = 5920
es_max = 9000

cpu_temp = 45
cpu_load = 0.4

uat_hist = [1 ,.8,.6,.2,0 ,0 ,1 ,1 ,.2,.6]
es_hist =  [.8,.3,.2,.6,.4,.3,.6,.4,.3,1 ]

# Layout
pad = 2 # Two pixels on the left and right.
text_margin = 25
line = 13


# debug line numbers.
# draw.text((pad, 0),        "1", font=font, fill=255)
# draw.text((pad, line * 1), "2", font=font, fill=255)
# draw.text((pad, line * 2), "3", font=font, fill=255)
# draw.text((pad, line * 3), "4", font=font, fill=255)
# draw.text((pad, line * 4), "5", font=font, fill=255)


# System status
statusContent  = u"CPU {cpu_load} {cpu_temp}°".format(**vars())

draw.text((pad, 0), statusContent, font=font2, fill=255)


uatspark = spark(uat_hist)
uatnoun = "OK"

esspark = spark(es_hist)
esnoun = "GOOD"

# print(u"{uatspark}".format(**vars()))
draw.text((pad, line * 2), u"UAT  {uatspark} {uatnoun}".format(**vars()), font=font3, fill=255)


draw.text((pad, line * 3), u"1090 {esspark} {esnoun}".format(**vars()), font=font3, fill=255)

# "Status bar", 2 pixels high.
# status_bar_width_max = 128 - (2 * pad) - (2 * text_margin)
# status_bar_width = int((float(uat_current) / uat_max) * status_bar_width_max)
# draw.rectangle((pad + text_margin, 14, pad + text_margin + status_bar_width, 20), outline=255, fill=255) # Top left, bottom right.
#
# # Draw the current (left) and max (right) numbers.
# draw.text((pad, 14), str(uat_current), font=font, fill=255)
# draw.text(((2*pad) + text_margin + status_bar_width_max, 14), str(uat_max), font=font, fill=255)
#
# # ES status.
# draw.text((44, 24), "1090ES", font=font, fill=255)
# status_bar_width = int((float(es_current) / es_max) * status_bar_width_max)
# draw.rectangle((pad + text_margin, 34, pad + text_margin + status_bar_width, 40), outline=255, fill=255) # Top left, bottom right.
#
# # Draw the current (left) and max (right) numbers.
# draw.text((pad, 34), str(es_current), font=font, fill=255)
# draw.text(((2*pad) + text_margin + status_bar_width_max, 34), str(es_max), font=font, fill=255)
#
# # Other stats.
# draw.text((pad, 45), "CPU: 45.0C, Towers: 8", font=font, fill=255)



del draw

im.save(sys.stdout, "PNG")
