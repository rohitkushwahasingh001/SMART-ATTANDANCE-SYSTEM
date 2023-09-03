from tkinter import*
from tkinter import ttk  #Containes style toolkit
from PIL import Image,ImageTk  # pil-pillow
from tkinter import messagebox
import mysql.connector

class Help:
    def __init__(self,root):
        self.root=root
        # geometry set
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lb1=Label(self.root,text="HELP DESK",font=("time new roman",35,"bold"),bg="royalblue3",fg="black")
        title_lb1.place(x=5,y=0,width=1270,height=45)

        img_top=Image.open("SmartAttendance-main\Images/help_d.jpg")
        img_top=img_top.resize((1270,620),Image.LANCZOS)   #High level img to Low level img
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lb=Label(self.root, image=self.photoimg_top)
        first_lb.place(x=5,y=55,width=1270,height=620)

        help_lb=Label(first_lb,text="Name: rohit kushwaha\n Dhruv",font=("time new roman",15,"bold"),fg="white",bg="black")
        help_lb.place(x=1000,y=65)

        help_lb2=Label(first_lb,text="email:rohit@gmail.com\n dhruv@gamil.com",font=("time new roman",15,"bold"),fg="white",bg="black")
        help_lb2.place(x=1000,y=145)

        help_lb3=Label(first_lb,text="contact:9311428596\n        942310882",font=("time new roman",15,"bold"),fg="white",bg="black")
        help_lb3.place(x=1000,y=225)















if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()