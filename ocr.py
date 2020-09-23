import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("/home/pauloricardo/reading-bot-me_irl/img/me_irl/me_irl2020-09-23 13:53:27.438254.jpeg") # the second one 
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
configuration = ("-l eng")
text = pytesseract.image_to_string(im, config=configuration)
print(text)