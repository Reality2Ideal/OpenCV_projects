import cv2
import numpy as np

# 从电脑摄像头获取图像
cap = cv2.VideoCapture(0)

while(1):
    res,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # 设定蓝色阈值
    lower_blue = np.array([100,43,46])
    upper_blue = np.array([124,255,255])
    # 设定红色阈值
    lower_red = np.array([0,43,46])
    upper_red = np.array([10,255,255])
    # 设定绿色阈值
    lower_green = np.array([35,43,46])
    upper_green = np.array([77,255,255])

    # 先提取蓝色
    mask1 = cv2.inRange(hsv,lower_blue,upper_blue)
    # 在提取红色
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    # 提取绿色
    mask3 = cv2.inRange(hsv,lower_green,upper_green)

    # 对图像进行位运算
    res1 = cv2.bitwise_and(frame,frame,mask = mask1)
    res2 = cv2.bitwise_and(frame,frame,mask = mask2)
    res3 = cv2.bitwise_and(frame,frame,mask = mask3)

    res_temple = cv2.add(res1,res2)
    res = cv2.add(res_temple,res3)

    cv2.imshow("res",res)

    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()


