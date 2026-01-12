from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
from tkinter import messagebox  
import  random
import time
import datetime
import _mysql_connector
from hotel import HotelManagementSystem
import mysql.connector
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x1000+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ADMIN\Desktop\hotel_mangement\image\facadenight.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\3135715.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_image1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbl_image1.place(x=730,y=175,width=130,height=100)
        

        get_str=Label(frame,text="Get Started",font=("times new romwn",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new romwn",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.textuser=ttk.Entry(frame,font=("times new romwn",15,"bold"))
        self.textuser.place(x=40,y=180,width=270)


        password=lbl=Label(frame,text="Password",font=("times new romwn",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.textpass=ttk.Entry(frame,font=("times new romwn",15,"bold"))
        self.textpass.place(x=40,y=250,width=270)

        #icon images
        img2=Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\profile-icon-design-free-vector.jpg")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_image2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbl_image2.place(x=650,y=323,width=25,height=25)
        
        #password icon
        img3=Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\profile-icon-design-free-vector.jpg")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_image2=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbl_image2.place(x=650,y=393,width=25,height=25)


# login button
        loginbtn=Button(frame,text="Login",font=("times new romwn",15,"bold"),command=self.login,bd=3,relief=RIDGE,fg="black",bg="white",activebackground="white",activeforeground="black")
        loginbtn.place(x=110,y=300,width=120,height=35)


        # register button
        regbtn=Button(frame,text="New User Register",font=("times new romwn",10,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="black")
        regbtn.place(x=15,y=350,width=160)

        #forgot password button
        forgetbtn=Button(frame,text="Forget Password",font=("times new romwn",10,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="black")
        forgetbtn.place(x=10,y=370,width=160)

    def login(self):
     if self.textuser.get() == "" or self.textpass.get() == "":
        messagebox.showerror("Error", "All fields are required")
        return  # empty field to skip rest

     elif self.textuser.get() == "abhi" and self.textpass.get() == "12345":
      #messagebox.showinfo("Success", "Welcome to Home Page")
      self.open_hotel_management()

      return  # admin bypass

     else:
        row = None  
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                username="root",
                password="Prince@123",
                database="hotel_management"
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT * FROM register WHERE email=%s AND password=%s",
                (
                    self.textuser.get(),  
                    self.textpass.get()   
                )
            )
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                open_main = messagebox.askyesno("Yes/No", "Access only admin")
                if open_main:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    return

        except Exception as e:
            messagebox.showerror("Database Error", f"{e}")

        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.commit()
                conn.close()


    def open_hotel_management(self):
        
        self.root.withdraw()
        
        
        self.new_window = Toplevel(self.root)
        self.app = HotelManagementSystem(self.new_window, login_root=self.root)




if __name__== "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()