#coding: utf-8
#image_merge.py

import Image
import os

def image_resize(img, size=(512, 256)):
    try:
        if img.mode not in ('L', 'RGB'):
            img = img.convert('RGB')
        img = img.resize(size)
    except Exception, e:
        pass
    return img
def image_merge(images, output_dir = '/media/disk/zhangshaoyong/pix2pix/output/mergedataset/', output_name = '', restriction_max_width=None, restriction_max_height = None):
    max_height = 0
    total_width = 0
    for img_path in images:
        if os.path.exists(img_path):
            img = Image.open(img_path)
            width, height = img.size
            if height > max_height:
                max_height = height
            total_width+= width
    new_img = Image.new('RGB', (total_width, max_height), 255)
    x = y = 0
    for img_path in images:
        if os.path.exists(img_path):
            img = Image.open(img_path)
            width, height = img.size
            new_img.paste(img, (x, y))
            x+= width
    if restriction_max_height and max_height > restriction_max_height:
        ratio = restriction_max_width/ float(max_height)
        max_height = restriction_max_height
        total_width = int(total_width*ratio)
        new_img = image_resize(new_img, size = (total_width, max_height))
        new_img = image_resize(new_img, size = (512, 256))

    if restriction_max_width and total_width > restriction_max_width:
        ratio = restriction_max_width / float(total_width)
        max_height = int(max_height*ratio)
        total_width = restriction_max_width
        new_img = image_resize(new_img, size = (total_width, max_height))
        new_img = image_resize(new_img, size = (512, 256))
        
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    save_path = '%s%s' % (output_dir, output_name)
    new_img.save(save_path)
    return save_path
    
if __name__ == '__main__':
    y = 0
    filename = []
    filemerge = open('/media/disk/zhangshaoyong/pix2pix/output/merge.txt','r').readlines()
    for i in filemerge:
        filename.append(i.split(' '))
    
    for t in range(len(filename)):
    	j = str(t)
        output_name = j + '.jpg'
        image_merge(images=[filename[t][0], filename[t][1].strip('\n')], output_dir = '/media/disk/zhangshaoyong/pix2pix/output/mergedataset/', output_name = output_name, restriction_max_width=512, restriction_max_height = 256)
        print 'merge ' + j
       