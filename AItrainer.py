import cv2 as cv
import numpy as np
import time
import PoseModule as pm

cap= cv.VideoCapture('Test/test.mp4')

#cap= cv.VideoCapture(0)

detector= pm.PoseDetector()
count= 0
dir= 0
pTime= 0
while True:
    success, img= cap.read()
    cv.resize(img, (1280, 720))
    # img= cv.imread('Test/test.jpeg')
    img= detector.findPose(img, draw=False)
    lmList= detector.findPosition(img, draw=False)
    #print(lmList)
    if len(lmList)!= 0:
        # Left Arm
        #detector.findAngle(img, 11, 13, 15)
        #Right Arm
        angle= detector.findAngle(img, 12, 14, 16)
        per= np.interp(angle, (55, 150), (0,100))
        bar= np.interp(angle, (55,150), (650,100))
        print(angle, per)

        # Check for the dumbbell curls
        color= (255,0,255)
        if per==100:
            color=(0,255,0)
            if dir == 0:
                count += 0.5
                dir= 1
        if per==0:
            color=(0,255,0)
            if dir==1:
                count+=0.5
                dir=0
        print(count)
        # Draw Bar
        cv.rectangle(img, (1100,100), (1175, 650), color, 3)
        cv.rectangle(img, (1100,int(bar)), (1175, 650), color , cv.FILLED)
        cv.putText(img, f'{int(per)} %', (1100, 75), cv.FONT_HERSHEY_PLAIN, 4, color, 4)
        # Draw Curl Count
        cv.rectangle(img, (0,450), (250, 720), (0,255,0), cv.FILLED)
        cv.putText(img, f'{int(count)}', (45, 670), cv.FONT_HERSHEY_PLAIN, 15, (255,0,0), 25)
        cTime= time.time()
        fps= 1/(cTime-pTime)
        cv.putText(img, f'{int(fps)}', (50, 100), cv.FONT_HERSHEY_PLAIN, 5, (255,0,0),5)
        pTime= cTime
    cv.imshow("Image", img)
    cv.waitKey(1)
