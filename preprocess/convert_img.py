import os 
from PIL import Image

train_path = os.path.join(os.getcwd(),'ICPR_text_train_part2_20180313','image_9000')
test_path = os.path.join(os.getcwd(),'ICPR_text_train_part1_20180316','train_1000','image_1000')

# change the mode of train image
os.chdir(train_path)
imgs = os.listdir(train_path)
for files in imgs:
	img = Image.open(files)
	#w,h,c=img.size
	style = img.mode
	if(style == 'P'):
		img = img.convert('RGB')
		img.save(files)

# change the mode of test image
os.chdir(test_path)
imgs = os.listdir(test_path)
for files in imgs:
	img = Image.open(files)
	#w,h,c=img.size
	style = img.mode
	if(style == 'RGBA'):
		img = img.convert('RGB')
		img.save(files)
