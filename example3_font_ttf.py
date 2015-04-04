import time

import SSD1306

import Image
import ImageDraw
import ImageFont


disp = SSD1306.SSD1306_128_64()

disp.begin()

disp.clear()
disp.display()

top = 2
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('Naughty Cartoons.ttf',18)
# Write two lines of text.
draw.text((0, top),    "  Intel",  font=font, fill=255)
draw.text((0, top+30), ' Edison', font=font, fill=255)

# Display image.
disp.image(image)
disp.display()
