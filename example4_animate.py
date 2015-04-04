import math
import time

import SSD1306

import Image
import ImageFont
import ImageDraw

disp = SSD1306.SSD1306_128_64()

disp.begin()

width = disp.width
height = disp.height

disp.clear()
disp.display()

image = Image.new('1', (width, height))
font = ImageFont.load_default()

# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

# Create drawing object.
draw = ImageDraw.Draw(image)

text= "Intel Edison is the best thing since sliced bread!"
maxwidth, unused = draw.textsize(text, font=font)

# Set animation and sine wave parameters.
amplitude = height/4
offset = height/2 - 4
velocity = -3
startpos = width

# Animate text moving in sine wave.
print 'Press Ctrl-C to quit.'
pos = startpos
while True:
	# Clear image buffer by drawing a black filled box.
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	# Enumerate characters and draw them offset vertically based on a sine wave.
	x = pos
	for i, c in enumerate(text):
		# Stop drawing if off the right side of screen.
		if x > width:
			break
		# Calculate width but skip drawing if off the left side of screen.
		if x < -10:
			char_width, char_height = draw.textsize(c, font=font)
			x += char_width
			continue
		# Calculate offset from sine wave.
		y = offset+math.floor(amplitude*math.sin(x/float(width)*2.0*math.pi))
		# Draw text.
		draw.text((x, y), c, font=font, fill=255)
		# Increment x position based on chacacter width.
		char_width, char_height = draw.textsize(c, font=font)
		x += char_width
	# Draw the image buffer.
	disp.image(image)
	disp.display()
	# Move position for next frame.
	pos += velocity
	# Start over if text has scrolled completely off left side of screen.
	if pos < -maxwidth:
		pos = startpos
	# Pause briefly before drawing next frame.
	time.sleep(0.1)
