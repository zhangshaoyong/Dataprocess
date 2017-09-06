#!/usr/bin/python
# -*- coding:utf8 -*-
# 防止中文注释报错
#读取一个文件夹中所有的文件名并将其与绝对路径写入文件中
import os
filename = os.listdir('/media/disk/zhangshaoyong/NewFolder/A/B/00/00/train_colors0/')
if os.path.exists("/media/disk/zhangshaoyong/NewFolder/A/B/00/00/traincolor0.txt")== True:#判断一个文件是否存在。
    #如果判断一个文件夹是否存在用 os.path.isdir（）
    os.remove("/media/disk/zhangshaoyong/NewFolder/A/B/00/00/traincolor0.txt")
os.mknod("/media/disk/zhangshaoyong/NewFolder/A/B/00/00/traincolor0.txt")
fp = open("/media/disk/zhangshaoyong/NewFolder/A/B/00/00/traincolor0.txt", 'w')
for i in filename:
    abspathname = '/media/disk/zhangshaoyong/NewFolder/A/B/00/00/train_colors0/'+i
    fp.write(abspathname+'\n')
fp.close

#批量resize图片
import Image
height_size = 256
width_size = 256
def resize_image(input, height, width, output):
    im = Image.open(input)
    out = im.resize((height, width), Image.ANTIALIAS)
    out.save(output)
filenames = []
output_path = '/media/disk/zhangshaoyong/NewFolder/A/B/00/256256depth/'
filemerge = open('/media/disk/zhangshaoyong/NewFolder/A/B/00/01/traindepths0.txt','r').readlines()
for i in range(len(filemerge)):
    j = str(i)
    print i
    input_name = filemerge[i].strip('\n')
    output_name = output_path + j + '.jpg'
    resize_image(input_name,height_size, width_size, output_name)
