from libs.customer_libs import CustomerLibs
from dbms.customer_management import insert_record
from tkinter import *
import customtkinter
from tkcalendar import *
from PIL import ImageTk, Image
from customer import login
from tkinter import messagebox, ttk


class Register(customtkinter.CTk):
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

        self.root.title("Đăng ký tài khoản khách hàng")
        self.root.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )

        # ===========================All Variables===========
        self.name_txt = StringVar()
        self.mobile_txt = StringVar()
        self.gender_txt = StringVar()
        self.email_txt = StringVar()
        self.address_txt = StringVar()
        self.password_txt = StringVar()
        self.credit_txt = StringVar()

        def signin():
            self.root.destroy()
            root = customtkinter.CTk()
            obj1 = login.Login(root)
            root.mainloop()

        font = customtkinter.CTkFont(family="Times New Roman", size=25, weight="normal")
        font1 = customtkinter.CTkFont(
            family="Times New Roman",
            size=25,
            weight="normal",
        )

        north_frame = customtkinter.CTkFrame(master=root, height=100, corner_radius=0)
        north_frame.pack(side=TOP, fill=BOTH)

        title_lbl = customtkinter.CTkLabel(
            master=north_frame,
            text="Đăng ký tài khoản khách hàng",
            font=("Cambria", 26, "bold"),
        )
        title_lbl.place(x=500, y=25)

        # -----------------------------Top frame Right frame------------------------------------------
        right_frame = customtkinter.CTkFrame(master=root)
        right_frame.pack(side=LEFT, fill=BOTH)

        canva = Canvas(right_frame, width=900, height=900, bd=0, highlightthickness=0)
        canva.pack()

        cover_image = Image.open(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/taxi.png"
        )
        photo1 = ImageTk.PhotoImage(cover_image)
        cover_image_label = Label(right_frame, image=photo1, bg="#212325")
        cover_image_label.image = photo1
        cover_image_label.place(x=0, y=0)

        name_lbl = Label(root, text="Tên: ", bg="#212325", fg="white", font=font)
        name_lbl.place(x=630, y=250)

        name_txt = customtkinter.CTkEntry(
            master=root, fg_color="white", text_color="black", font=font1, width=250
        )
        name_txt.configure(textvariable=self.name_txt)
        name_txt.place(x=650, y=200)

        dob_lbl = Label(root, text="Ngày sinh: ", bg="#212325", fg="white", font=font)
        dob_lbl.place(x=630, y=320)

        style = ttk.Style()
        style.configure(
            "my.DateEntry",
            fieldbackground="#2a2d2e",
            background="red",
            foreground="black",
            arrowcolor="red",
        )
        dob_txt = DateEntry(
            root,
            font=font1,
            selectmode="day",
            style="my.DateEntry",
            background="green",
            bordercolor="red",
            selectbackground="green",
            width=17,
            date_pattern="yyyy-mm-dd",
        )

        dob_txt.place(x=820, y=320)

        gender_lbl = Label(
            root, text="Giới tính: ", bg="#212325", fg="white", font=font
        )
        gender_lbl.place(x=1350, y=250)

        gender_txt = customtkinter.CTkOptionMenu(
            master=root,
            fg_color="white",
            variable=self.gender_txt,
            text_color="black",
            values=["Nam", "Nữ", "Khác"],
            font=font1,
            width=250,
        )

        gender_txt.set("Nam")
        gender_txt.place(x=1240, y=200)

        mobile_lbl = Label(root, text="SĐT: ", bg="#212325", fg="white", font=font)
        mobile_lbl.place(x=1350, y=320)

        mobile_txt = customtkinter.CTkEntry(
            master=root, fg_color="white", text_color="black", font=font1, width=250
        )
        mobile_txt.configure(textvariable=self.mobile_txt)
        mobile_txt.place(x=1240, y=250)

        address_lbl = Label(root, text="Địa chỉ: ", bg="#212325", fg="white", font=font)
        address_lbl.place(x=630, y=395)

        address_txt = customtkinter.CTkEntry(
            master=root, fg_color="white", text_color="black", font=font1, width=250
        )
        address_txt.configure(textvariable=self.address_txt)
        address_txt.place(x=650, y=310)

        email_lbl = Label(root, text="Email: ", bg="#212325", fg="white", font=font)
        email_lbl.place(x=1350, y=390)

        email_txt = customtkinter.CTkEntry(
            master=root, fg_color="white", text_color="black", font=font1, width=250
        )
        email_txt.configure(textvariable=self.email_txt)
        email_txt.place(x=1240, y=305)

        password_lbl = Label(
            root, text="Mật khâủ: ", bg="#212325", fg="white", font=font
        )
        password_lbl.place(x=630, y=465)

        password_txt = customtkinter.CTkEntry(
            master=root, fg_color="white", text_color="black", font=font1, width=250
        )
        password_txt.configure(textvariable=self.password_txt)
        password_txt.place(x=650, y=365)

        credit_lbl = Label(
            root, text="Số thẻ tín dụng: ", bg="#212325", fg="white", font=font
        )
        credit_lbl.place(x=1350, y=460)

        credit_txt = customtkinter.CTkEntry(
            master=root, fg_color="white", text_color="black", font=font1, width=250
        )
        credit_txt.configure(textvariable=self.credit_txt)
        credit_txt.place(x=1240, y=360)

        def save_customer_info():
            if (
                (name_txt.get() == "")
                or (dob_txt.get() == "")
                or (gender_txt.get() == "")
                or (mobile_txt.get() == "")
                or (email_txt.get() == "")
                or (address_txt.get() == "")
                or (password_txt.get() == "")
                or (credit_txt.get() == 0)
            ):
                warning = messagebox.showwarning(
                    "Hệ thống đặt xe taxi",
                    "Vui lòng nhập đầy đủ thông tin!",
                )

            else:
                customer_info = CustomerLibs(
                    "",
                    name_txt.get(),
                    dob_txt.get(),
                    gender_txt.get(),
                    mobile_txt.get(),
                    email_txt.get(),
                    address_txt.get(),
                    password_txt.get(),
                    credit_txt.get(),
                    status="Customer",
                )
                result = insert_record(customer_info)
                if result == True:
                    promt = messagebox.showinfo(
                        "Hệ thống đặt xe taxi",
                        "Thêm tài khoản khách hàng thành công!",
                    )
                else:
                    promt1 = messagebox.showerror(
                        "Lỗi!",
                        "Thêm tài khoản khách hàng thất bại!",
                    )

        register_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/edit.png"
            )
        )

        register_btn = customtkinter.CTkButton(
            master=root,
            command=save_customer_info,
            text="Đăng ký",
            image=register_btn_image,
            hover_color="black",
            font=("Tahoma", 20, "bold"),
        )
        register_btn.place(x=900, y=500)

        def clear():
            self.name_txt.set("")
            self.mobile_txt.set("")
            self.credit_txt.set("")
            self.gender_txt.set("")
            self.address_txt.set("")
            self.password_txt.set("")
            self.email_txt.set("")

            if (
                (name_txt.get() == "")
                or (mobile_txt.get() == "")
                or (credit_txt.get() == "")
                or (address_txt.get() == "")
                or (password_txt.get() == "")
                or (email_txt.get() == "")
            ):
                msg1 = messagebox.showinfo(
                    "Hệ thống đặt xe taxi",
                    "Tất cả các trường đã được xóa!",
                )

            else:
                msg2 = messagebox.showerror("Lỗi!", "Đã xảy ra lỗi!")

        clear_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/cleaning.png"
            )
        )
        clear_btn = customtkinter.CTkButton(
            master=root,
            command=clear,
            text="Xóa",
            image=clear_btn_image,
            hover_color="black",
            font=("Tahoma", 20, "bold"),
        )
        clear_btn.place(x=1080, y=500)

        back_lbl = customtkinter.CTkLabel(
            master=root,
            text="Bạn đã có tài khoản?",
            font=("", 14, "normal"),
            text_color="white",
        )
        back_lbl.place(x=940, y=550)

        back_btn = customtkinter.CTkButton(
            master=root,
            text="Đăng nhập",
            width=100,
            font=("Tahoma", 14, "bold"),
            hover_color="black",
            command=signin,
        )
        back_btn.place(x=1080, y=550)


if __name__ == "__main__":
    root = customtkinter.CTk()
    Register(root)
    root.mainloop()
