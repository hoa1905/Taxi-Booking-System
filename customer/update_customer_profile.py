from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from tkinter import messagebox
from dbms.customer_management import update_customer_record
from libs import Global
from libs.customer_libs import CustomerLibs


class UpdateCustomerProfile:
    def __init__(self, update_profile):
        self.update_profile = update_profile
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.update_profile.resizable(0, 0)
        self.update_profile.title("Hồ sơ {}".format(Global.current_user[1]))
        self.update_profile.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )
        width = 750
        height = 440
        my_screen_width = self.update_profile.winfo_screenwidth()
        my_screen_height = self.update_profile.winfo_screenheight()
        xCordinate = int((my_screen_width / 2) - (width / 2))
        yCordinate = int((my_screen_height / 2) - (height / 2))
        self.update_profile.geometry(
            "{}x{}+{}+{}".format(width, height, xCordinate, yCordinate - 50)
        )
        self.update_profile.maxsize(750, 440)

        id = Entry(self.update_profile)
        id.insert(0, Global.current_user[0])

        # ++++++++++++++++++++++++++++My Font++++++++++++++++++++++++++++++++++++++++++
        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=19, weight="normal"
        )

        # ++++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++
        center_frame = customtkinter.CTkFrame(
            master=self.update_profile, width=710, height=360
        )
        center_frame.place(x=20, y=60)

        # ++++++++++++++++++++++++++++++++++++++Name Label+++++++++++++++++++++++++++++++++++++++
        name_lbl = customtkinter.CTkLabel(center_frame, text="Tên: ", font=font720)
        name_lbl.place(x=20, y=100)

        # +++++++++++++++++++++++++++++++++++++Global Name Label+++++++++++++++++++++++++++++++++++++
        name_txt = customtkinter.CTkEntry(center_frame, width=180, font=font720)
        name_txt.insert(0, Global.current_user[1])
        name_txt.place(x=120, y=100)

        # ++++++++++++++++++++++++++++++++++++++++DOB Label+++++++++++++++++++++++++++++++++++++
        dob_lbl = customtkinter.CTkLabel(center_frame, text="Ngày sinh: ", font=font720)
        dob_lbl.place(x=20, y=150)

        # +++++++++++++++++++++++++++++++++++++Global DOB Label+++++++++++++++++++++++++++++++++++++++
        # .format(Global.current_user[2])
        dob1_txt = customtkinter.CTkEntry(center_frame, width=180, font=font720)
        dob1_txt.insert(0, Global.current_user[2])
        dob1_txt.place(x=120, y=150)

        # +++++++++++++++++++++++++++++++++++++Gender Label+++++++++++++++++++++++++++++++++++++++
        gender_lbl = customtkinter.CTkLabel(
            center_frame, text="Giới tính: ", font=font720
        )
        gender_lbl.place(x=20, y=200)

        # +++++++++++++++++++++++++++++++++++++Global Gender Label+++++++++++++++++++++++++++++++++++++++
        gender1_txt = customtkinter.CTkEntry(center_frame, width=180, font=font720)
        gender1_txt.insert(0, Global.current_user[3])
        gender1_txt.place(x=120, y=200)

        # +++++++++++++++++++++++++++++++++++++Mobile Label+++++++++++++++++++++++++++++++++++++++
        mobile_lbl = customtkinter.CTkLabel(center_frame, text="SĐT: ", font=font720)
        mobile_lbl.place(x=20, y=250)

        # +++++++++++++++++++++++++++++++++++++Global Mobile Label+++++++++++++++++++++++++++++++++++++++
        mobile1_txt = customtkinter.CTkEntry(center_frame, width=180, font=font720)
        mobile1_txt.insert(0, Global.current_user[4])
        mobile1_txt.place(x=120, y=250)

        # +++++++++++++++++++++++++++++++++++++Email Label+++++++++++++++++++++++++++++++++++++++
        email_lbl = customtkinter.CTkLabel(center_frame, text="Email: ", font=font720)
        email_lbl.place(x=360, y=100)

        # +++++++++++++++++++++++++++++++++++++Global Email Label+++++++++++++++++++++++++++++++++++++++
        email1_txt = customtkinter.CTkEntry(center_frame, width=190, font=font720)
        email1_txt.insert(0, Global.current_user[5])
        email1_txt.place(x=500, y=100)

        # +++++++++++++++++++++++++++++++++++++Address Label+++++++++++++++++++++++++++++++++++++++
        address_lbl = customtkinter.CTkLabel(
            center_frame, text="Địa chỉ: ", font=font720
        )
        address_lbl.place(x=360, y=150)

        # +++++++++++++++++++++++++++++++++++++Global Address Label+++++++++++++++++++++++++++++++++++++++
        address1_txt = customtkinter.CTkEntry(center_frame, width=190, font=font720)
        address1_txt.insert(0, Global.current_user[6])
        address1_txt.place(x=500, y=150)

        # +++++++++++++++++++++++++++++++++++++Credit Label+++++++++++++++++++++++++++++++++++++++
        credit_lbl = customtkinter.CTkLabel(
            center_frame, text="Số thẻ tín dụng: ", font=font720
        )
        credit_lbl.place(x=360, y=200)

        # +++++++++++++++++++++++++++++++++++++Global Credit Label+++++++++++++++++++++++++++++++++++++++
        credit1_txt = customtkinter.CTkEntry(center_frame, width=190, font=font720)
        credit1_txt.insert(0, Global.current_user[8])
        credit1_txt.place(x=500, y=200)

        def update_customer():
            customer = CustomerLibs(
                cid=id.get(),
                name=name_txt.get(),
                dob=dob1_txt.get(),
                gender=gender1_txt.get(),
                mobile=mobile1_txt.get(),
                email=email1_txt.get(),
                address=address1_txt.get(),
                credit=credit1_txt.get(),
            )
            update_result = update_customer_record(customer)
            if update_result == True:
                messagebox.showinfo(
                    "Hệ thống đặt xe taxi",
                    "Đã cập nhật thành công!",
                )
                self.update_profile.destroy()

            else:
                messagebox.showerror("Hệ thống đặt xe taxi", "Lỗi")

        update_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/edit-alt-regular-24.png"
            )
        )
        update_btn = customtkinter.CTkButton(
            master=center_frame,
            command=update_customer,
            text="Cập nhật chi tiết",
            font=font720,
            image=update_btn_image,
        )
        update_btn.place(x=300, y=320)

        user_image = ImageTk.PhotoImage(
            Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-solid-120.png"
            )
        )
        user_image_label = Label(self.update_profile, image=user_image, bg="#212325")
        user_image_label.image = user_image
        user_image_label.place(x=400, y=20)


if __name__ == "__main__":
    update_profile = customtkinter.CTk()
    UpdateCustomerProfile(update_profile)
    update_profile.mainloop()
