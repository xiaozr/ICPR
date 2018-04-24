数据的预处理过程：
    原始数据包括两个文件夹，一个文件夹包含 Image , 一个文件夹包含 Bounding Box 的 TXT 文件
    1）将 TXT 文件的 Bounding box 信息转化为 Annotation/...xml 格式，使用 txt_xml.py 文件
    2）Image 文件中，训练数据的图像包含两种格式，一个是 RGB，一个是 RGBA，测试数据图像也包含两种格式，一个是 RGB 一个是 P,使用 model_img.py 文件
    3）将非 RGB 格式的图片转化为 RGB 格式，使用 convert_img.py 文件
    4）分别生成包含训练图片和测试图片名称的 TXT 文件，放在 txt 文件夹下，使用 which_test_train.py 文件
    5）使用 creat_list.sh 文件分别生成训练图片和标注，测试图片和标注对齐的 trainval.txt 和 test.txt 文件
    6）使用 creat_data.sh 文件根据 trainval.txt 和 test.txt 文件生成训练和测试 lmdb 数据
