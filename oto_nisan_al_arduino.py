import time
import RPi.GPIO as GPIO
import cv2
import numpy as np
import os 
import pyserial
import serial
 
GPIO.cleanup()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

serialport = serial.Serial('ttyUSB0', 9600)


#serialport.write(bytes(deger, 'utf-8'))
# Bağlantı kapa.
#serialport.flush()


#iniciate id counter
id = 0

x1=320#640/2
y1=240#480/2
xmax=350
xmin=290
ymax=270
ymin=210

names = ['Selda','Yahya', 'Mete Eker','Gunes','yahya','Yahya DOGAN','Ege','Mehmet','Mehmet'] 


# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)


GPIO.setmode(GPIO.BOARD)

xx= 12
yonx=16
zz=18
yonz=22

GPIO.setup(xx, GPIO.OUT)
GPIO.setup(zz, GPIO.OUT)

GPIO.setup(yonx, GPIO.OUT)
GPIO.setup(yonz, GPIO.OUT)

def hrkt(pin,yon,yonp,zaman):#step pin,yon,yon pin,zaman
        
        if(zaman==0):
            GPIO.output(yonp,GPIO.LOW)
            GPIO.output(pin,GPIO.LOW)
            print(str(yonp),"kapatildi")
            print(str(pin),"kapatildi")
        else:
            if(yon==1):
                GPIO.output(yonp,GPIO.HIGH)
            else:
                GPIO.output(yonp,GPIO.LOW)

            GPIO.output(pin,GPIO.HIGH)
            time.sleep(zaman)
            GPIO.output(pin,GPIO.LOW)
            time.sleep(zaman)
def ates():
    print("ates")






zmn=0.001

while True:

    ret, img =cam.read()
    img = cv2.flip(img, -1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        nisangah="+"

        cv2.putText(img,str(nisangah) , (x1-20,y1-20), font, 3, (0,255,0), 5)

        if(id == 2 or id==3 ):
            b=0
            g=0
            r=255
            w2=int(w/2.2)
            h2=int(h/4)
            dot="."

            cv2.putText(img,str(dot) , (x+w2,y+h2), font, 1, (b,g,r), 5)
            print("Suclu",int(x+w2-3),int(y+h2-2))
            xp=x+w2
            yp=y+h2

        if(id == 1 or id==0 or id==4 or id==5 or id==6 ):
            print("Suclu Degil")
            b=0
            g=255
            r=0
            xp=0
            yp=0

        if(id==0):
            print (id)
            hrkt(xx,0,yonx,0) 
            hrkt(zz,0,yonz,0)     

            GPIO.output(xx ,GPIO.LOW)   
            GPIO.output(yonx ,GPIO.LOW)    
            GPIO.output(zz ,GPIO.LOW)   
            GPIO.output(yonz ,GPIO.LOW)

            print("Dur ")


        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        if(id=="unknown"):
            b=0
            g=255
            r=255
            xp=0
            yp=0

        cv2.putText(img, id, (x+5,y-5), font, 1, (b,g,r), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (b,g,r), 1)       
        cv2.rectangle(img, (x,y), (x+w,y+h), (b,g,r), 2)

        if(xp<360 and xp>280) :
            if(yp>200 and yp< 280):
                serialport.write(bytes(0, 'utf-8'))               
                print("Dur ")

        if(xp<xmin and yp>200 and yp< 280):
            serialport.write(bytes(1, 'utf-8'))#sag
            print("Sag'a git ")
            
        if(xp>xmax and yp>200 and yp< 280):
            serialport.write(bytes(2, 'utf-8'))#sol
            print("Sol'a git ")

        if(yp>ymax and xp<360 and xp>280):
            serialport.write(bytes(3, 'utf-8'))#ust
            print("Ust'e git ")

        if(yp<ymin and xp<360 and xp>280 ):
            serialport.write(bytes(4, 'utf-8'))#alt
            print("Alt'a git ")

        if(xp<xmin and yp>ymax):
            serialport.write(bytes(5, 'utf-8'))#sag ust
            print("Sag uste git ")
            
        if(xp<xmin and yp<ymin):
            serialport.write(bytes(6, 'utf-8'))#sag alt
            print("Sag asagiya git ")
            

        if(xp>xmax and yp>ymax):
            serialport.write(bytes(7, 'utf-8'))#sol ust
            print("Sol uste git ")
            
        if(xp>xmax and yp<ymin):
            serialport.write(bytes(8, 'utf-8'))#sol alt
            print("Sol alta git ")
        
            
        print(xp,yp)
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

        time.sleep(0.005)

