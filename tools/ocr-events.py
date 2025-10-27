#!/home/archid/python/.ocr/bin/python

import glob
import os
import pytesseract
import PIL.Image

# Open the output file
hf = open("events.txt", "w")
etypes=['boat', 'outpost', 'road']

for etype in etypes:
	files = glob.glob(f'../html/images/frosthaven/events/{etype}/*-f.png')
	for file in files:
		name=os.path.basename(file)
		text = pytesseract.image_to_string(PIL.Image.open(file))
		hf.write(name + "|" + text.replace('\n',' ') + '\n')




