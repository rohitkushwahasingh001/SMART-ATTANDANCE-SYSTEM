from tkinter import*
from tkinter import ttk  #Containes style toolkit
from PIL import Image,ImageTk  # pil-pillow
from tkinter import messagebox
import mysql.connector

class Developer:
    def __init__(self,root):
        self.root=root
        # geometry set
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lb1=Label(self.root,text="DEVELOPER",font=("time new roman",35,"bold"),bg="white",fg="dark blue")
        title_lb1.place(x=5,y=0,width=1270,height=45)

        img_top=Image.open("SmartAttendance-main\Images/devv.jpg")
        img_top=img_top.resize((1270,740),Image.LANCZOS)   #High level img to Low level img
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lb=Label(self.root, image=self.photoimg_top)
        first_lb.place(x=5,y=55,width=1270,height=620)


        # Frame
        main_frame=Frame(first_lb,bd=2,bg="white")
        main_frame.place(x=1000,y=55,width=250,height=404)

        img_l=Image.open("SmartAttendance-main\Images/developergif.gif")
        img_l=img_l.resize((200,200),Image.LANCZOS)   #High level img to Low level img
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        first_lb=Label(main_frame, image=self.photoimg_l)
        first_lb.place(x=300,y=0,width=200,height=200)

        # Developer Info
        dev_lb=Label(main_frame,text="Rohit kushwha\nRoll no: 201130050049 \n BTECH(CSAI-2ndyear)",font=("time new roman",15,"bold"),bg="white",fg="#142552")
        dev_lb.place(x=10,y=45)

        dev_lb=Label(main_frame,text="Dhruv\nRoll no: 201130050044 \n BTECH(CSAI-2ndyear) ",font=("time new roman",15,"bold"),bg="white",fg="#142552")
        dev_lb.place(x=10,y=150)

    






















if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()