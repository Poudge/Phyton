import random
from captcha.image import ImageCaptcha
#
#pattern = "12345qwerty"
#
#img_captcha = ImageCaptcha(width=300, height=200)
#img_captcha.write(pattern, "capcha.png")
import random

pattern= []

for i in range(33, 127):
    pattern.append(chr(i))

#print(pattern)

pattern1 = ""

for i in range(10):
    pattern1 += random.choice(pattern)


print(pattern1)

img_captcha = ImageCaptcha(width=300, height=200)
img_captcha.write(pattern1, "capcha.png")

