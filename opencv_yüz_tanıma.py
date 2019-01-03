import os
import numpy as np
import cv2

normal = '\033[0m'
kirmizi= '\033[31m'
yesil= '\033[32m'
sari= '\033[33m'
lacivert= '\033[34m'
mor= '\033[35m'
mavi= '\033[36m'
pmavi = '\033[96m'#p --> parlak
pkirmizi= '\033[91m'
pyesil = '\033[92m'
psari = '\033[93m'
siyah = '\033[90m'
asiyah= '\033[40m'#a --> arkaplan
akirmizi= '\033[41m'
ayesil= '\033[42m'
asari= '\033[43m'
alacivert= '\033[44m'
amor= '\033[45m'
amavi= '\033[46m'
abeyaz= '\033[47m'
apsiyah= '\033[100m'#a --> arkaplan-parlak
apkirmizi= '\033[101m'
apyesil= '\033[102m'
apsari= '\033[103m'
aplacivert= '\033[104m'
apmor= '\033[105m'
apmavi= '\033[106m'
apbeyaz= '\033[107m'
faceCascade = cv2.CascadeClassifier('yuz.xml')#buraya yuz.xml doyasinin konumunu girin
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,

        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        print(pyesil + str(x),pyesil + str(y),pmavi +str(w),pmavi +str(h))
        #print(w,h)                         Mv,Ysl,Krmz,Kalinlik
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,50,50),2)
        #roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # 'ESC' ye basarak cikabilirisiniz.
        break
cap.release()
cv2.destroyAllWindows()
