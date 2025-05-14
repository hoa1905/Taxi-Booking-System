from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from libs import Global


class CustomerProfile:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.resizable(0, 0)
        self.main.title("Hồ sơ {}".format(Global.current_user[1]))
        self.main.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )
        width = 750
        height = 400
        my_screen_width = self.main.winfo_screenwidth()
        my_screen_height = self.main.winfo_screenheight()
        xCordinate = int((my_screen_width / 2) - (width / 2))
        yCordinate = int((my_screen_height / 2) - (height / 2))
        self.main.geometry(
            "{}x{}+{}+{}".format(width, height, xCordinate, yCordinate - 50)
        )
        self.main.maxsize(950, 400)

        # ++++++++++++++++++++++++++++My Font++++++++++++++++++++++++++++++++++++++++++
        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=19, weight="normal"
        )

        # ++++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++
        center_frame = customtkinter.CTkFrame(master=self.main, width=710, height=320)
        center_frame.place(x=20, y=60)

        # ++++++++++++++++++++++++++++++++++++++Name Label+++++++++++++++++++++++++++++++++++++++
        name_lbl = customtkinter.CTkLabel(center_frame, text="Tên: ", font=font720)
        name_lbl.place(x=50, y=100)

        # +++++++++++++++++++++++++++++++++++++Global Name Label+++++++++++++++++++++++++++++++++++++
        name_lbl1 = customtkinter.CTkLabel(
            center_frame, text="{}".format(Global.current_user[1]), font=font720
        )
        name_lbl1.place(x=150, y=100)

        # ++++++++++++++++++++++++++++++++++++++++DOB Label+++++++++++++++++++++++++++++++++++++
        dob_lbl = customtkinter.CTkLabel(center_frame, text="Ngày sinh: ", font=font720)
        dob_lbl.place(x=50, y=150)

        # +++++++++++++++++++++++++++++++++++++Global DOB Label+++++++++++++++++++++++++++++++++++++++
        # .format(Global.current_user[2])
        dob1_lbl = customtkinter.CTkLabel(
            center_frame, text="{}".format(Global.current_user[2]), font=font720
        )
        dob1_lbl.place(x=150, y=150)

        # +++++++++++++++++++++++++++++++++++++Gender Label+++++++++++++++++++++++++++++++++++++++
        gender_lbl = customtkinter.CTkLabel(
            center_frame, text="Giới tính: ", font=font720
        )
        gender_lbl.place(x=50, y=200)

        # +++++++++++++++++++++++++++++++++++++Global Gender Label+++++++++++++++++++++++++++++++++++++++
        gender1_lbl = customtkinter.CTkLabel(
            center_frame, text="{}".format(Global.current_user[3]), font=font720
        )
        gender1_lbl.place(x=150, y=200)

        # +++++++++++++++++++++++++++++++++++++Mobile Label+++++++++++++++++++++++++++++++++++++++
        mobile_lbl = customtkinter.CTkLabel(center_frame, text="SĐT: ", font=font720)
        mobile_lbl.place(x=50, y=250)

        # +++++++++++++++++++++++++++++++++++++Global Mobile Label+++++++++++++++++++++++++++++++++++++++
        mobile1_lbl = customtkinter.CTkLabel(
            center_frame, text="{}".format(Global.current_user[4]), font=font720
        )
        mobile1_lbl.place(x=150, y=250)

        # +++++++++++++++++++++++++++++++++++++Email Label+++++++++++++++++++++++++++++++++++++++
        email_lbl = customtkinter.CTkLabel(center_frame, text="Email: ", font=font720)
        email_lbl.place(x=370, y=100)

        # +++++++++++++++++++++++++++++++++++++Global Email Label+++++++++++++++++++++++++++++++++++++++
        email1_lbl = customtkinter.CTkLabel(
            center_frame, text="{}".format(Global.current_user[5]), font=font720
        )
        email1_lbl.place(x=510, y=100)

        # +++++++++++++++++++++++++++++++++++++Address Label+++++++++++++++++++++++++++++++++++++++
        address_lbl = customtkinter.CTkLabel(
            center_frame, text="Địa chỉ: ", font=font720
        )
        address_lbl.place(x=370, y=150)

        # +++++++++++++++++++++++++++++++++++++Global Address Label+++++++++++++++++++++++++++++++++++++++
        address1_lbl = customtkinter.CTkLabel(
            center_frame, text="{}".format(Global.current_user[6]), font=font720
        )
        address1_lbl.place(x=510, y=150)

        # +++++++++++++++++++++++++++++++++++++Credit Label+++++++++++++++++++++++++++++++++++++++
        credit_lbl = customtkinter.CTkLabel(
            center_frame, text="Số thẻ tín dụng: ", font=font720
        )
        credit_lbl.place(x=370, y=200)

        # +++++++++++++++++++++++++++++++++++++Global Credit Label+++++++++++++++++++++++++++++++++++++++
        credit1_lbl = customtkinter.CTkLabel(
            center_frame, text="{}".format(Global.current_user[8]), font=font720
        )
        credit1_lbl.place(x=510, y=200)

        # +++++++++++++++++++++++++++++++++++++Image Label+++++++++++++++++++++++++++++++++++++++
        user_image = ImageTk.PhotoImage(
            Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-solid-120.png"
            )
        )
        user_image_label = Label(self.main, image=user_image, bg="#212325")
        user_image_label.image = user_image
        user_image_label.place(x=400, y=20)


if __name__ == "__main__":
    main = customtkinter.CTk()
    CustomerProfile(main)
    main.mainloop()
