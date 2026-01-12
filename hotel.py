import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_win
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root,login_root):
        self.login_rooy=login_root
        self.root=root
        self.root.title("Hospital Application")
        self.root.geometry("1550x800+0+0")

# ------------------------ 1st Image ------------------
        img1 = Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\hotel1.jpeg")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1550,height=140)

# ------------------LOGO-------------------
  
        img2 = Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\Gemini_Generated_Image_4dlq9t4dlq9t4dlq.png")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=230,height=140)
#------------------------Tittle----------------
        lb1_title=Label(self.root,text="WELCOME TO ABHI HOTEL",font=("times new roman",40,"bold"),bg="darkgoldenrod",fg="white",bd=2,relief=RIDGE)
        lb1_title.place(x=0,y=140,width=1550,height=50)

        #-----------------------Frame-----------------
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

         #---------------- MENU--------------------
        lb1_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="darkgoldenrod",fg="white",bd=4,relief=RIDGE)
        lb1_menu.place(x=0,y=0,width=230)


 #-----------------------Frame-----------------
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,font=("times new roman",14,"bold"),bg="darkgoldenrod",fg="white",bd=0,width=22,cursor="hand1")
        cust_btn.grid(row=0,column=0)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,font=("times new roman",14,"bold"),bg="darkgoldenrod",fg="white",bd=0,width=22,cursor="hand1")
        room_btn.grid(row=1,column=0)

        deatails_btn=Button(btn_frame,text="DETAIL",command=self.details_room,font=("times new roman",14,"bold"),bg="darkgoldenrod",fg="white",bd=0,width=22,cursor="hand1")
        deatails_btn.grid(row=2,column=0)

        report_btn=Button(btn_frame,text="REPORT",font=("times new roman",14,"bold"),bg="darkgoldenrod",fg="white",bd=0,width=22,cursor="hand1")
        report_btn.grid(row=3,column=0)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,font=("times new roman",14,"bold"),bg="darkgoldenrod",fg="white",bd=0,width=22,cursor="hand1")
        logout_btn.grid(row=4,column=0)

        #---------------------Right Side Image-----------------------------
        img3 = Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\premium_photo-1661964071015-d97428970584.jpeg")
        img3 = img3.resize((1310, 590), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lbimg3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbimg3.place(x=225,y=0,width=1310,height=590)

        #-------------down Images--------------------
        img4 = Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\images.jpeg")
        img4 = img4.resize((230, 210), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lbimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbimg1.place(x=0,y=220,width=230,height=170)

        img5 = Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\facadenight.jpg")
        img5 = img5.resize((230, 190), Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lbimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lbimg1.place(x=0,y=380,width=230,height=170)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)


    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()
        self.login_rooy.deiconify()
    

if __name__ =="__main__":
    root=Tk()
    dummy_login_root=Tk()
    dummy_login_root.withdraw()
    obj=HotelManagementSystem(root)
    root.mainloop()