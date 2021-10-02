import cv2
from PIL import Image
import matplotlib.pyplot as plt

img_flag = cv2.imread("D:\\Open_CV_workplace\\image\\flag.jpg",1)

# 国旗进行从左向右的渐变处理，越往右越浅
img_flag = cv2.cvtColor(img_flag,cv2.COLOR_BGR2BGRA)
after_flag = img_flag[0:960,0:960]
b,g,r,alpha = cv2.split(after_flag)
h,l,a = after_flag.shape
for i in range(l):
    v = (255/l)*(l - i)
    alpha[:,i] = v
after_flag = cv2.merge([b,g,r,alpha])
cv2.imwrite("after_flag.png",after_flag)
# 微信图片进行处理
img_wechat = Image.open("D:\\Open_CV_workplace\\image\\333.png")
img_wechat = img_wechat.convert('RGBA')
final_flag = Image.open("D:\\Open_CV_workplace\\image\\after_flag.png")
final_flag = final_flag.convert('RGBA')

final_image = Image.blend(img_wechat,final_flag,0.8)

final_image.save("final_image.png")

cv2.waitKey()
cv2.destroyAllWindows()


