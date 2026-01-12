from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Application")
        self.root.geometry("1130x550+230+220")

        #---------------variabels------------
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_ROOMTYPE=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meals=StringVar()
        self.var_noofday=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

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
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING DETAILS",padx=2,font=("times new roman",12,"bold"))
        Labelframeleft.place(x=5,y=50,width=420,height=490)

        # cust_contact
        lblcust_contact=Label(Labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(Labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=20)
        entry_contact.grid(row=0,column=1,sticky=W)

        # fetch Data bottons
        btnfetchdata=Button(Labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",9,"bold"),bg="black",fg="white",width=8)
        btnfetchdata.place(x=347,y=4)

        #check_in_date
        check_in_date=Label(Labelframeleft,text="Check In Date",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(Labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        # check out date
        lbl_check_out_date=Label(Labelframeleft,text="Check Out Date",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_out_date.grid(row=2,column=0,sticky=W)
        txt_check_out_date=ttk.Entry(Labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txt_check_out_date.grid(row=2,column=1)

        # room Types
        label_room_types=Label(Labelframeleft,text="Room Types",font=("arial",12,"bold"),padx=2,pady=6)
        label_room_types.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_room_types=ttk.Combobox(Labelframeleft,textvariable=self.var_ROOMTYPE,font=("arial",12,"bold"),width=27,state="readonly")
        combo_room_types["value"]=ide
        combo_room_types.current(0)
        combo_room_types.grid(row=3,column=1)

        # available room
        lbl_available_room=Label(Labelframeleft,text="Available Room",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_available_room.grid(row=4,column=0,sticky=W)
        #txt_room_availabel=ttk.Entry(Labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        #txt_room_availabel.grid(row=4,column=1)

        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(Labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        # meals
        lbl_meals=Label(Labelframeleft,text="Meals",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_meals.grid(row=5,column=0,sticky=W)
        txt_meals=ttk.Entry(Labelframeleft,textvariable=self.var_meals,font=("arial",13,"bold"),width=29)
        txt_meals.grid(row=5,column=1)

        # no of days
        lbl_no_of_days=Label(Labelframeleft,text="No Of Days",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_no_of_days.grid(row=6,column=0,sticky=W)
        txt_no_of_days=ttk.Entry(Labelframeleft,textvariable=self.var_noofday,font=("arial",13,"bold"),width=29)
        txt_no_of_days.grid(row=6,column=1)

        # paid tax
        lbl_paid_tax=Label(Labelframeleft,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_paid_tax.grid(row=7,column=0,sticky=W)
        txt_paid_tax=ttk.Entry(Labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txt_paid_tax.grid(row=7,column=1)

        # sub total
        lbl_sub_total=Label(Labelframeleft,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_sub_total.grid(row=8,column=0,sticky=W)
        txt_sub_total=ttk.Entry(Labelframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txt_sub_total.grid(row=8,column=1)

        # total cost
        lbl_total_cost=Label(Labelframeleft,text="Total Cost :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_total_cost.grid(row=9,column=0,sticky=W)
        txt_total_cost=ttk.Entry(Labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txt_total_cost.grid(row=9,column=1)

        #-----------------bill bitton----------------------
        btn_bill=Button(Labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="white",width=10)
        btn_bill.grid(row=10,column=0,padx=1,sticky=W)

        #-----------------Buttons------------------
        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=375,width=400,height=40)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="white",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="white",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="white",width=10)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="white",width=10)
        btn_reset.grid(row=0,column=3,padx=1)

        # ------------------Right side image----------------
        img4 = Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\bed.jpeg")
        img4 = img4.resize((400, 250), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbimg=Label(self.root,image=self.photoimg4,bd=0,relief=RIDGE)
        lbimg.place(x=760,y=55,width=400,height=250)

         # ----------------------Tabel Frame and search system----------------------
        Labelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",12,"bold"))
        Labelframe.place(x=425,y=280,width=750,height=260)

        lblSearchr=Label(Labelframe,text="Search By:",font=("arial",12,"bold"),bg="Red",fg="white")
        lblSearchr.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Labelframe,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Labelframe,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btn_search=Button(Labelframe,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="white",width=6)
        btn_search.grid(row=0,column=3,padx=1)

        btn_showall=Button(Labelframe,text="Showall",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="white",width=6)
        btn_showall.grid(row=0,column=4,padx=1)

        #--------------Show Data Tabel-----------------deatal
        detail_tabel = Frame(Labelframe, bd=2, relief=RIDGE)
        detail_tabel.place(x=0, y=50, width=690, height=130)

        scrol_x = ttk.Scrollbar(detail_tabel, orient=HORIZONTAL)
        scrol_y = ttk.Scrollbar(detail_tabel, orient=VERTICAL)

        self.room_table = ttk.Treeview(detail_tabel,
             columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meals",
             "noofdays"),
    xscrollcommand=scrol_x.set,
    yscrollcommand=scrol_y.set)

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x.config(command=self.room_table.xview)
        scrol_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Roomtype")
        self.room_table.heading("roomavailable", text="Room Available")
        self.room_table.heading("meals", text="Meals")
        self.room_table.heading("noofdays", text="No Of days")
        

        self.room_table["show"] = "headings"
        # heading box size in  Data Tabels
        self.room_table.column("checkin",width=100 )
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meals",width=100 )
        self.room_table.column("noofdays",width=100 )
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
    
# --------------add data-----------
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin .get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else: 
            try:
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute(""" INSERT INTO room (`Contact`, `check-In`, check_out, roomtype, roomavailable, meal, noofdays)
                                       VALUES (%s, %s, %s, %s, %s, %s, %s)""", (
                                                                                         self.var_contact.get(),
                                                                                         self.var_checkin.get(),
                                                                                         self.var_checkout.get(),
                                                                                         self.var_ROOMTYPE.get(),
                                                                                         self.var_roomavailable.get(),
                                                                                         self.var_meals.get(),
                                                                                         self.var_noofday.get()
                                                                                     ))
    

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Somthing went wrong:{str(es)}",parent=self.root)



    # ------------------fetch data--------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


# get cursor
    def get_cursor(self, event=""):
      
     try:
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        # Check if row has enough data before accessing indexes
        if row and len(row) >= 7:
            self.var_contact.set(row[0])
            self.var_checkin.set(row[1])
            self.var_checkout.set(row[2])
            self.var_ROOMTYPE.set(row[3])
            self.var_roomavailable.set(row[4])
            self.var_meals.set(row[5])
            self.var_noofday.set(row[6])
     except Exception as e:
        print("Error in get_cursor:", e)

# ------------------update function--------------------
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Plaease enter mobile number",parent=self.root)
        else: 
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("""UPDATE room SET `check-In`=%s, check_out=%s, roomtype=%s, roomavailable=%s, noofdays=%s WHERE Contact=%s""", (
                                                              self.var_checkin.get(),
                                                              self.var_checkout.get(),
                                                              self.var_ROOMTYPE.get(),
                                                              self.var_roomavailable.get(),
                                                              self.var_noofday.get(),
                                                              self.var_contact.get()
                                                          ))

    


            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated succesfully",parent=self.root)



#-----------------delete function----------------
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Application","Do you want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from room where Contact =%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_ROOMTYPE.set("")
        self.var_roomavailable.set("")
        self.var_meals.set("")
        self.var_noofday.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
    
        #--------------all data fetch---------------------

    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDatarframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDatarframe.place(x=440,y=55,width=300,height=200)

                lblname=Label(showDatarframe,text="Name:",font=("arial",12,"bold"))
                lblname.place(x=0,y=0)

                lbl=Label(showDatarframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

# -------------Gender---------------------
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDatarframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDatarframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

# -------------email---------------------
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDatarframe,text="Email:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=60)

                lblemail=Label(showDatarframe,text=row,font=("arial",12,"bold"))
                lblemail.place(x=90,y=60)

# -------------Nationality---------------------
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDatarframe,text="Nationality:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=90)

                lblNationality=Label(showDatarframe,text=row,font=("arial",12,"bold"))
                lblNationality.place(x=90,y=90)

# -------------Adress---------------------
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
                my_cursor=conn.cursor()
                query=("select Adress from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDatarframe,text="Adress:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=120)

                lblAdress=Label(showDatarframe,text=row,font=("arial",12,"bold"))
                lblAdress.place(x=90,y=120)

# -------------------------------search system---------------------------
    def search(self):
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="**********",database="hotel_management")
        my_cursor=conn.cursor()

        my_cursor.execute("SELECT * FROM room WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")

        rows=my_cursor.fetchall()
        if len (rows) !=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
     
     inDate = self.var_checkin.get()
     outDate = self.var_checkout.get()
     inDate = datetime.strptime(inDate, "%d/%m/%Y")
     outDate = datetime.strptime(outDate, "%d/%m/%Y")
     self.var_noofday.set(abs((outDate - inDate).days))


     if (self.var_meals.get()=="Breakfast" and self.var_ROOMTYPE.get()=="Luxary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


     elif  (self.var_meals.get()=="lunch" and self.var_ROOMTYPE.get()=="Singal"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
     elif  (self.var_meals.get()=="lunch" and self.var_ROOMTYPE.get()=="Duplex"):
            q1=float(600)
            q2=float(1100)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

if __name__=="main":
    root=Tk()  
    obj=Roombooking(root)
    root.mainloop(  )