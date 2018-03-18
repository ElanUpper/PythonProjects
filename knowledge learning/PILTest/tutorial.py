# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tutorial
   Description :
   Author :       elan
   date：          2/18/2018
-------------------------------------------------
   Change Activity:
                   2/18/2018:
-------------------------------------------------
"""

from PIL import ImageColor, Image, ImageFilter

# RGB值再加上alpha值（通透度，透明度）
# alpha值为0时，无论是什么颜色均变为透明
print(ImageColor.getcolor('red', 'RGBA')) ;
print(ImageColor.getcolor('black', 'RGB')) ;

# create image
# mode = RGB/RGBA  (width,height)  color
#img1 = Image.new('RGB', (100, 100), 'red');
#img2 = Image.new('RGB', (100, 100), '#FFFF00');
#img3 = Image.new('RGBA', (200, 100), (255, 0, 0, 120));

# 查看image信息
img = Image.open('C:\\Users\\elan\\Desktop\\pic\\100.jpg');
(img_width, img_height) = img.size;
#print('width {0}, height {1}, format: {2}, desc: {3}'.format(img_width, img_height, img.format, img.format_description))
#img.save('C:\\Users\\elan\\Desktop\\pic\\101.jpg');
# 使用默认查看器打开
#img.show();

# 剪切复制image  坐标顺序 (left, upper, right, lower) [左, 右) [顶, 底)
#img_cut = img.crop((100, 200, img_width-100, img_height-200));
# 使用windows自带编辑工具查看区域坐标 然后直接填入
img_cut = img.crop((490, 90, 767, 457));
img_copy = img.copy();  # 复制一个新的Image对象
img_copy.paste(img_cut, (20,0)) # 复制到哪里 (left, upper)
#img_copy.show();

# 打印x*y复制效果
img_phantom = img.copy();
for x_position in range(0, img_width, img_cut.size[0]) :
	for y_position in range(0, img_height, img_cut.size[1]):
		img_phantom.paste(img_cut, (x_position, y_position))
#img_phantom.show();


# 调整图片大小 缩小会失真
img_resize = img.copy().resize((1300, 1300)); # (width, height)
#img_resize.show();


## 图片旋转 逆时针旋转
#print(img.size)
img_rotate = img.rotate(270, expand=True);
#img_rotate.show();
#print(img_rotate.size)


# 图片翻转 Image.FLIP_LEFT_RIGHT:水平翻转 Image.FLIP_TOP_BOTTOM:垂直翻转
#img.transpose(Image.FLIP_LEFT_RIGHT).show();


# 图像过滤
# img.show(); # 对比完成后样式
# 高斯模糊
#img.filter(ImageFilter.GaussianBlur).show();
# 普通模糊
#img.filter(ImageFilter.BLUR).show();
# 边缘增强
#img.filter(ImageFilter.EDGE_ENHANCE).show();
# 找到边缘
#img.filter(ImageFilter.FIND_EDGES).show();
# 浮雕
#img.filter(ImageFilter.EMBOSS).show();
# 轮廓
#img.filter(ImageFilter.CONTOUR).show();
# 锐化
#img.filter(ImageFilter.SHARPEN).show();
# 平滑
#img.filter(ImageFilter.SMOOTH).show();
# 细节
#img.filter(ImageFilter.DETAIL).show();

