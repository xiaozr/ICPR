import os 
from PIL import Image
# mode of train image
cur_dir=os.getcwd()
x=open('mode_train.txt','w') 
path=os.path.join(os.getcwd(),'ICPR_text_train_part2_20180313','image_9000')
os.chdir(path)
imgs=os.listdir(path)
for files in imgs:
	img=Image.open(files)
	#w,h,c=img.size
	rbg=img.mode
	#x.write(files)
	x.write(rbg+'\n')
x.close()	

#mode of test image
os.chdir(cur_dir) 
x=open('mode_test.txt','w') 
path=os.path.join(os.getcwd(),'ICPR_text_train_part1_20180316','train_1000','image_1000')
os.chdir(path)
imgs=os.listdir(path)
for files in imgs:
	img=Image.open(files)
	#w,h,c=img.size
	rbg=img.mode
	#x.write(files)
	x.write(rbg+'\n')
x.close()
