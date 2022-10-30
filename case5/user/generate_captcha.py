from captcha.image import ImageCaptcha
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

s = generate_random_string(5)

image = ImageCaptcha()
data = image.generate(s)

image.write(s, 'captcha.png')
