from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN YOUR DATA",font=("times new roman",35,"bold"),bg="deepskyblue1")
        title_lbl.place(x=5,y=0,width=1270,height=60)

        #image
        img_top=Image.open("SmartAttendance-main\Images/training2.jpeg")
        img_top=img_top.resize((1270,625),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=5,y=65,width=1270,height=625)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",24,"bold"),bg="green",fg="white")
        b1_1.place(x=250,y=385,width=250,height=50)

   
    def train_classifier(self):
        data_dir=("SmartAttendance-main\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')  # gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)  # Remove the "==13" comparison
        ids = np.array(ids)

        # Train classifier using the cv2.face_LBPHFaceRecognizer class
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()