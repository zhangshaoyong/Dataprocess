import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def read_filename(path):
    for filename in os.listdir(path):
        #filename1 = os.path.abspath(filename)
        all_filename.append(filename)
        all_file.append(path + filename)
    print all_file[0]
    return all_filename, all_file
def shift(img_1,img_2,step):
    for i in range(weight-1):
        for j in range(height-1):
            v = j-step
            if (v)<0:
                v = 0
                im2[i][v] = 0
            img_1[i][j] = img_2[i][v]
    return img_1
pathgenerate = '/media/disk/zhangshaoyong/jupyter/depthmap/generate/'
#读取文档中的（一行中有两个文件，用空格隔开，把这两个文件路径名字分别存储到两个文档中（用于处理双目数据集的）
file1 = []
finename2 = open('/media/disk/zhangshaoyong/jupyter/depthmap/02.txt', 'r').readlines()
finename3 = open('/media/disk/zhangshaoyong/jupyter/depthmap/03.txt', 'r').readlines()


#for i in finename3:
    #file1.append(i.split(' '))
for i in range(len(finename2)):
    finename2[i] = finename2[i].strip('\n')
    finename3[i] = finename3[i].strip('\n')
    print finename2[i]
    print finename3[i]


    im1 = Image.open(finename2[i])
    im2 = Image.open(finename3[i])
    #将两张图片的亮度调为原来的一半像素值统一在0到128之间
    im1 = im1.point(lambda p: p*0.5)
    im2 = im2.point(lambda p: p*0.5)
    #保存两张图片
    im1.save('/media/disk/zhangshaoyong/jupyter/depthmap/1.jpg')
    im2.save('/media/disk/zhangshaoyong/jupyter/depthmap/2.jpg')
    #将图二的像素值调为128到256之间，并保存
    im2 = cv2.imread('/media/disk/zhangshaoyong/jupyter/depthmap/2.jpg')
    im22 = 128*np.ones((im2.shape[0], im2.shape[1], im2.shape[2]),dtype=im2.dtype)
    im2 = im2 + im22

    im1 = cv2.imread('/media/disk/zhangshaoyong/jupyter/depthmap/1.jpg')
    weight, height, channel = im1.shape
    img21 = np.zeros((im1.shape[0], im1.shape[1], im1.shape[2]),dtype=im1.dtype)
    img21 = shift(img21,im2,0)       
    im = im1 - img21
    #删除两张无用的图片
    os.remove('/media/disk/zhangshaoyong/jupyter/depthmap/1.jpg')
    os.remove('/media/disk/zhangshaoyong/jupyter/depthmap/2.jpg')
    i = str(i)
    plt.imsave(pathgenerate + i + '.png', im)
