
import numpy as np
import cv2

img = cv2.imread('messi.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) #matris bilgisi verir
print(img.size) #piksel bilgisi verir
print(img.dtype) #datatype bilgisi verir
b,g,r = cv2.split(img) #gorseli renk kanallarina ayirir
img = cv2.merge((b,g,r)) #birlestirir

ball = img [280:340, 330:390] #topun koordinatlari belirlendi ROI =region of interest
img[243:303, 150:210] = ball #top koordinatlara atandi

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512)) #matris boyutu esitlendi

#dst = cv2.add(img, img2); #birlesitirme islemi
dst = cv2.addWeighted(img, .7, img2, .1, 0); #birlestirilmis gorseldeki baskin gorsel oranini degistirdi

cv2.imshow('image',dst)
cv2.waitKey()
cv2.destroyAllWindows()