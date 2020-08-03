            


# In[1]:

#impoting all libraries

import cv2 
import numpy as np
import pandas as pd
import datetime
import os
import winsound


# In[2]:

#taking examinees logn details

name="HARIHARAN K"
roll="17TC0259"


# In[3]:

#imoprting face clasiifiers

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)


# In[4]:

#face and cheating detector during exam

cheating=0
cheating2=0
while(True):
    ret,frame=cap.read()
    blurred=cv2.GaussianBlur(frame,(21,21),0)
    weight_frame=cv2.addWeighted(frame,1.75,blurred,-0.5,0)
    
    yuv=cv2.cvtColor(frame,cv2.COLOR_BGR2YUV)
    yuv[:,:,0]=cv2.equalizeHist(yuv[:,:,0])
    
    bgr_frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
    gray = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2GRAY)
    
    clahe = cv2.createCLAHE(clipLimit=40.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)
    
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    
    for(x,y,w,h) in faces:
        roi_gray=gray[x:x+w,y:y+h]
        roi_frame=frame[x:x+w,y:y+h]
        cv2.rectangle(frame,(x,y),(x+w,y+h),color=(255,0,0),thickness=2,lineType=cv2.LINE_AA)
    
    if len(faces)==0:
        cheating=cheating+1
        if cheating==1:
            now=datetime.datetime.now().second
        if cheating>0:
            if (datetime.datetime.now().second-now) > 3:
                #print("CHEATING",datetime.datetime.now().hour,":",datetime.datetime.now().minute,":",datetime.datetime.now().second)
                print(roll+" caught ")
                if cheating >3:
                    print("EXAM TERMINATED AND PAPER CANCELLED!!","\n","NAME-",name," ","ROLL NO-",roll,"CAUGHT CHEATING")
                    break
    
    
    if len(faces)==0:
        cheating2=cheating2+1
        count=0
        if cheating2==1:
            now1=datetime.datetime.now().second
        if cheating2>0:
            
            if (datetime.datetime.now().second-now1)>2:
                count=count+1
            if count>=2:
                print("cheating !! exam terminated,endl=\n")
                break
            if count <2 :
                frequency=2500
                duration=1000
                winsound.Beep(frequency,duration)
                

                   
                
                    
   
        
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()






