from PIL import Image
from tesseract import image_to_string

image = Image.open('Image.png')
Text = image_to_string(image)
if(Text[1] == +):
	print( Text[0], Text[1], Text[2], "=" int(Text[0])+int(Text[2])
else if(Text[1] == -):
	print( Text[0], Text[1], Text[2], "=" int(Text[0])-int(Text[2])
else if(Text[1] == *):
	print( Text[0], Text[1], Text[2], "=" int(Text[0])*int(Text[2])
else if(Text[1] == /):
	print( Text[0], Text[1], Text[2], "=" int(Text[0])/int(Text[2])
