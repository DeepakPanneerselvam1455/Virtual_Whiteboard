import mediapipe as mp
#import mediapipe.python.solutions.drawing_utils as du
#import mediapipe.python.solutions.hands as h

import cv2
import time
import math
class handDetector():
    def __init__(self,
               static_image_mode=False,
               max_num_hands=2,
               model_complexity=1,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5):       
        self.static_image_modemode = static_image_mode
        self.max_num_hands = max_num_hands
        self.model_complexity=model_complexity
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence=  min_tracking_confidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.static_image_modemode,self.max_num_hands,self.model_complexity,self.min_detection_confidence,self.min_tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds=[4,8,12,16,20]
    def findHandes(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)  # Use self.hands to access the attribute
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:  
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self, img, handNo=0, draw=True):
        self.lmList = []
        xList = []
        yList = []
        self.bbox=[]
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]  
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.lmList.append([id, cx, cy])
                if draw:
                        cv2.circle(img,(cx,cy),2,(255,0,0),cv2.FILLED)
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            xmin = max(0, xmin - 20)
            xmax = min(w, xmax + 20)
            ymin = max(0, ymin - 20)
            ymax = min(h, ymax + 20)
            self.bbox = (xmin, ymin, xmax, ymax)
            if draw:
                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        return  self.lmList,self.bbox
    def finguresUp(self):
        fingers=[]
        #for thumb left <,right >
        #for virtual painter change as "<"
        if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #for 4 fingers
        for id in range(1,5): 
            if self.lmList[self.tipIds[id]][2]<self.lmList[self.tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers
    def findDistane(self,p1,p2,img,draw=True,r=15,t=2):
        x1,y1=self.lmList[p1][1:]
        x2,y2=self.lmList[p2][1:]
        cx,cy=(x1+x2)//2,(y1+y2)//2
        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,0,255),t)
            cv2.circle(img,(x1,y1),r,(255,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),r,(255,0,255),cv2.FILLED)
            cv2.circle(img,(cx,cy),r,(0,0,255),cv2.FILLED)
        length=math.hypot(x2-x1,y2-y1)
        return length,img,[x1,y1,x2,y2,cx,cy]
def main():
    ptime=0
    currenttime=0
    cap=cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success,img=cap.read()
        img=cv2.flip(img,1)
        img=detector.findHandes(img,False)
        lmList,_=detector.findPosition(img,handNo=0,draw=True)
        if len(lmList)!=0:
            print(lmList[4])
        #imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        fingers=detector.finguresUp()
        currenttime=time.time()
        fps=1/(currenttime-ptime)
        ptime=currenttime
        cv2.putText(img,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0,5),3)
        cv2.imshow("Wedcam",img)
        cv2.waitKey(1)    
if __name__=="__main__":
    main()
