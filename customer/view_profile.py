from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from customer import customer_profile, update_customer_profile
from libs import Global


class ViewCustomerProfile:
    def __init__(self, profile):
        self.profile = profile
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.profile.resizable(0, 0)
        self.profile.title("Xem hồ sơ {}".format(Global.current_user[1]))
        self.profile.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )
        width = 500
        height = 200
        my_screen_width = self.profile.winfo_screenwidth()
        my_screen_height = self.profile.winfo_screenheight()
        xCordinate = int((my_screen_width / 2) - (width / 2))
        yCordinate = int((my_screen_height / 2) - (height / 2))
        self.profile.geometry(
            "{}x{}+{}+{}".format(width, height, xCordinate + 100, yCordinate - 50)
        )
        self.profile.maxsize(950, 400)

        # ++++++++++++++++++++++++++++My Font++++++++++++++++++++++++++++++++++++++++++
        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=19, weight="normal"
        )

        view_profile_frame = customtkinter.CTkFrame(self.profile, width=200, height=150)
        view_profile_frame.place(x=20, y=20)

        image = Image.open(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-solid-72.png"
        )
        image = image.resize((80, 80))
        image = ImageTk.PhotoImage(image)
        image_label = Label(view_profile_frame, image=image, bg="#2b2b2b")
        image_label.image = image
        image_label.place(x=75, y=20)

        def open_profile():
            # self.profile.destroy()
            main = customtkinter.CTkToplevel()
            customer_profile.CustomerProfile(main)
            main.mainloop()

        label = customtkinter.CTkButton(
            view_profile_frame,
            fg_color="#2b2b2b",
            command=open_profile,
            hover_color="#2b2b2b",
            text="Xem hồ sơ cá nhân",
            font=font720,
        )
        label.place(x=25, y=100)

        update_profile_frame = customtkinter.CTkFrame(
            self.profile, width=230, height=150
        )
        update_profile_frame.place(x=250, y=20)

        image1 = Image.open(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-solid-72.png"
        )
        image1 = image1.resize((80, 80))
        image1 = ImageTk.PhotoImage(image1)
        image_label1 = Label(update_profile_frame, image=image1, bg="#2b2b2b")
        image_label1.image = image1
        image_label1.place(x=100, y=20)

        def open_update_profile():
            # self.profile.destroy()
            updateprofile = customtkinter.CTkToplevel()
            update_customer_profile.UpdateCustomerProfile(updateprofile)
            updateprofile.mainloop()

        label1 = customtkinter.CTkButton(
            update_profile_frame,
            command=open_update_profile,
            fg_color="#2b2b2b",
            hover_color="#2b2b2b",
            text="Cập nhật hồ sơ cá nhân",
            font=font720,
        )
        label1.place(x=15, y=100)


if __name__ == "__main__":
    profile = customtkinter.CTk()
    ViewCustomerProfile(profile)
    profile.mainloop()
