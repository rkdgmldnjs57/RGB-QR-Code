import cv2
import numpy as np

NOTATION = '0123456789ABCDEF'

def numeral_system(number, base):  #5진수 변환
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n


#픽셀에 색 할당

def red(x, y) :
    img.itemset((y, x, 2), 255) 

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


#ASCII 32~126 출력 가능 문자 (95개)


#####main#####


sentence = input()     #입력 문자열

Data = []              #ASCII 변환 5진 리스트
DivData = []           #각 자리 쪼갠 리스트
length = len(sentence) #문자열 길이

size = int((length*3)**0.5+1)


for i in range(length) :  #ASCII 변환 후 5진수로 변환하여 Data에 저장
    Data.append(numeral_system(ord(sentence[i])-32, 5)) #32~126 -> 0~94로 변환

print(size)


for i in range(length) :  #자리 쪼개어 DivData에 각각 3칸씩 저장
    if int(Data[i])<100 :
        DivData.append('0')
        DivData.append(str(Data[i])[0])
        DivData.append(str(Data[i])[1])
    else :
        DivData.append(str(Data[i])[0])
        DivData.append(str(Data[i])[1])
        DivData.append(str(Data[i])[2])



#opencv 시작

img = np.zeros((size, size, 3), np.uint8)  #qr코드 담을 빈 배열 생성
cnt = 0

for y in range(size) :                     #배열 전체 돌며 픽셀 별 데이터 입력
    for x in range(size) :                 #초과 입력 방지
        if cnt<length*3 : 
            color = int(DivData[cnt])
            cnt+=1
            
        else :
            break
        
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
            

if size**2 < length*3 :                      #초과 입력 알림
    print("Data loss")

    
bigimg = cv2.resize(img, dsize = (500, 500), interpolation = cv2.INTER_NEAREST)  #qr 코드 (500, 500) 으로 확대
cv2.imwrite('images/save.png', bigimg)  #.png 저장
cv2.imshow('Image', bigimg)  #qr코드 표시

cv2.waitKey(0)  #키보드 입력 대기
cv2.destroyAllWindows()
cv2.imwrite('images/save.png', bigimg)  #.png 저장
print('Saved')
