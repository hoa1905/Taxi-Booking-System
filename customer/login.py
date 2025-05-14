from tkinter import messagebox
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
from admin import admin_dashboard
from customer import customer_register, customer_dashboard
from driver import driver_dashboard
from libs import Global
from libs.customer_libs import CustomerLibs
from dbms.login_management import login, driver_login, admin_login


class Login(customtkinter.CTk):
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode(
            "dark"
        )  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme(
            "blue"
        )  # Themes: blue (default), dark-blue, green
        self.root.screen_width = root.winfo_screenwidth()
        self.root.screen_height = root.winfo_screenheight()

        # Đặt kích thước và vị trí cửa sổ tại (0, 0)
        self.root.geometry(f"{self.root.screen_width}x{self.root.screen_height}+0+0")

        # đặt kích thước tối thiểu cho cửa sổ giao diện bằng độ phân giải màn hình. Nghĩa là người dùng không thể thu nhỏ cửa sổ nhỏ hơn kích thước này.
        # self.root.minsize(self.root.screen_width, self.root.screen_height)
        # phóng to cửa sổ lên toàn màn hình khi chạy ứng dụng. ( cửa sổ khởi động ở chế độ toàn màn hình ngay từ đầu.)
        # self.root.state("zoomed")

        self.root.title("Đăng nhập hệ thống đặt xe taxi")
        self.root.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )
        self.root.bind("<Escape>", lambda e: root.destroy())

        # -----------------------------Font------------------------------------------
        font1 = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )

        # -----------------------------Top Frame------------------------------------------
        north_frame = customtkinter.CTkFrame(master=root, height=100)
        north_frame.pack(side=TOP, fill=BOTH)

        # -----------------------------Top frame title------------------------------------------
        title_label = customtkinter.CTkLabel(
            master=north_frame,
            text="Đăng nhập hệ thống đặt xe taxi",
            font=("Times New Roman", 35, "bold"),
        )
        title_label.place(x=650, y=40)

        # -----------------------------Top frame Left frame------------------------------------------
        frame1 = customtkinter.CTkFrame(
            master=root, width=400, height=400, corner_radius=20
        )
        frame1.pack(side=LEFT, padx=20)

        # -----------------------------Left frame image------------------------------------------
        # Tạo canvas
        canvas = Canvas(
            frame1,
            width=900,
            height=900,
            bg="#212325",
            borderwidth=0,
            bd=0,
            highlightthickness=0,
        )
        canvas.pack()

        # Mở và resize ảnh
        image_path = "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/Tablet login-rafiki.png"
        cover_image = Image.open(image_path)
        resized_image = cover_image.resize((800, 800))

        # Chuyển đổi ảnh
        photo1 = ImageTk.PhotoImage(resized_image)

        # Hiển thị ảnh bằng Label
        cover_image_label = Label(frame1, image=photo1, bg="#212325")
        cover_image_label.image = photo1  # giữ tham chiếu tránh bị xóa
        cover_image_label.place(x=10, y=0)

        # -----------------------------Signin and create account tab------------------------------------------
        main_frame = customtkinter.CTkFrame(
            self.root, width=750, height=600, corner_radius=20
        )
        main_frame.pack(side=RIGHT, padx=30, pady=30)

        # -----------------------------Image------------------------------------------
        sign_in_image = Image.open(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user.png"
        )
        # Resize ảnh về kích thước mong muốn (rộng 300px, cao 300px)
        sign_in_image = sign_in_image.resize((150, 150))
        photo = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(master=main_frame, image=photo, bg="#2b2b2b")
        sign_in_image_label.image = photo
        sign_in_image_label.place(x=380, y=40)

        # -----------------------------Email label------------------------------------------
        email_lbl = customtkinter.CTkLabel(
            master=main_frame, text="Email: ", font=font1
        )
        email_lbl.place(x=200, y=205)
        # -----------------------------Email Entry Widget------------------------------------------
        email_txt1 = customtkinter.CTkEntry(
            master=main_frame, corner_radius=10, font=font1, width=200
        )
        email_txt1.place(x=330, y=200)

        # -----------------------------Password Label------------------------------------------
        password_lbl = customtkinter.CTkLabel(
            master=main_frame, text="Mật khẩu: ", font=font1
        )
        password_lbl.place(x=200, y=255)

        # -----------------------------Password Entry Widget------------------------------------------
        password_txt1 = customtkinter.CTkEntry(
            master=main_frame, show="*", corner_radius=10, font=font1, width=200
        )
        password_txt1.place(x=330, y=250)

        # -----------------------------Show password checkbox widget------------------------------------------
        i = customtkinter.IntVar()

        def show_password():
            if i.get() == 1:
                password_txt1.configure(show="")
            else:
                password_txt1.configure(show="*")

        password_show = customtkinter.CTkCheckBox(
            master=main_frame,
            text="Hiện mật khẩu",
            variable=i,
            command=show_password,
        )
        password_show.place(x=330, y=290)

        # -----------------------------Customer, admin and driver login function------------------------------------------
        def login_customer():
            login720 = CustomerLibs(
                email=email_txt1.get(), password=password_txt1.get()
            )
            user = login(login720)
            driver_result = driver_login(login720)
            admin_result = admin_login(login720)

            if email_txt1.get() == "" or password_txt1.get() == "":
                messagebox.showerror(
                    "Hệ thống đặt xe taxi",
                    "Vui lòng nhập email và mật khẩu!",
                )

            else:
                if user != None:
                    if user[9] == "Customer":
                        Global.current_user = user
                        self.root.destroy()
                        root = customtkinter.CTk()
                        customer_dashboard.CustomerDashboard(root)
                        root.mainloop()

                elif driver_result != None:
                    Global.current_driver = driver_result
                    self.root.destroy()
                    root = customtkinter.CTk()
                    driver_dashboard.DriverDashboard(root)
                    root.mainloop()

                elif admin_result != None:
                    Global.current_admin = admin_result
                    self.root.destroy()
                    root = customtkinter.CTk()
                    admin_dashboard.AdminDashboard(root)
                    root.mainloop()

                else:
                    msg = messagebox.showerror(
                        "Hệ thống đặt xe taxi",
                        "Email và mật khẩu không đúng!",
                    )

        # -----------------------------Login Button------------------------------------------
        button = customtkinter.CTkButton(
            master=main_frame,
            command=login_customer,
            text="Đăng nhập",
            corner_radius=10,
            text_color="white",
            font=("", 18, "bold"),
            hover_color="black",
        )
        button.place(x=340, y=350)

        signup_lbl = customtkinter.CTkLabel(
            master=main_frame,
            text="Chưa có tài khoản?",
        )
        signup_lbl.place(x=320, y=420)

        # -----------------------------Signup GUI function------------------------------------------
        def signup():
            self.root.destroy()
            root = customtkinter.CTk()
            obj = customer_register.Register(root)
            root.mainloop()

        signup_btn = customtkinter.CTkButton(
            master=main_frame,
            text="Đăng ký ngay",
            width=50,
            height=20,
            hover_color="black",
            command=signup,
        )

        signup_btn.place(x=440, y=420)


if __name__ == "__main__":
    root = customtkinter.CTk()
    Login(root)
    root.mainloop()
