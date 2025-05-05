from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from tkinter import messagebox
from dbms.password_change_backend import password_change
from libs import Global
from libs.customer_libs import CustomerLibs


class PasswordChange(customtkinter.CTk):
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.root.title("Hệ thống đặt xe taxi | Đối mật khẩu khách hàng")
        self.root.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )
        frame_width = 530
        frame_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.root.geometry(
            "{}x{}+{}+{}".format(
                frame_width, frame_height, x_cordinate + 70, y_cordinate - 70
            )
        )
        self.root.resizable(0, 0)

        frame = customtkinter.CTkFrame(self.root)
        frame.pack(fill=BOTH, expand=TRUE)

        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )

        img = ImageTk.PhotoImage(
            Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-solid-72.png"
            )
        )
        image_label = Label(self.root, image=img, bg="#2b2b2b")
        image_label.image = img
        image_label.place(x=150, y=40)

        title_lbl = customtkinter.CTkLabel(
            master=self.root,
            text="Đối mật khẩu",
            font=font720,
            bg_color="#2b2b2b",
        )
        title_lbl.place(x=200, y=40)

        current_pw_lbl = customtkinter.CTkLabel(
            master=self.root, text="Mật khẩu mới: ", font=font720, bg_color="#2b2b2b"
        )
        current_pw_lbl.place(x=50, y=150)

        current_pw_txt = customtkinter.CTkEntry(
            master=self.root, font=font720, show="*", width=200
        )
        current_pw_txt.place(x=230, y=150)

        confirm_pw_lbl = customtkinter.CTkLabel(
            master=self.root,
            text="Nhập lại mật khẩu mới: ",
            font=font720,
            bg_color="#2b2b2b",
        )
        confirm_pw_lbl.place(x=50, y=220)

        conform_pw_txt = customtkinter.CTkEntry(
            master=self.root, show="*", font=font720, width=200
        )
        conform_pw_txt.place(x=230, y=220)

        def show_password():
            if i.get() == 1:
                conform_pw_txt.configure(show="")
                current_pw_txt.configure(show="")
            else:
                conform_pw_txt.configure(show="*")
                current_pw_txt.configure(show="*")

        i = customtkinter.IntVar()

        password_show = customtkinter.CTkCheckBox(
            self.root,
            text="Hiện mật khẩu",
            variable=i,
            command=show_password,
            bg_color="#2b2b2b",
        )
        password_show.place(x=240, y=260)

        id_txt = Entry(self.root)
        id_txt.insert(0, "{}".format(Global.current_user[0]))

        def change_password():
            customerid = id_txt.get()
            password1 = current_pw_txt.get()
            newpassword = conform_pw_txt.get()

            if password1 == newpassword:
                password720 = CustomerLibs(cid=customerid, password=newpassword)
                result = password_change(password720)
                if result == True:
                    messagebox.showinfo(
                        "Hệ thống đặt xe taxi", "Đổi mật khẩu thành công!"
                    )
                    self.root.destroy()
                else:
                    messagebox.showerror("Hệ thống đặt xe taxi", "Đã có lỗi xảy ra!")

            else:
                messagebox.showerror(
                    "Hệ thống đặt xe taxi",
                    "Mật khẩu không trùng khớp!",
                )

        confirm_btn = customtkinter.CTkButton(
            master=self.root,
            command=change_password,
            text="Đối mật khẩu!",
            font=font720,
        )
        confirm_btn.place(x=230, y=310)


if __name__ == "__main__":
    root = customtkinter.CTk()
    PasswordChange(root)
    root.mainloop()
