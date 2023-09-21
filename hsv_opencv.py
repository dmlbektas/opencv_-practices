#hsv hue-renk value-parlaklik saturation-doygunluk

import cv2
import numpy as np

def nothing(x):
    pass
cap = cv2.VideoCapture(0);
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,nothing) # LOWER HUE
cv2.createTrackbar("LS","Tracking",0,255,nothing) # LOWER SAT
cv2.createTrackbar("LV","Tracking",0,255,nothing) # LOWER VAL
cv2.createTrackbar("UH","Tracking",255,255,nothing) # UPPER HUE
cv2.createTrackbar("US","Tracking",255,255,nothing) # UPPER SAT
cv2.createTrackbar("UV","Tracking",255,255,nothing) # UPPER VAL

while True:
    frame = cv2.imread('smarties.png')
    #ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #asagidaki hsv degerleri yesil toplari ayirt eder
    l_h = cv2.getTrackbarPos("LH" , "Tracking") #50
    l_s = cv2.getTrackbarPos("LS", "Tracking") #57
    l_v = cv2.getTrackbarPos("LV", "Tracking") #75

    u_h = cv2.getTrackbarPos("UH", "Tracking") #88
    u_s = cv2.getTrackbarPos("US", "Tracking") #255
    u_v = cv2.getTrackbarPos("UV", "Tracking") #255
    l_b = np.array([l_h,l_s,l_v]) #lower blue
    u_b = np.array([u_h,u_s,u_v]) # upper blue

    mask = cv2.inRange(hsv,l_b,u_b) # mavi renkleri maskeleme islemi

    res = cv2.bitwise_and(frame,frame,mask =mask) #sonuc

    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()