from tkinter import *
from tkinter import messagebox
from PIL import Image
import customtkinter

from dbms.customer_management import (
    insert_record,
    search_customer,
    update_record,
    delete_record,
)
from libs.customer_libs import CustomerLibs


class CustomerManagement(customtkinter.CTk):
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.title("Hệ thống đặt xe taxi | Quản lý khách hàng")
        self.main.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )
        width = 1050
        height = 450
        my_screen_width = self.main.winfo_screenwidth()
        my_screen_height = self.main.winfo_screenheight()
        xCordinate = int((my_screen_width / 2) - (width / 2))
        yCordinate = int((my_screen_height / 2) - (height / 2))
        self.main.geometry(
            "{}x{}+{}+{}".format(width, height, xCordinate + 200, yCordinate)
        )
        self.main.maxsize(1050, 450)

        # font
        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )

        # All the variables
        self.id_txt = StringVar()
        self.name_txt = StringVar()
        self.gender_txt = StringVar()
        self.mobile_txt = StringVar()
        self.email_txt = StringVar()
        self.address_txt = StringVar()
        self.dob_txt = StringVar()
        self.password_txt = StringVar()
        self.credit_txt = StringVar()

        # +++++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++++++++++++++++
        top_frame = customtkinter.CTkFrame(master=self.main, height=70)
        top_frame.pack(side=TOP, fill=BOTH, padx=20, pady=(10, 20))

        # +++++++++++++++++++++++++++++++++++Title Label+++++++++++++++++++++++++++++++++++++
        title_label = customtkinter.CTkLabel(
            master=top_frame,
            text="HỆ THỐNG QUẢN LÝ KHÁCH HÀNG",
            font=("Times New Roman", 25, "bold"),
        )
        title_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # ++++++++++++++++++++++++++++++++Center Frame++++++++++++++++++++++++++++++++++
        center_frame = customtkinter.CTkFrame(master=self.main, width=1000, height=340)
        center_frame.pack(anchor=CENTER)

        def searchCustomer():
            customer_id = id_txt.get()
            customer_result = search_customer(customer_id)
            if customer_result == None:
                messagebox.showwarning(
                    "Hệ thống quản lý khách hàng",
                    "Mã khách hàng {} không được tìm thấy".format(customer_id),
                )

            else:
                name_txt.delete(0, len(name_txt.get()))
                name_txt.insert(0, customer_result[1])

                dob_txt.delete(0, len(dob_txt.get()))
                dob_txt.insert(0, customer_result[2])

                gender_txt.delete(0, len(gender_txt.get()))
                gender_txt.insert(0, customer_result[3])

                mobile_txt.delete(0, len(mobile_txt.get()))
                mobile_txt.insert(0, customer_result[4])

                email_txt.delete(0, len(email_txt.get()))
                email_txt.insert(0, customer_result[5])

                address_txt.delete(0, len(address_txt.get()))
                address_txt.insert(0, customer_result[6])

                password_txt.delete(0, len(password_txt.get()))
                password_txt.insert(0, customer_result[7])

                credit_txt.delete(0, len(credit_txt.get()))
                credit_txt.insert(0, customer_result[8])

        # ++++++++++++++++++++++++++++ID Label+++++++++++++++++++++++++++++++++++++
        id_lbl = customtkinter.CTkLabel(
            master=center_frame, text="Tìm kiếm: ", font=font720
        )
        id_lbl.place(x=20, y=20)

        # ++++++++++++++++++++++++++++++ID TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        id_txt = customtkinter.CTkEntry(
            master=center_frame,
            placeholder_text="Nhập mã khách hàng",
            font=font720,
            width=200,
        )
        id_txt.place(x=120, y=15)

        search_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/search-alt-2-regular-24.png"
            )
        )
        search_customer_btn = customtkinter.CTkButton(
            master=center_frame,
            image=search_image,
            text="Tìm kiếm",
            command=searchCustomer,
            font=font720,
            width=180,
        )
        search_customer_btn.place(x=340, y=15)

        # ++++++++++++++++++++++++Center Frame 2+++++++++++++++++++++++++++++++++++
        center_frame2 = customtkinter.CTkFrame(
            master=center_frame, height=255, width=690
        )
        center_frame2.place(x=20, y=65)

        # ++++++++++++++++++++++++++++Name Label+++++++++++++++++++++++++++++++++++++
        name_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="Tên: ", font=font720
        )
        name_lbl.place(x=40, y=30)

        # ++++++++++++++++++++++++++++++TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        name_txt = customtkinter.CTkEntry(
            master=center_frame2, textvariable=self.name_txt, font=font720, width=200
        )
        name_txt.place(x=150, y=30)

        # ++++++++++++++++++++++++++++DOB Label+++++++++++++++++++++++++++++++++++++
        dob_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="Ngày sinh: ", font=font720
        )
        dob_lbl.place(x=380, y=30)

        # ++++++++++++++++++++++++++++++DOB TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        dob_txt = customtkinter.CTkEntry(
            master=center_frame2, textvariable=self.dob_txt, font=font720, width=200
        )
        dob_txt.place(x=470, y=30)

        # ++++++++++++++++++++++++++++Gender Label+++++++++++++++++++++++++++++++++++++
        gender_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="Giới tính: ", font=font720
        )
        gender_lbl.place(x=380, y=80)

        # ++++++++++++++++++++++++++++++Gender TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        gender_txt = customtkinter.CTkEntry(
            master=center_frame2, textvariable=self.gender_txt, font=font720, width=200
        )
        gender_txt.place(x=470, y=80)

        # ++++++++++++++++++++++++++++Address Label+++++++++++++++++++++++++++++++++++++
        address_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="Địa chỉ: ", font=font720
        )
        address_lbl.place(x=380, y=130)

        # ++++++++++++++++++++++++++++++Address TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        address_txt = customtkinter.CTkEntry(
            master=center_frame2, textvariable=self.address_txt, font=font720, width=200
        )
        address_txt.place(x=470, y=130)

        # ++++++++++++++++++++++++++++Credit Label+++++++++++++++++++++++++++++++++++++
        credit_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="Số thẻ tín dụng: ", font=font720
        )
        credit_lbl.place(x=380, y=180)

        # ++++++++++++++++++++++++++++++Credit TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        credit_txt = customtkinter.CTkEntry(
            master=center_frame2, textvariable=self.credit_txt, font=font720, width=200
        )
        credit_txt.place(x=470, y=180)

        # +++++++++++++++++++++++++++++Mobile Label++++++++++++++++++++++++++++
        mobile_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="SĐT: ", font=font720
        )
        mobile_lbl.place(x=40, y=80)

        # ++++++++++++++++++++++++++++++Mobile TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        mobile_txt = customtkinter.CTkEntry(
            master=center_frame2, textvariable=self.mobile_txt, font=font720, width=200
        )
        mobile_txt.place(x=150, y=80)

        # +++++++++++++++++++++++++++++Email Label++++++++++++++++++++++++++++
        email_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="Email: ", font=font720
        )
        email_lbl.place(x=40, y=130)

        # ++++++++++++++++++++++++++++++Email TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        email_txt = customtkinter.CTkEntry(
            master=center_frame2, textvariable=self.email_txt, font=font720, width=200
        )
        email_txt.place(x=150, y=130)

        # +++++++++++++++++++++++++++++Password Label++++++++++++++++++++++++++++
        password_lbl = customtkinter.CTkLabel(
            master=center_frame2, text="Mật khẩu: ", font=font720
        )
        password_lbl.place(x=40, y=180)

        # ++++++++++++++++++++++++++++++Password TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        password_txt = customtkinter.CTkEntry(
            master=center_frame2,
            textvariable=self.password_txt,
            font=font720,
            width=200,
        )
        password_txt.place(x=150, y=180)

        side_frame = customtkinter.CTkFrame(master=center_frame, width=250, height=300)
        side_frame.place(x=730, y=20)

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
                    "Hệ thống quản lý khách hàng",
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
                        "Hệ thống quản lý khách hàng",
                        "Thêm tài khoản khách hàng thành công!",
                    )
                else:
                    promt1 = messagebox.showerror(
                        "Lỗi!", "Thêm tài khoản khách hàng thất bại!"
                    )

        save_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/check-square-regular-24.png"
            )
        )
        save_btn = customtkinter.CTkButton(
            master=side_frame,
            command=save_customer_info,
            image=save_image,
            text="Lưu thông tin",
            font=font720,
            width=180,
            hover_color="black",
        )
        save_btn.place(x=35, y=50)

        def update():
            customer_info = CustomerLibs(
                cid=id_txt.get(),
                name=name_txt.get(),
                dob=dob_txt.get(),
                gender=gender_txt.get(),
                mobile=mobile_txt.get(),
                email=email_txt.get(),
                address=address_txt.get(),
                credit=credit_txt.get(),
                status="Customer",
            )
            update_result = update_record(customer_info)
            if update_result == True:
                messagebox.showinfo("Hệ thống quản lý khách hàng", "Đã được cập nhật")

            else:
                messagebox.showwarning(
                    "Hệ thống quản lý khách hàng", "Câp nhật không thành công!"
                )

        update_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/edit-alt-regular-24.png"
            )
        )
        update_btn = customtkinter.CTkButton(
            master=side_frame,
            command=update,
            text="Cập nhật thông tin",
            image=update_image,
            font=font720,
            width=180,
            hover_color="black",
        )
        update_btn.place(x=35, y=100)

        def delete():
            customer_id = id_txt.get()
            delete_result = delete_record(customer_id)
            if delete_result == True:
                messagebox.showinfo(
                    "Hệ thống quản lý khách hàng",
                    "Mã khách hàng {} đã được xóa thành công".format(customer_id),
                )

            else:
                messagebox.showerror("Hệ thống quản lý khách hàng", "Đã có lỗi xảy ra!")

        delete_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-x-regular-24.png"
            )
        )
        delete_btn = customtkinter.CTkButton(
            master=side_frame,
            image=delete_image,
            command=delete,
            text="Xóa thông tin",
            font=font720,
            width=180,
            hover_color="black",
        )
        delete_btn.place(x=35, y=150)

        def clear():
            self.id_txt.set("")
            self.name_txt.set("")
            self.email_txt.set("")
            self.mobile_txt.set("")
            self.address_txt.set("")
            self.password_txt.set("")
            self.dob_txt.set("")
            self.gender_txt.set("")
            self.credit_txt.set("")

        clear_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-x-regular-24.png"
            )
        )
        clear_btn = customtkinter.CTkButton(
            master=side_frame,
            image=clear_image,
            text="Clear",
            command=clear,
            font=font720,
            width=180,
            hover_color="black",
        )
        clear_btn.place(x=35, y=200)


if __name__ == "__main__":
    main = customtkinter.CTk()
    CustomerManagement(main)
    main.mainloop()
