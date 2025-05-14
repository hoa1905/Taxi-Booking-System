from tkinter import *
import customtkinter
from PIL import Image
from dbms.driver_management import (
    insert_record,
    search_record,
    delete_record,
    update_record,
)
from libs.driver_libs import DriverLibs
from tkinter import messagebox


class DriverManagement:

    def __init__(self, driver):
        self.driver = driver
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.driver.title("Hệ thống đặt xe taxi | Quản lý tài xế")
        my_width = 900
        my_height = 500
        screen_Width = self.driver.winfo_screenwidth()
        screen_Height = self.driver.winfo_screenheight()
        xCordinate = int((screen_Width / 2) - (my_width / 2))
        yCordinate = int((screen_Height / 2) - (my_height / 2))
        # +++++++++++++++++++++++++Center Window in to screen++++++++++++++++++++++++++++++
        self.driver.geometry(
            "{}x{}+{}+{}".format(my_width, my_height, xCordinate + 200, yCordinate)
        )
        # +++++++++++++++++++++++++++++++Set Icon in window++++++++++++++++++++++++++++++++++++
        self.driver.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )

        # font
        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )

        # All the variables
        self.id_txt = StringVar()
        self.name_txt = StringVar()
        self.mobile_txt = StringVar()
        self.email_txt = StringVar()
        self.license_txt = StringVar()
        self.password_txt = StringVar()

        # +++++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++++++++++++++++
        top_frame = customtkinter.CTkFrame(master=self.driver, height=70)
        top_frame.pack(side=TOP, fill=BOTH, padx=20, pady=(10, 20))

        # +++++++++++++++++++++++++++++++++++Title Label+++++++++++++++++++++++++++++++++++++
        title_label = customtkinter.CTkLabel(
            master=top_frame,
            text="HỆ THỐNG QUẢN LÝ TÀI XẾ",
            font=("Times New Roman", 25, "bold"),
        )
        title_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # ++++++++++++++++++++++++++++++++Center Frame++++++++++++++++++++++++++++++++++
        center_frame = customtkinter.CTkFrame(master=self.driver, width=855, height=380)
        center_frame.pack(anchor=CENTER)

        def search_driver():
            driver_id = int(id_txt.get())
            search_result = search_record(driver_id)

            if id_txt.get() == "":
                messagebox.showerror(
                    "Hệ thống đặt xe taxi",
                    "Hãy nhập mã tài xế",
                )
            else:
                if search_result == None:
                    messagebox.showerror(
                        "Hệ thống đặt xe taxi",
                        "Không tìm thấy tài xế có mã số " + id_txt.get(),
                    )
                else:
                    name_txt.delete(0, len(name_txt.get()))
                    name_txt.insert(0, search_result[1])

                    mobile_txt.delete(0, len(mobile_txt.get()))
                    mobile_txt.insert(0, search_result[2])

                    email_txt.delete(0, len(email_txt.get()))
                    email_txt.insert(0, search_result[3])

                    license_txt.delete(0, len(license_txt.get()))
                    license_txt.insert(0, search_result[4])

                    password_txt.delete(0, len(password_txt.get()))
                    password_txt.insert(0, search_result[5])

        # ++++++++++++++++++++++++++++ID Label+++++++++++++++++++++++++++++++++++++
        id_lbl = customtkinter.CTkLabel(
            master=center_frame, text="Tìm kiếm: ", font=font720
        )
        id_lbl.place(x=20, y=20)

        # ++++++++++++++++++++++++++++++ID TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        id_txt = customtkinter.CTkEntry(
            master=center_frame,
            placeholder_text="Nhập mã tài xế",
            font=font720,
            width=200,
        )
        id_txt.place(x=120, y=15)

        search_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/search-alt-2-regular-24.png"
            )
        )
        delete_btn = customtkinter.CTkButton(
            master=center_frame,
            image=search_image,
            text="Tìm kiếm",
            command=search_driver,
            font=font720,
            width=180,
        )
        delete_btn.place(x=350, y=15)

        center_frame2 = customtkinter.CTkFrame(
            master=center_frame, height=300, width=540
        )
        center_frame2.place(x=20, y=65)

        # ++++++++++++++++++++++++++++Name Label+++++++++++++++++++++++++++++++++++++
        name_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="Tên: ", font=font720
        )
        name_lbl.place(x=40, y=30)

        # ++++++++++++++++++++++++++++++TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        name_txt = customtkinter.CTkEntry(
            master=center_frame2, textvariable=self.name_txt, font=font720, width=250
        )
        name_txt.place(x=200, y=30)

        # +++++++++++++++++++++++++++++Mobile Label++++++++++++++++++++++++++++
        mobile_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="SĐT: ", font=font720
        )
        mobile_lbl.place(x=40, y=80)

        # ++++++++++++++++++++++++++++++Mobile TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        mobile_txt = customtkinter.CTkEntry(
            master=center_frame2, textvariable=self.mobile_txt, font=font720, width=250
        )
        mobile_txt.place(x=200, y=80)

        # +++++++++++++++++++++++++++++Email Label++++++++++++++++++++++++++++
        email_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="Email: ", font=font720
        )
        email_lbl.place(x=40, y=130)

        # ++++++++++++++++++++++++++++++Email TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        email_txt = customtkinter.CTkEntry(
            master=center_frame2, textvariable=self.email_txt, font=font720, width=250
        )
        email_txt.place(x=200, y=130)

        # +++++++++++++++++++++++++++++License Label++++++++++++++++++++++++++++
        license_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="Số bằng lái xe: ", font=font720
        )
        license_lbl.place(x=40, y=180)

        # ++++++++++++++++++++++++++++++License TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        license_txt = customtkinter.CTkEntry(
            master=center_frame2, textvariable=self.license_txt, font=font720, width=250
        )
        license_txt.place(x=200, y=180)

        # +++++++++++++++++++++++++++++Password Label++++++++++++++++++++++++++++
        password_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="Mật khẩu: ", font=font720
        )
        password_lbl.place(x=40, y=230)

        # ++++++++++++++++++++++++++++++Password TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        password_txt = customtkinter.CTkEntry(
            master=center_frame2,
            textvariable=self.password_txt,
            font=font720,
            width=250,
        )
        password_txt.place(x=200, y=230)

        inner_frame = customtkinter.CTkFrame(master=center_frame, width=250, height=340)
        inner_frame.place(x=580, y=20)

        def save_record():
            if (
                name_txt.get() == ""
                or mobile_txt.get() == ""
                or email_txt.get() == ""
                or license_txt.get() == ""
                or password_txt.get() == ""
            ):
                messagebox.showwarning(
                    "Hệ thống đặt xe taxi", "Vui lòng nhập đầy đủ thông tin!"
                )
            else:
                driver = DriverLibs(
                    name=name_txt.get(),
                    mobile=mobile_txt.get(),
                    email=email_txt.get(),
                    license=license_txt.get(),
                    password=password_txt.get(),
                    driverstatus="Hoạt động",
                )
                result = insert_record(driver)
                if result == True:
                    msg1 = messagebox.showinfo(
                        "Hệ thống đặt xe taxi", "Thêm tài khoản tài xế thành công!"
                    )
                else:
                    msg2 = messagebox.showerror(
                        "Hệ thống đặt xe taxi", "Thêm tài khoản tài xế thất bại!"
                    )

        save_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/check-square-regular-24.png"
            )
        )
        save_btn = customtkinter.CTkButton(
            master=inner_frame,
            command=save_record,
            image=save_image,
            text="Lưu",
            font=font720,
            width=180,
            hover_color="black",
        )
        save_btn.place(x=30, y=80)

        def update():
            driver = DriverLibs(
                name=name_txt.get(),
                mobile=mobile_txt.get(),
                email=email_txt.get(),
                license=license_txt.get(),
                did=id_txt.get(),
            )
            update_result = update_record(driver)

            if update_result == True:
                messagebox.showinfo("Hệ thống đặt xe taxi", "Đã cập nhật thành công!")

            else:
                messagebox.showerror("Hệ thống đặt xe taxi", "Đã có lỗi xảy ra!")

        update_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/edit-alt-regular-24.png"
            )
        )
        update_btn = customtkinter.CTkButton(
            master=inner_frame,
            command=update,
            text="Cập nhật",
            image=update_image,
            font=font720,
            width=180,
            hover_color="black",
        )
        update_btn.place(x=30, y=140)

        def delete():
            id = id_txt.get()
            result = delete_record(id)
            if result == True:
                messagebox.showinfo(
                    "Hệ thống đặt xe taxi", "Xóa tài khoản tài xế thành công!"
                )

            else:
                messagebox.showerror("Hệ thống đặt xe taxi", "Đã có lỗi xảy ra!")

        delete_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-x-regular-24.png"
            )
        )
        delete_btn = customtkinter.CTkButton(
            master=inner_frame,
            image=delete_image,
            command=delete,
            text="Xóa",
            font=font720,
            width=180,
            hover_color="black",
        )
        delete_btn.place(x=30, y=200)

        def clear():
            self.id_txt.set("")
            self.name_txt.set("")
            self.email_txt.set("")
            self.mobile_txt.set("")
            self.license_txt.set("")
            self.password_txt.set("")

        clear_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-x-regular-24.png"
            )
        )
        clear_btn = customtkinter.CTkButton(
            master=inner_frame,
            image=clear_image,
            text="Xóa trắng",
            command=clear,
            font=font720,
            width=180,
            hover_color="black",
        )
        clear_btn.place(x=30, y=260)


if __name__ == "__main__":
    driver = customtkinter.CTk()
    DriverManagement(driver)
    driver.mainloop()
