import cv2
import numpy as np
import time as t

def decorder(image, x, y):
    if(image.item(y, x, 2)==255 and image.item(y, x, 1)==0):
        return 0
    elif(image.item(y, x, 1)==255 and image.item(y, x, 2)==0):
        return 1
    elif(image.item(y, x, 0)==255 and image.item(y, x, 2)==0):
        return 2
    elif(image.item(y, x, 0)==255 and image.item(y, x, 1)==255 and image.item(y, x, 2)==255):
        return 4
    elif(image.item(y, x, 0)==0 and image.item(y, x, 1)==0 and image.item(y, x, 2)==0):
        return 3

Decode=str()
size = int(input())
img = cv2.imread('image.png')
cv2.imshow('ss', img)

k = cv2.waitKey(0) 
if k == 27 : # ESC키
    cv2.destroyAllWindows()

orgimg = cv2.resize(img, dsize = (size, size), interpolation = cv2.INTER_NEAREST)  #확대된 이미지 원본으로 축소
cv2.imshow('s', orgimg)

x = 0
y = 0

for k in range(size**2):#번역을 위한 반복문
        if k % size != 0 :
            x+=1
        else : 
            y+=1
            x=0

        


        ch = chr(decorder(orgimg, 3*x, y)*25 + decorder(orgimg, 3*x+1, y)*5 + decorder(orgimg, 3*x+2, y))
        Decode = Decode + ch #번역하여 출력함

print(Decode)

cv2.waitKey(0)  #키보드 입력 대기
cv2.destroyAllWindows()