import tkinter as tk
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from tkinter.filedialog import askopenfilename
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 

##############################################+=============================================================

root = tk.Tk()
root.configure(background="cyan")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("AMBULANCE DETECTION SYSTEM")


lbl = tk.Label(root, text="Ambulance Detection System", font=('times', 40,' italic '), height=1, width=30,bg="cyan",fg="black")
lbl.place(x=330, y=5)

frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=280, height=600, bd=5, font=('times', 15, ' italic '),bg="snow")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=5, y=50)

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

def Create_database():
        
    font = cv2.FONT_HERSHEY_SIMPLEX
    Ambulance_Cascade = cv2.CascadeClassifier(r'E:\OMKARS\Ambulance_Detection\classifier\cascade.xml')
    
    fileName = askopenfilename(initialdir='E:/Ambulance_Detection/', title='Select Video File',
                                       filetypes=[("all files", "*.mp4*")])
    #cap = cv2.VideoCapture(r'E:\Ambulance_Detection\Ambulance_Video.mp4')
    cap = cv2.VideoCapture(fileName)

    
    sampleN=0;
    
    while 1:
    
        ret, img = cap.read()
    
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        Ambulance = Ambulance_Cascade.detectMultiScale(gray, scaleFactor = 1.65,minNeighbors = 18) #These values helped me to get better squares around Ambulance
        
                                            

        for (x,y,w,h) in Ambulance:
    
            sampleN=sampleN+1;

            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
            cv2.putText(img,str("Ambulance"),(x,y+h),font,1,(0,0,0),1,cv2.LINE_AA)
    
            cv2.waitKey(100)


        cv2.imshow('Detector',img)
    

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()

    cv2.destroyAllWindows()

#################################################################################################################
def window():
    root.destroy()

button1 = tk.Button(frame_alpr, text="Ambulance Detection", command=Create_database,width=20, height=1, font=('times', 15, ' italic '),bg="yellow4",fg="white")
button1.place(x=10, y=40)


exit = tk.Button(frame_alpr, text="Exit", command=window, width=20, height=1, font=('times', 15, ' italic '),bg="red",fg="white")
exit.place(x=10, y=400)

root.mainloop()
