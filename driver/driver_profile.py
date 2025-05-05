from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from libs import Global


class DriverProfile:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.title("Hồ sơ cá nhân của {}".format(Global.current_driver[1]))
        self.main.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )
        width = 750
        height = 350
        self.main.resizable(0, 0)
        my_screen_width = self.main.winfo_screenwidth()
        my_screen_height = self.main.winfo_screenheight()
        xCordinate = int((my_screen_width / 2) - (width / 2))
        yCordinate = int((my_screen_height / 2) - (height / 2))
        self.main.geometry(
            "{}x{}+{}+{}".format(width, height, xCordinate + 50, yCordinate - 50)
        )
        self.main.maxsize(950, 400)

        # ++++++++++++++++++++++++++++My Font++++++++++++++++++++++++++++++++++++++++++
        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=19, weight="normal"
        )

        # ++++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++
        center_frame = customtkinter.CTkFrame(master=self.main, width=710, height=250)
        center_frame.place(x=20, y=60)

        # ++++++++++++++++++++++++++++++++++++++Name Label+++++++++++++++++++++++++++++++++++++++
        name_lbl = customtkinter.CTkLabel(
            center_frame, text="Họ và tên: ", font=font720
        )
        name_lbl.place(x=50, y=100)

        # +++++++++++++++++++++++++++++++++++++Global Name Label+++++++++++++++++++++++++++++++++++++
        name_lbl1 = customtkinter.CTkLabel(
            center_frame, text="{}".format(Global.current_driver[1]), font=font720
        )
        name_lbl1.place(x=150, y=100)

        # +++++++++++++++++++++++++++++++++++++Mobile Label+++++++++++++++++++++++++++++++++++++++
        mobile_lbl = customtkinter.CTkLabel(center_frame, text="SĐT: ", font=font720)
        mobile_lbl.place(x=50, y=150)

        # +++++++++++++++++++++++++++++++++++++Global Mobile Label+++++++++++++++++++++++++++++++++++++++
        mobile1_lbl = customtkinter.CTkLabel(
            center_frame, text="{}".format(Global.current_driver[2]), font=font720
        )
        mobile1_lbl.place(x=150, y=150)

        # +++++++++++++++++++++++++++++++++++++Email Label+++++++++++++++++++++++++++++++++++++++
        email_lbl = customtkinter.CTkLabel(center_frame, text="Email: ", font=font720)
        email_lbl.place(x=340, y=100)

        # +++++++++++++++++++++++++++++++++++++Global Email Label+++++++++++++++++++++++++++++++++++++++
        email1_lbl = customtkinter.CTkLabel(
            center_frame, text="{}".format(Global.current_driver[3]), font=font720
        )
        email1_lbl.place(x=510, y=100)

        # +++++++++++++++++++++++++++++++++++++Address Label+++++++++++++++++++++++++++++++++++++++
        license_lbl = customtkinter.CTkLabel(
            center_frame, text="Số giấy phép lái xe: ", font=font720
        )
        license_lbl.place(x=340, y=150)

        # +++++++++++++++++++++++++++++++++++++Global Address Label+++++++++++++++++++++++++++++++++++++++
        license1_lbl = customtkinter.CTkLabel(
            center_frame, text="{}".format(Global.current_driver[4]), font=font720
        )
        license1_lbl.place(x=510, y=150)

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
    DriverProfile(main)
    main.mainloop()
