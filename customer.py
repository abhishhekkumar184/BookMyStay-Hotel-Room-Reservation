from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Application")
        self.root.geometry("1130x550+230+220")


        #-------------variables------------------
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cus_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_adress=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

        #------------------------Tittle----------------
        lb1_title=Label(self.root,text="ADD CUSTOMER DETAIL",font=("times new roman",18,"bold"),bg="darkgoldenrod",fg="white",bd=2,relief=RIDGE)
        lb1_title.place(x=0,y=00,width=1200,height=50)


        # ------------------LOGO-------------------


        img2 = Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\Gemini_Generated_Image_4dlq9t4dlq9t4dlq.png")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbimg.place(x=5,y=2,width=100,height=40)


        #----------------- Label frame--------------
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Deatail",padx=2,font=("times new roman",12,"bold"))
        Labelframeleft.place(x=5,y=50,width=400,height=490)


        #-----------------label and entries-------------------------

        # cust_ref
        lblcust_ref=Label(Labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lblcust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(Labelframeleft,textvariable=self.var_ref,font=("arial",13,"bold"),width=29,state="readonly")
        entry_ref.grid(row=0,column=1)

        #cust name
        cname=Label(Labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcnane=ttk.Entry(Labelframeleft,textvariable=self.var_cus_name,font=("arial",13,"bold"),width=29)
        txtcnane.grid(row=1,column=1)

        # mother name
        lblmname=Label(Labelframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmnane=ttk.Entry(Labelframeleft,textvariable=self.var_mother,font=("arial",13,"bold"),width=29)
        txtmnane.grid(row=2,column=1)

        # gender combobox
        label_gender=Label(Labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(Labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        # postcode
        lblpostcode=Label(Labelframeleft,text="Post Code:",font=("arial",12,"bold"),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)
        txtpostcode=ttk.Entry(Labelframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width=29)
        txtpostcode.grid(row=4,column=1)

        # mobile number
        lblmobile=Label(Labelframeleft,text="Mobile Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)
        txtmobile=ttk.Entry(Labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtmobile.grid(row=5,column=1)

        # email
        lblemail=Label(Labelframeleft,text="Email Id:",font=("arial",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)
        txtemail=ttk.Entry(Labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtemail.grid(row=6,column=1)


        # nationality
        lblnationality=Label(Labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lblnationality.grid(row=7,column=0,sticky=W)
        combo_nationality=ttk.Combobox(Labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nationality["value"]=("China","Indian","Nepal","Bhutan","Banglasdeh","ShriLanka","Other")
        combo_nationality.current(1)
        combo_nationality.grid(row=7,column=1)
        
        # idproof type cobobox
        lblIdproof=Label(Labelframeleft,text="Id proof:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdproof.grid(row=8,column=0,sticky=W)
        combo_Idproof=ttk.Combobox(Labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Idproof["value"]=("AdharCard","Driving Licence","Pan Card","Passport","Voter ID","Ration Card","Other")
        combo_Idproof.current(0)
        combo_Idproof.grid(row=8,column=1)

        # id number
        lblIdNumber=Label(Labelframeleft,text="Id Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(Labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        # adress
        lbladres=Label(Labelframeleft,text="Adress:",font=("arial",12,"bold"),padx=2,pady=6)
        lbladres.grid(row=10,column=0,sticky=W)
        txtadress=ttk.Entry(Labelframeleft,textvariable=self.var_adress,font=("arial",13,"bold"),width=29)
        txtadress.grid(row=10,column=1)

        #-----------------Buttons------------------
        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=380,width=400,height=40)

        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="darkgoldenrod",fg="black",width=10)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="darkgoldenrod",fg="black",width=10)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="darkgoldenrod",fg="black",width=10)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="darkgoldenrod",fg="black",width=10)
        btn_reset.grid(row=0,column=3,padx=1)

        # ----------------------Tabel Frame and search system----------------------
        Labelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",12,"bold"))
        Labelframe.place(x=425,y=50,width=750,height=400)


        lblSearchr=Label(Labelframe,text="Search By:",font=("arial",12,"bold"),bg="black",fg="white")
        lblSearchr.grid(row=0,column=0,sticky=W,padx=2)


        self.search_var=StringVar()
        combo_search=ttk.Combobox(Labelframe,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref","ID Proof","Name")
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
        detail_tabel.place(x=0, y=50, width=690, height=320)

        scrol_x = ttk.Scrollbar(detail_tabel, orient=HORIZONTAL)
        scrol_y = ttk.Scrollbar(detail_tabel, orient=VERTICAL)

        self.Cust_details_table = ttk.Treeview(detail_tabel,
             columns=("ref", "name", "mother", "gender", "post", "mobile",
             "email", "nationality", "id_proof", "id_number", "address"),
    xscrollcommand=scrol_x.set,
    yscrollcommand=scrol_y.set)

        scrol_x.pack(side=BOTTOM, fill=X)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x.config(command=self.Cust_details_table.xview)
        scrol_y.config(command=self.Cust_details_table.yview)

        self.Cust_details_table.heading("ref", text="Ref No")
        self.Cust_details_table.heading("name", text="Name")
        self.Cust_details_table.heading("mother", text="Mother")
        self.Cust_details_table.heading("gender", text="Gender")
        self.Cust_details_table.heading("post", text="Post")
        self.Cust_details_table.heading("mobile", text="Mobile")
        self.Cust_details_table.heading("email", text="Email")
        self.Cust_details_table.heading("nationality", text="Nationality")
        self.Cust_details_table.heading("id_proof", text="ID Proof")
        self.Cust_details_table.heading("address", text="Address")

        self.Cust_details_table["show"] = "headings"
        # heading box size in  Data Tabels
        self.Cust_details_table.column("ref", width=100)
        self.Cust_details_table.column("name", width=100)
        self.Cust_details_table.column("mother",width=100 )
        self.Cust_details_table.column("gender",width=100)
        self.Cust_details_table.column("post", width=100)
        self.Cust_details_table.column("mobile", width=100)
        self.Cust_details_table.column("email", width=100)
        self.Cust_details_table.column("nationality",width=100 )
        self.Cust_details_table.column("id_number", width=100)
        self.Cust_details_table.column("address",width=100)


        self.Cust_details_table.pack(fill=BOTH, expand=1)
        self.Cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else: 
            try:
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Prince@123",database="hotel_management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into  customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                  self.var_ref.get(),
                                                  self.var_cus_name.get(),
                                                  self.var_mother.get(),
                                                  self.var_gender.get(),
                                                  self.var_post.get(),
                                                  self.var_mobile.get(),
                                                  self.var_email.get(),
                                                  self.var_nationality.get(),
                                                  self.var_id_proof.get(),
                                                  self.var_id_number.get(),
                                                  self.var_adress.get() ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Somthing went wrong:{str(es)}",parent=self.root)
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Prince@123",database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    def get_cursor(self, event=""):
      cursor_row = self.Cust_details_table.focus()
      content = self.Cust_details_table.item(cursor_row)
      row = content["values"]

      self.var_ref.set(row[0])
      self.var_cus_name.set(row[1])
      self.var_mother.set(row[2])
      self.var_gender.set(row[3])
      self.var_post.set(row[4])
      self.var_mobile.set(row[5])
      self.var_email.set(row[6])
      self.var_nationality.set(row[7])
      self.var_id_proof.set(row[8])
      self.var_id_number.set(row[9])
      self.var_adress.set(row[10])

    
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Plaease enter mobile number",parent=self.root)
        else: 
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Prince@123",database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute(
    "UPDATE customer SET Name=%s, Mother=%s, Gender=%s, Post=%s, Mobile=%s, Email=%s, Nationality=%s, Idnumber=%s, Adress=%s WHERE Ref=%s",
    (
        self.var_cus_name.get(),
        self.var_mother.get(),
        self.var_gender.get(),
        self.var_post.get(),
        self.var_mobile.get(),
        self.var_email.get(),
        self.var_nationality.get(),
        self.var_id_number.get(),
        self.var_adress.get(),
        self.var_ref.get()
    )
)

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated succesfully",parent=self.root       
                                
                                                                                                                                        )

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Application","Do you want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Prince@123",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

        
    def reset(self):
      #self.var_ref.set(""),
      self.var_cus_name.set(""),
      self.var_mother.set(""),
      #self.var_gender.set(""),
      self.var_post.set(""),
      self.var_mobile.set(""),
      self.var_email.set(""),
    #  self.var_nationality.set(""),
     #self.var_id_proof.set(""),
      self.var_id_number.set(""),
      self.var_adress.set("")
      x=random.randint(1000,9999)
      self.var_ref.set(str(x))


    def search(self):
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Prince@123",database="hotel_management")
        my_cursor=conn.cursor()

        my_cursor.execute("SELECT * FROM customer WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")

        rows=my_cursor.fetchall()
        if len (rows) !=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
            
if __name__=="main":
    root=Tk()  
    obj=Cust_win(root)
    root.mainloop(  )
