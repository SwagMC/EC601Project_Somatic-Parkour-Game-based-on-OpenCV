import numpy as np
import cv2
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('/home/tianyiz/user/601project/c/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while 1:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#Background reduce
	fgmask = fgbg.apply(img)
	cv2.imshow('Reduce',fgmask)
	for (x,y,w,h) in faces:
		print(x,y,w,h)
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
	cv2.imshow('img',img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
