import os
cur_dir=os.getcwd()
test_dir=os.path.join(cur_dir,'ICPR_text_train_part1_20180316/train_1000')
train_dir=os.path.join(cur_dir,'ICPR_text_train_part2_20180313/')

#to  test txt dir
txt_dir=os.path.join(test_dir,'txt_1000')
os.chdir(txt_dir)
files=os.listdir(txt_dir)
test_file=open(txt_dir+'/test.txt','w')
for file in files:
	name=os.path.splitext(file)[0]
	test_file.write(name+'\n')
test_file.close()

#to train txt dir 
txt_dir=os.path.join(train_dir,'txt_9000')
files=os.listdir(txt_dir)
test_file=open(txt_dir+'/trainval.txt','w')
for file in files:
	name=os.path.splitext(file)[0]
	test_file.write(name+'\n')
test_file.close()
