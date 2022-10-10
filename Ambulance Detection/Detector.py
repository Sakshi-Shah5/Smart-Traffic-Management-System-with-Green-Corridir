import numpy as np
import cv2



def DETECT(PATH):
    face_cascade = cv2.CascadeClassifier(r"E:\Ambulance_Detection\classifier\cascade.xml")
    #img = cv2.imread(PATH)
    #img = img.resize(200,200)
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cam = cv2.VideoCapture(PATH)
    while True:    
        ret , img = cam.read()
        faces = face_cascade.detectMultiScale(img,1.01, 7)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('img',img)
        cv2.waitKey(0)
    cv2.destroyAlIWindows()

DETECT(r'E:\Ambulance_Detection\Ambulance_Video.mp4')


def DETECT(PATH):
    face_cascade = cv2.CascadeClassifier(r"E:\Ambulance_Detection\classifier\cascade.xml")
    img = cv2.imread(PATH)
    #img = img.resize(200,200)
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    faces = face_cascade.detectMultiScale(img,1.01, 19)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAlIWindows()


DETECT(r'E:\Ambulance_Detection\p\Yes34.jpg')
DETECT(r'E:\Ambulance_Detection\n\N34.jpg')












from PIL import Image
here = Image.open(r'E:\Ambulance_Detection\p\Yes112.jpg')
here.size


#!/usr/bin/python
from PIL import Image
import os, sys

path = "E:/Ambulance_Detection/p/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()

import vlc
