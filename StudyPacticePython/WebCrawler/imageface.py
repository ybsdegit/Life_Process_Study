#!/practice/Study_Test python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 21:19
# @Author  : yb.w
# @File    : imageface.py
# @define  : 检测图片中的人脸,用矩形框标出
# 使用OpenCV自带库参数数据

# 1.导入库
import cv2

# 2.加载图片，加载模型

# 待检测的图片路径
imagepath = r'./face1.jpg'
# 获取训练好的人脸的参数数据，这里直接使用默认值
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_alt.xml')
# 读取图片
image = cv2.imread(imagepath)

# 3.对图片灰度化处理
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4.检测人脸，探测图片中的人脸
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5, 5),
    # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)
print("发现{0}个人脸!".format(len(faces)))

# 5.标记人脸
for(x,y,w,h) in faces:
        # 1.原始图片 2.人脸坐标原点 3.标记的高度 4，线的颜色 5，线宽
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

# 6.显示图片
cv2.imshow("Find Faces!", image)

# 7.暂停窗口
cv2.waitKey(5)

# 8.销毁窗口
cv2.destroyAllWindows()