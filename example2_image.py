import time
import SSD1306
import Image


disp = SSD1306.SSD1306_128_64()

disp.begin()
disp.clear()
disp.display()

image = Image.open('happycat_oled_64.ppm').convert('1')

disp.image(image)
disp.display()
