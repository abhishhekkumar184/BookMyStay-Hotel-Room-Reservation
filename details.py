from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Application")
        self.root.geometry("1130x550+230+220")

        #------------------------Tittle----------------
        lb1_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",18,"bold"),bg="darkgoldenrod",fg="white",bd=2,relief=RIDGE)
        lb1_title.place(x=0,y=00,width=1200,height=50)


        # ------------------LOGO-------------------
        img2 = Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\Gemini_Generated_Image_4dlq9t4dlq9t4dlq.png")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbimg.place(x=5,y=2,width=100,height=40)

        #----------------- Label frame--------------
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",padx=2,font=("times new roman",12,"bold"))
        Labelframeleft.place(x=5,y=50,width=520,height=380)
        

        

        # floor
        lbl_floor=Label(Labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(Labelframeleft,textvariable=self.var_floor,font=("arial",13,"bold"),width=20)
        entry_floor.grid(row=0,column=1,sticky=W)

        # roroomno
        lbl_roomno=Label(Labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0,sticky=W)

        self.var_RoomNo=StringVar()
        entry_roomno=ttk.Entry(Labelframeleft,textvariable=self.var_RoomNo,font=("arial",13,"bold"),width=20)
        entry_roomno.grid(row=1,column=1,sticky=W)

        # Room Type
        lbl_roomtype=Label(Labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        entry_roomtype=ttk.Entry(Labelframeleft,textvariable=self.var_RoomType,font=("arial",13,"bold"),width=20)
        entry_roomtype.grid(row=2,column=1,sticky=W)

        # floor
        lbl_floor=Label(Labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        entry_floor=ttk.Entry(Labelframeleft,font=("arial",13,"bold"),width=20)
        entry_floor.grid(row=0,column=1,sticky=W)

        #-----------------Buttons------------------
        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=400,height=40)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="white",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="white",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="white",width=10)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),bg="black",fg="white",width=10)
        btn_reset.grid(row=0,column=3,padx=1)

        # ----------------------Tabel Frame and search system----------------------
        Labelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show room details",padx=2,font=("times new roman",12,"bold"))
        Labelframe.place(x=600,y=55,width=600,height=350)

        scrol_x = ttk.Scrollbar(Labelframe, orient=HORIZONTAL)
        scrol_y = ttk.Scrollbar(Labelframe, orient=VERTICAL)

        self.room_table = ttk.Treeview(Labelframe,
             columns=("floor","roomno","roomtype"),
    xscrollcommand=scrol_x.set,
    yscrollcommand=scrol_y.set)

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x.config(command=self.room_table.xview)
        scrol_y.config(command=self.room_table.yview)
        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")
        

        self.room_table["show"] = "headings"
        # heading box size in  Data Tabels
        self.room_table.column("floor",width=100 )
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # --------------add data-----------
    def add_data(self):
     if self.var_floor.get()=="" or self.var_RoomNo.get()=="" or self.var_RoomType.get()=="":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
     else: 
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                username="root",
                password="**********",
                database="hotel_management"
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "INSERT INTO details VALUES (%s, %s, %s)",
                (
                    self.var_floor.get(),
                    self.var_RoomNo.get(),
                    self.var_RoomType.get()
                )
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "New Room Added Successfully", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    
    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # get cursor
    def get_cursor(self, event=""):
      
     
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_RoomNo.set(row[1]),
        self.var_RoomType.set(row[2]) 

    # ------------------update function--------------------
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Plaease enter floor number",parent=self.root)
        else: 
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("""UPDATE  details set  `Floor`=%s, RoomType=%s WHERE RoomNo=%s""", (
                                                              self.var_floor.get(),
                                                              self.var_RoomType.get(),
                                                              self.var_RoomNo.get()
                                                              
                                                          ))
            

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Room details has been updated succesfully",parent=self.root)           

 
#-----------------delete function----------------
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Application","Do you want delete this room details",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo =%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        self.var_floor.set(""),
        self.var_RoomNo.set(""),
        self.var_RoomType.set("") 


if __name__=="main":
    root=Tk()  
    obj=DetailsRoom(root)
    root.mainloop(  )