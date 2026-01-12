from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem 

# Main Login Window

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Login Portal")
        self.root.geometry("1550x1000+0+0")

        # ==================== Back  ground Image ====================
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

        # ==================== Other Buttons ====================
        regbtn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activebackground="black", activeforeground="white")
        regbtn.place(x=15, y=420, width=160)

        forgetbtn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activebackground="black", activeforeground="white")
        forgetbtn.place(x=10, y=450, width=160)


    def login(self):
        """Admin aur User dono roles ke liye login logic handle karta hai."""
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
            if username == "abhi" and password == "12345":
                messagebox.showinfo("Success", "Welcome user!", parent=self.root)
                self.open_hotel_page()
            else:
                messagebox.showerror("Error", "Invalid Admin credentials.", parent=self.root)
            
            

    def login_user_from_db(self, email, password):
        """Database se user credentials validate karta hai."""
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Prince@123", 
                database="hotel_management"
            )
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s AND password=%s"
            my_cursor.execute(query, (email, password))
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid username or password.", parent=self.root)
            else:
                messagebox.showinfo("Success", f"Welcome, {row[1]}!", parent=self.root) 
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


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
