from PIL import Image
import os 
# data 包含三个文件夹，img,txt,annotation
cur_dir=os.getcwd()
data_name='[update] ICPR_text_train_part1_20180316/train_1000'
img_name='image_1000'
xml_name='Annotation_1000'
text_name='txt_1000'
#进入data路径
data_dir=os.path.join(cur_dir,data_name)
os.chdir(data_dir)
#创建 annotation 文件夹
cmd='mkdir '+xml_name
os.system(cmd)
img_dir=os.path.join(data_dir,img_name)
xml_dir=os.path.join(data_dir,xml_name)
text_dir=os.path.join(data_dir,text_name)
#进入 text 文件夹中
os.chdir(text_dir)
for root,dirs,files in os.walk(text_dir):
	for file in files:
		text_file=open(file,'r',encoding='UTF-8')
		#获得无后缀txt文件名
		Name=os.path.splitext(file)[0]
		#print(Name)
		xml_file=open(xml_dir+'/'+Name+'.xml','w')
		#获得图片得大小
		img_file=Image.open(img_dir+'/'+Name+'.jpg')
		width,height=img_file.size
		#写 xml 文件
		xml_file.write('<annotation>\n')
		xml_file.write('	<folder>ICPR</folder>\n')
		xml_file.write('	<filename>'+Name+'.jpg'+'</filename>\n')
		xml_file.write('	<source>\n')
		xml_file.write('	<size>\n')
		xml_file.write('		<width>'+str(width)+'</width>\n')
		xml_file.write('		<height>'+str(height)+'</height>\n')
		xml_file.write('		<depth>'+str(3)+'</depth>\n')
		xml_file.write('	</size>\n')
		xml_file.write('	<segmented>'+str(0)+'</segmented>\n')
		for box in text_file:
			coordinate=box.split(',')
			#计算左下角和右上角的坐标
			xmin=min(coordinate[0],coordinate[2])
			ymin=min(coordinate[1],coordinate[7])
			xmax=max(coordinate[4],coordinate[6])
			ymax=max(coordinate[3],coordinate[5])
			#写 bndbox 部分
			xml_file.write('	<object>\n')
			xml_file.write('		<name>'+'text'+'</name>\n')
			xml_file.write('		<pose>Unspecified</pose>\n')
			xml_file.write('		<truncated>0</truncated>\n')
			xml_file.write('		<difficult>0</difficult>\n')
			xml_file.write('		<bndbox>\n')
			xml_file.write('			<xmin>'+str(xmin)+'</xmin>\n')
			xml_file.write('			<ymin>'+str(ymin)+'</ymin>\n')
			xml_file.write('			<xmax>'+str(xmax)+'</xmax>\n')
			xml_file.write('			<ymax>'+str(ymax)+'</ymax>\n')
			xml_file.write('		<bndbox>\n')
			xml_file.write('	<object>\n')
		xml_file.write('<annotation>\n')
		text_file.close()
		xml_file.close()



