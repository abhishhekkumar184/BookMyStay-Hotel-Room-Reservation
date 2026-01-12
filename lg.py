from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem 


# New User Registration Window

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register New User")
        self.root.geometry("1600x900+0+0")
        self.root.grab_set() 

        # ================== Variables ==================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ================== Background Image ==================
        try:
            self.bg = ImageTk.PhotoImage(file=r"C:\Users\ADMIN\Desktop\hotel_mangement\image\background.jpg") # Ek background image ka path dein
            bg_lbl = Label(self.root, image=self.bg)
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            self.root.config(bg="white")
        
        # ================== Main Frame ==================
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # ================== Labels and Entries ==================
        # ---------- Row 1
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname.place(x=370, y=100)
        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        lname_entry.place(x=370, y=130, width=250)

        # ---------- Row 2
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)
        contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        contact_entry.place(x=50, y=200, width=250)

        email = Label(frame, text="Email (Username)", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)
        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        email_entry.place(x=370, y=200, width=250)

        # ---------- Row 3
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15), state="readonly")
        self.combo_security_Q['values'] = ("Select", "Your Birth Place", "Your Pet Name", "Your Best Friend Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50, y=270, width=250)
        
        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)
        
        # ---------- Row 4
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)
        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        self.txt_confirm_pswd.place(x=370, y=340, width=250)
        
        # ================== Check Button & Buttons ==================
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 12), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        register_btn = Button(frame, text="Register Now", command=self.register_data, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="green")
        register_btn.place(x=50, y=420, width=200, height=40)
        
        login_btn = Button(frame, text="Back to Login", command=self.root.destroy, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="blue")
        login_btn.place(x=370, y=420, width=200, height=40)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", user="root", password="**********", database="hotel_management")
                my_cursor = conn.cursor()
                query = ("SELECT * FROM register WHERE email=%s")
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
                else:
                    my_cursor.execute("INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                        self.var_fname.get(), self.var_lname.get(), self.var_contact.get(),
                        self.var_email.get(), self.var_securityQ.get(), self.var_securityA.get(),
                        self.var_pass.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registered Successfully!", parent=self.root)
                    self.root.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


# Forgot Password Window

class ForgotPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.geometry("340x450+610+170")
        self.root.grab_set()

        frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        frame.place(x=0,y=0,relwidth=1,relheight=1)

        title = Label(frame, text="FORGOT PASSWORD", font=("times new roman",20,"bold"),fg="red",bg="white")
        title.pack(side=TOP,fill=X,pady=10)

        email = Label(frame, text="Email (Username)", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=20, y=80)
        self.txt_email = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_email.place(x=20, y=110, width=250)
        
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=20, y=150)
        self.combo_security_Q = ttk.Combobox(frame, font=("times new roman", 15), state="readonly")
        self.combo_security_Q['values'] = ("Select", "Your Birth Place", "Your Pet Name", "Your Best Friend Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=20, y=180, width=250)
        
        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=20, y=220)
        self.txt_security = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_security.place(x=20, y=250, width=250)

        new_password = Label(frame, text="New Password", font=("times new roman", 15, "bold"), bg="white")
        new_password.place(x=20, y=290)
        self.txt_new_pass = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txt_new_pass.place(x=20, y=320, width=250)
        
        reset_btn = Button(frame, text="Reset Password", command=self.reset_password, font=("times new roman", 15, "bold"), fg="white", bg="green")
        reset_btn.place(x=80, y=370, width=180)

    def reset_password(self):
        if self.combo_security_Q.get() == "Select" or self.txt_security.get() == "" or self.txt_email.get() == "":
             messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", user="root", password="**********", database="hotel_management")
                my_cursor = conn.cursor()
                query = ("SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s")
                value = (self.txt_email.get(), self.combo_security_Q.get(), self.txt_security.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter correct information", parent=self.root)
                else:
                    query = ("UPDATE register SET password=%s WHERE email=%s")
                    value = (self.txt_new_pass.get(), self.txt_email.get())
                    my_cursor.execute(query, value)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Your password has been reset successfully!", parent=self.root)
                    self.root.destroy()
            except Exception as es:
                 messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


# Main Login Window

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Login Portal")
        self.root.geometry("1550x1000+0+0")

        # ==================== Background Image ====================
        try:
            self.bg = ImageTk.PhotoImage(file=r"C:\Users\ADMIN\Desktop\hotel_mangement\image\facadenight.jpg")
            lbl_bg = Label(self.root, image=self.bg)
            lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Background image load karne mein error: {e}")
            self.root.config(bg="gray")

        # ==================== Login Frame ====================
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=500)

        # ==================== Login Icon ====================
        try:
            img1 = Image.open(r"C:\Users\ADMIN\Desktop\hotel_mangement\image\3135715.png") 
            img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
            self.photoimage1 = ImageTk.PhotoImage(img1)
            lbl_image1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
            lbl_image1.place(x=730, y=175, width=100, height=100)
        except Exception as e:
            print(f"Login icon load karne mein error: {e}")
        
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # ==================== Role Selection ====================
        role_label = Label(frame, text="Login As", font=("times new roman", 15, "bold"), fg="white", bg="black")
        role_label.place(x=40, y=155)

        self.role_var = StringVar()
        self.combo_role = ttk.Combobox(frame, textvariable=self.role_var, font=("times new roman", 13), state="readonly")
        self.combo_role['values'] = ("Select Role", "Admin", "User")
        self.combo_role.current(0)
        self.combo_role.place(x=40, y=180, width=270)

        # ==================== Username ====================
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=40, y=225)

        self.textuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.textuser.place(x=40, y=250, width=270)

        # ==================== Password ====================
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=40, y=295)

        self.textpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.textpass.place(x=40, y=320, width=270)
        
        # ==================== Login Button ====================
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activebackground="red", activeforeground="white")
        loginbtn.place(x=110, y=370, width=120, height=35)

        # ==================== Other Buttons (UPDATED COMMANDS) ====================
        regbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activebackground="black", activeforeground="white")
        regbtn.place(x=15, y=420, width=160)

        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activebackground="black", activeforeground="white")
        forgetbtn.place(x=10, y=450, width=160)


    def login(self):
        role = self.role_var.get()
        username = self.textuser.get()
        password = self.textpass.get()

        if role == "Select Role":
            messagebox.showerror("Error", "Please select a login role.", parent=self.root)
            return
        
        if not username or not password:
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
            return

        if role == "Admin":
            if username == "admin" and password == "12345":
                messagebox.showinfo("Success", "Welcome Admin!", parent=self.root)
                self.open_hotel_page()
            else:
                messagebox.showerror("Error", "Invalid Admin credentials.", parent=self.root)
        
        elif role == "User":
            
            self.login_user_from_db(username, password)
            
    def login_user_from_db(self, email, password):
        """Database se user credentials validate karta hai."""
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="**********", 
                database="hotel_management"
            )
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s AND password=%s"
            my_cursor.execute(query, (email, password))
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid username or password.", parent=self.root)
            else:
                messagebox.showinfo("Success", f"Welcome, {row[0]}!", parent=self.root) 
                self.open_hotel_page()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {e}", parent=self.root)
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()

    def open_hotel_page(self):
        """Admin aur Users ke liye main Hotel Management System kholta hai."""
        self.root.withdraw() 
        self.new_window = Toplevel(self.root)
        self.app = HotelManagementSystem(self.new_window, login_root=self.root)
    
    # ==================== Functions to open new windows ====================
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def forgot_password_window(self):
        self.new_window = Toplevel(self.root)
        self.app = ForgotPassword(self.new_window)


if __name__ == "__main__":
   
    try:
        conn = mysql.connector.connect(host="127.0.0.1", user="root", password="**********", database="hotel_management")
        my_cursor = conn.cursor()
        
        my_cursor.execute("""
            CREATE TABLE IF NOT EXISTS register (
                fname VARCHAR(255),
                lname VARCHAR(255),
                contact VARCHAR(255),
                email VARCHAR(255) PRIMARY KEY,
                securityQ VARCHAR(255),
                securityA VARCHAR(255),
                password VARCHAR(255)
            )
        """)
        conn.close()
    except Exception as es:
        print(f"Database connection/setup error: {es}")

    root = Tk()
    app = Login_Window(root)
    root.mainloop()
