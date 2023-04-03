import cv2
import numpy as np
import random as r


NOTATION = '0123456789ABCDEF'

def numeral_system(number, base):  #5진수 변환
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n

def decorder(image,x,y):
    if(image.item(y,x,2)==255 and image.item(y,x,1)==0):
        return 0
    else:
        if(image.item(y,x,1)==255 and image.item(y,x,2)==0):
            return 1
        else:
            if(image.item(y,x,0)==255 and image.item(y,x,2)==0):
                return 2
            else:
                if(image.item(y,x,0)==255 and image.item(y,x,1)==255 and image.item(y,x,2)==255):
                    return 4
                else:
                    if(image.item(y,x,0)==0 and image.item(y,x,1)==0 and image.item(y,x,2)==0):
                        return 3


def red(x, y) :
    img.itemset((y, x, 2), 255) #(x,y)에 색 지정

def green(x, y) :
    img.itemset((y, x, 1), 255)

def blue(x, y) :
    img.itemset((y, x, 0), 255)

def black(x, y) :
    pass

def white(x, y) :
    img.itemset((y, x, 0), 255)
    img.itemset((y, x, 1), 255)
    img.itemset((y, x, 2), 255)



sentence = 'Soongyuya Munpyeongan' #데이터 변환
Data = []
Data2 = []
leng = len(sentence)


for i in range(leng) :
    Data.append(numeral_system(ord(sentence[i]), 5))

print(Data)

for i in range(leng) :
    Data2.append(str(Data[i])[0])
    Data2.append(str(Data[i])[1])
    Data2.append(str(Data[i])[2])

print(Data2)


size = 21               #opencv start
img = np.zeros((size, size, 3), np.uint8)
cnt = 0
Decode=str()

for y in range(size) :
    for x in range(size) :
        if cnt<leng*3 : 
            color = int(Data2[cnt])
            cnt+=1

        else :
            color = 3

        if color == 0 :
            red(x, y)

        elif color == 1 :
            green(x, y)

        elif color == 2 :
            blue(x, y)

        elif color == 3 :
            black(x, y)

        elif color == 4 :
            white(x, y)

for y in range(size):#번역을 위한 반복문
    for x in range(0,7):
        Decode = Decode + chr(decorder(img,3*x,y)*25+(decorder(img,3*x+1,y)*5)+(decorder(img,3*x+2,y))) #번역하여 출력함
        
print(Decode)
bigimg = cv2.resize(img, dsize = (500, 500), interpolation = cv2.INTER_AREA)

#cv2.imshow('sample', img)
cv2.imshow('sampleup', bigimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('images/img.bmp', img)
cv2.imwrite('images/bigimg.bmp', bigimg)