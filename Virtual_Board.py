import cv2
import mediapipe
import numpy as np
import os 
import HandTrack as htm
brushThickness=15
eraserThickness=100
folderpath="Project_1\\Resources\\Header_for_Painter"
myList=os.listdir(folderpath)
print(myList)
overlayList=[]
for imPath in myList:
    image =cv2.imread(f'{folderpath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header=overlayList[0]
drawColor=(255,0,255)
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector=htm.handDetector(min_detection_confidence=0.6)
xp,yp=0,0
imgCanvas=np.zeros((720,1280,3),np.uint8)
while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    img=detector.findHandes(img)
    lmList,_=detector.findPosition(img,draw=False)
    if len(lmList)!=0:
        #print(lmList)
        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:]
        fingurs=detector.finguresUp()
        #print(fingurs)
        if fingurs[1]and fingurs[2]:
            xp,yp=0,0
            print("selection mode")
            if y1<125:
                if 100<x1<200:
                    header=overlayList[0]
                    drawColor=(255,0,55) 
                elif 300<x1<450:
                    header=overlayList[1]
                    drawColor=(0,242,255)
                elif 450<x1<650:
                    header=overlayList[2]
                    drawColor=(0,0,255)
                elif 700<x1<850:
                    header=overlayList[3]
                    drawColor=(0,255,0)
                elif 900<x1<1000:
                    header=overlayList[4]
                    drawColor=(255,242,0)
                elif 1050<x1<1200:
                    header=overlayList[5]
                    drawColor=(0,0,0)
            cv2.rectangle(img,(x1,y1-25),(x2,y2+25),drawColor,cv2.FILLED)
        #5.if drawing mode -index finger is up
        if fingurs[1]and fingurs[2]==False:
            cv2.circle(img,(x1,y1),15,drawColor,cv2.FILLED)
            print("drawing mode")

            if xp==0 and yp==0:
                xp,yp=x1,y1
            if drawColor==(0,0,0):
                cv2.line(img,(xp,yp),(x1,y1),drawColor,eraserThickness)
                cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,eraserThickness)
            else:
                cv2.line(img,(xp,yp),(x1,y1),drawColor,brushThickness)
                cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)
            xp,yp=x1,y1
    imgGray=cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)
    imgInv=cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
    imgInv=cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img=cv2.bitwise_and(img,imgInv)
    img=cv2.bitwise_or(img,imgCanvas)
    img[0:125,0:1280]=header
    cv2.imshow("Hi",img)
    cv2.imshow("CanvasBlack",imgCanvas)
    cv2.imshow("CanvasWhite",imgInv)
    cv2.waitKey(1)
