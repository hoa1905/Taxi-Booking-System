from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image
from datetime import date
from time import strftime
from tktimepicker import AnalogPicker, AnalogThemes, constants
from admin import booking_report, active_booking
from billing import admin_payment, admin_billing_history, billing_report
from customer import customer_management, customer_report, search_customers
from dbms.booking_backend import (
    total_booking,
    select_all,
    update_booking,
    total_revenue,
    validate_admin_booking,
    cancel_status_booking_update,
)
from dbms.customer_backend import total_customer
from dbms.driver_management import total_driver, available_driver, update_driver_status
from driver import driver_management, driver_report, search_drivers
from libs import Global
from libs.booking_libs import BookingLibs
from libs.driver_libs import DriverLibs
from customer import login


class AdminDashboard(customtkinter.CTk):
    def __init__(self, main):

        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.main.screen_width = main.winfo_screenwidth()
        self.main.screen_height = main.winfo_screenheight()

        # Đặt kích thước và vị trí cửa sổ tại (0, 0)
        self.main.geometry(f"{self.main.screen_width}x{self.main.screen_height}+0+0")

        self.main.title("Hệ thống đặt xe taxi | Dashboard Quản trị viên")
        self.main.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )

        # ++++++++++++++++++++++++++++++++Font Collection+++++++++++++++++++++++++++++++++++++++++++
        title_font = customtkinter.CTkFont(
            family="Times New Roman", size=35, weight="normal"
        )
        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )
        label_font = customtkinter.CTkFont(
            family="Times New Roman", size=25, weight="normal"
        )
        side_menu_font = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )

        # ++++++++++++++++++++++++++++++++++++++Top Frame+++++++++++++++++++++++++++++++++++++++++++
        north_frame = customtkinter.CTkFrame(
            master=self.main, height=80, corner_radius=0
        )
        north_frame.pack(side=TOP, fill=BOTH)

        # +++++++++++++++++++++++++++++++++++Welcome Label++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        welcome_label = customtkinter.CTkLabel(
            master=north_frame,
            text="Xin chào {}".format(Global.current_admin[1]),
            font=("Times New Roman", 30, "bold"),
            text_color="white",
            fg_color="#2b2b2b",
        )
        welcome_label.place(x=1290, y=25)

        # +++++++++++++++++++++++++++++Title Label++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        title_lbl = customtkinter.CTkLabel(
            master=north_frame, text="Dashboard Quản trị viên", font=title_font
        )
        title_lbl.place(x=50, y=25)

        # +++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++++
        left_frame = customtkinter.CTkFrame(master=self.main, width=300)
        left_frame.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        # +++++++++++++++++++++++++++++++Image+++++++++++++++++++++++++++++++++++++++
        user_image = ImageTk.PhotoImage(
            Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-solid-120.png"
            )
        )
        user_image_label = Label(left_frame, image=user_image, bg="#2b2b2b")
        user_image_label.image = user_image
        user_image_label.place(x=100, y=40)

        def my_time():
            time_string = strftime("%I:%M:%S %p")  # time format
            l1.configure(text=time_string)
            l1.after(1000, my_time)  # time delay of 1000 milliseconds

        l1 = customtkinter.CTkLabel(master=left_frame, font=side_menu_font)
        l1.place(x=90, y=150)
        my_time()

        def assign_driver_gui():
            root = customtkinter.CTkToplevel()
            root.title("Hệ thống đặt xe taxi | Phân công tài xế")
            width = 1500
            height = 490
            my_screen_width = self.main.winfo_screenwidth()
            my_screen_height = self.main.winfo_screenheight()
            xCordinate = int((my_screen_width / 2) - (width / 2))
            yCordinate = int((my_screen_height / 2) - (height / 2))
            root.geometry(
                "{}x{}+{}+{}".format(width, height, xCordinate + 100, yCordinate)
            )
            root.iconbitmap(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
            )
            root.resizable(0, 0)

            assign_booking_frame = customtkinter.CTkFrame(
                root, width=400, corner_radius=20
            )
            assign_booking_frame.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

            title11lbl = customtkinter.CTkLabel(
                master=assign_booking_frame, text="Phân công tài xế", font=font720
            )
            title11lbl.place(x=110, y=20)

            # +++++++++++++++++++++++++++++++Pickup label+++++++++++++++++++++++++++++++++++++++
            pick_up_address_lbl = customtkinter.CTkLabel(
                assign_booking_frame, text="Điểm đón: ", font=font720
            )
            pick_up_address_lbl.place(x=30, y=100)

            pick_up_address_txt = customtkinter.CTkEntry(
                assign_booking_frame, font=font720, width=200
            )
            pick_up_address_txt.bind("<Button-1>", lambda e: "break")
            pick_up_address_txt.bind("<Key>", lambda e: "break")
            pick_up_address_txt.place(x=140, y=100)

            date_lbl = customtkinter.CTkLabel(
                assign_booking_frame, text="Ngày đặt: ", font=font720
            )
            date_lbl.place(x=30, y=150)

            date_txt = customtkinter.CTkEntry(
                assign_booking_frame, font=font720, width=200
            )
            date_txt.bind("<Button-1>", lambda e: "break")
            date_txt.bind("<Key>", lambda e: "break")
            date_txt.place(x=140, y=150)

            pickup_lbl = customtkinter.CTkLabel(
                assign_booking_frame, text="Giờ:", font=font720
            )
            pickup_lbl.place(x=30, y=200)

            def update_time2(time):
                pick_up_txt.delete(0, len(pick_up_txt.get()))
                pick_up_txt.insert(0, str("{}:{} {}".format(*time)))

            def time720():
                top = customtkinter.CTkToplevel(assign_booking_frame)
                top.title("Hệ thống đặt xe taxi")
                top.iconbitmap(
                    "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
                )
                top.resizable(0, 0)
                frame_width = 400
                frame_height = 500
                screen_width = top.winfo_screenwidth()
                screen_height = top.winfo_screenheight()
                x_cordinate = int((screen_width / 2) - (frame_width / 2))
                y_cordinate = int((screen_height / 2) - (frame_height / 2))
                top.geometry(
                    "{}x{}+{}+{}".format(
                        frame_width, frame_height, x_cordinate, y_cordinate
                    )
                )
                time_picker = AnalogPicker(top, type=constants.HOURS12)
                time_picker.pack(expand=True, fill="both")
                theme = AnalogThemes(time_picker)
                theme.setDracula()
                ok_btn = customtkinter.CTkButton(
                    master=top,
                    text="Ok",
                    command=lambda: update_time2(time_picker.time()),
                )
                ok_btn.pack()

            pick_up_txt = customtkinter.CTkEntry(
                assign_booking_frame, font=font720, width=200
            )
            pick_up_txt.bind("<Button-1>", lambda e: "break")
            pick_up_txt.bind("<Key>", lambda e: "break")
            pick_up_txt.place(x=140, y=200)

            time_img = customtkinter.CTkImage(
                light_image=Image.open(
                    "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/time-five-regular-24.png"
                )
            )
            pick_up_time_btn = customtkinter.CTkButton(
                assign_booking_frame,
                image=time_img,
                text="",
                fg_color="black",
                command=time720,
                font=font720,
                width=40,
            )
            pick_up_time_btn.place(x=350, y=202)

            drop_off_lbl = customtkinter.CTkLabel(
                assign_booking_frame, text="Điểm đến:", font=font720
            )
            drop_off_lbl.place(x=30, y=250)

            drop_off_txt = customtkinter.CTkEntry(
                assign_booking_frame, font=font720, width=200
            )
            drop_off_txt.bind("<Button-1>", lambda e: "break")
            drop_off_txt.bind("<Key>", lambda e: "break")
            drop_off_txt.place(x=140, y=250)

            driver_id_label = customtkinter.CTkLabel(
                assign_booking_frame, text="Mã tài xế:", font=font720
            )
            driver_id_label.place(x=30, y=300)

            driver_id_combo = customtkinter.CTkEntry(
                assign_booking_frame, font=font720, width=200
            )
            driver_id_combo.bind("<Button-1>", lambda e: "break")
            driver_id_combo.bind("<Key>", lambda e: "break")
            driver_id_combo.place(x=140, y=300)

            customerid = customtkinter.CTkEntry(assign_booking_frame)
            bookingid = customtkinter.CTkEntry(assign_booking_frame)

            def available_driver_gui():
                driver_gui = customtkinter.CTkToplevel()
                driver_gui.iconbitmap(
                    "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
                )
                driver_gui.title("Hệ thống đặt xe taxi")
                driver_gui.resizable(0, 0)
                frame_width = 400
                frame_height = 300
                screen_width = driver_gui.winfo_screenwidth()
                screen_height = driver_gui.winfo_screenheight()
                x_cordinate = int((screen_width / 2) - (frame_width / 2))
                y_cordinate = int((screen_height / 2) - (frame_height / 2))
                driver_gui.geometry(
                    "{}x{}+{}+{}".format(
                        frame_width, frame_height, x_cordinate + 200, y_cordinate
                    )
                )

                available_driver_table = ttk.Treeview(driver_gui)
                available_driver_table.pack(side=TOP, fill=BOTH, expand=TRUE)
                available_driver_table["columns"] = ("id", "name")
                available_driver_table.column("#0", width=0, stretch=0)
                available_driver_table.column("id", width=100, anchor=CENTER)
                available_driver_table.column("name", width=100, anchor=CENTER)

                available_driver_table.heading("#0", text="", anchor=CENTER)
                available_driver_table.heading("id", text="Mã tài xế", anchor=CENTER)
                available_driver_table.heading("name", text="Họ và tên", anchor=CENTER)

                def get_available_driver():

                    available_driver_result = available_driver()
                    i = 0
                    for driver in available_driver_result:
                        available_driver_table.insert(
                            parent="", index="end", values=(driver[0], driver[1])
                        )

                get_available_driver()

                def select_available_driver(a):
                    driver_id_combo.delete(0, END)
                    selectitem = available_driver_table.selection()[0]
                    driver_id_combo.insert(
                        0, available_driver_table.item(selectitem)["values"][0]
                    )

                available_driver_table.bind(
                    "<<TreeviewSelect>>", select_available_driver
                )

                root.mainloop()

            available_driver_btn = customtkinter.CTkButton(
                assign_booking_frame,
                command=available_driver_gui,
                text="Tài xế có sẵn",
                font=font720,
                width=150,
            )
            available_driver_btn.place(x=30, y=350)

            def cancel_booking():
                update_booking_result = cancel_status_booking_update(bookingid.get())
                if update_booking_result == True:
                    update_booking_result_lbl.configure(
                        text="Đặt xe đã được huỷ thành công"
                    )
                    booking_table_tree_view.delete(
                        *booking_table_tree_view.get_children()
                    )
                    booking_table()
                    booking_table_tree_view2.delete(
                        *booking_table_tree_view2.get_children()
                    )
                    booking_table_tree_view11()
                else:
                    update_booking_result_lbl.configure(text="Đã có lỗi xảy ra")

            available_driver_btn = customtkinter.CTkButton(
                assign_booking_frame,
                command=cancel_booking,
                text="Hủy đặt xe",
                font=font720,
                width=150,
            )
            available_driver_btn.place(x=100, y=390)

            update_booking_result_lbl = customtkinter.CTkLabel(
                assign_booking_frame, text="", font=font720
            )
            update_booking_result_lbl.place(x=50, y=430)

            assign_booking_frame2 = customtkinter.CTkFrame(
                master=root,
                width=1050,  # fg_color="#FFFFFF"
            )
            assign_booking_frame2.pack(side=LEFT, fill=BOTH, padx=(0, 10), pady=10)

            booking_table_tree_view = ttk.Treeview(assign_booking_frame2)
            booking_table_tree_view["columns"] = (
                "bookingid",
                "pickup",
                "date",
                "time",
                "dropoff",
                "status",
                "customerid",
                "driverid",
            )
            booking_table_tree_view.column("#0", width=0, stretch=0)
            booking_table_tree_view.column("bookingid", width=100, anchor=CENTER)
            booking_table_tree_view.column("pickup", width=230, anchor=CENTER)
            booking_table_tree_view.column("date", width=150, anchor=CENTER)
            booking_table_tree_view.column("time", width=150, anchor=CENTER)
            booking_table_tree_view.column("dropoff", width=230, anchor=CENTER)
            booking_table_tree_view.column("status", width=110, anchor=CENTER)
            booking_table_tree_view.column("customerid", width=180, anchor=CENTER)
            booking_table_tree_view.column("driverid", width=120, anchor=CENTER)

            booking_table_tree_view.heading("#0", text="", anchor=CENTER)
            booking_table_tree_view.heading(
                "bookingid", text="Mã đặt xe", anchor=CENTER
            )
            booking_table_tree_view.heading("pickup", text="Điểm đón", anchor=CENTER)
            booking_table_tree_view.heading("date", text="Ngày đặt", anchor=CENTER)
            booking_table_tree_view.heading("time", text="Giờ đặt", anchor=CENTER)
            booking_table_tree_view.heading("dropoff", text="Điểm đến", anchor=CENTER)
            booking_table_tree_view.heading("status", text="Trạng thái", anchor=CENTER)
            booking_table_tree_view.heading(
                "customerid", text="Mã khách hàng", anchor=CENTER
            )
            booking_table_tree_view.heading("driverid", text="Mã tài xế", anchor=CENTER)

            def booking_table():
                book_result = select_all()
                i = 0
                for ro in book_result:
                    booking_table_tree_view.insert(
                        parent="",
                        index="end",
                        values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]),
                    )
                    i = i + 1

            booking_table_tree_view.pack(padx=10, pady=10)

            def get_driver_detail(a):
                pick_up_address_txt.delete(0, END)
                date_txt.delete(0, END)
                pick_up_txt.delete(0, END)
                drop_off_txt.delete(0, END)
                customerid.delete(0, END)
                bookingid.delete(0, END)

                selectitem2 = booking_table_tree_view.selection()[0]

                pick_up_address_txt.insert(
                    0, booking_table_tree_view.item(selectitem2)["values"][1]
                )
                date_txt.insert(
                    0, booking_table_tree_view.item(selectitem2)["values"][2]
                )
                pick_up_txt.insert(
                    0, booking_table_tree_view.item(selectitem2)["values"][3]
                )
                drop_off_txt.insert(
                    0, booking_table_tree_view.item(selectitem2)["values"][4]
                )
                customerid.insert(
                    0, booking_table_tree_view.item(selectitem2)["values"][6]
                )
                bookingid.insert(
                    0, booking_table_tree_view.item(selectitem2)["values"][0]
                )

            booking_table_tree_view.bind("<<TreeviewSelect>>", get_driver_detail)

            def update_customer_booking():
                pick_up_address_txt.get()
                date_txt.get()
                pick_up_txt.get()
                drop_off_txt.get()
                customerid.get()
                driver_id_combo.get()
                bookingid.get()

                validate_result = validate_admin_booking()
                today = date.today()
                today720 = str(today)

                if bookingid.get() == "":
                    update_booking_result_lbl.configure(text="Bạn chưa chọn mã đặt xe")

                elif driver_id_combo.get() == "":
                    update_booking_result_lbl.configure(text="Vui lòng nhập mã tài xế")

                elif validate_result != None:
                    date3 = date_txt.get()
                    if date3 < today720:
                        update_booking_result_lbl.configure(
                            text="Ngày đón của khách hàng này đã hết hạn."
                        )

                    else:
                        update_booking_info = BookingLibs(
                            pickupaddress=pick_up_address_txt.get(),
                            date=date_txt.get(),
                            time=pick_up_txt.get(),
                            dropoffaddress=drop_off_txt.get(),
                            cid=customerid.get(),
                            bookingstatus="Đã phân công",
                            did=driver_id_combo.get(),
                            bookingid=bookingid.get(),
                        )
                        update_booking_result = update_booking(update_booking_info)

                        driver = DriverLibs(
                            did=driver_id_combo.get(), driverstatus="Đã phân công"
                        )
                        update_result = update_driver_status(driver)
                        if update_booking_result == True:
                            update_booking_result_lbl.configure(
                                text="Tài xế đã được phân công thành công"
                            )
                            booking_table_tree_view.delete(
                                *booking_table_tree_view.get_children()
                            )
                            booking_table()
                            booking_table_tree_view2.delete(
                                *booking_table_tree_view2.get_children()
                            )
                            booking_table_tree_view11()

                        else:
                            update_booking_result_lbl.configure(text="Đã có lỗi xảy ra")

            assign_btn = customtkinter.CTkButton(
                assign_booking_frame,
                command=update_customer_booking,
                text="Phân công tài xế",
                font=font720,
                width=150,
            )
            assign_btn.place(x=190, y=350)

            booking_table()
            root.mainloop()

        assign_driver_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/edit-alt-regular-24.png"
            )
        )
        assign_driver_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Phân công tài xế",
            command=assign_driver_gui,
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=assign_driver_btn_image,
            fg_color="#2b2b2b",
        )
        assign_driver_btn.place(x=40, y=200)

        def billing_gui():
            main = customtkinter.CTkToplevel()
            admin_payment.AdminPayment(main)
            main.mainloop()

        payment_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/paypal-logo-24.png"
            )
        )
        payment_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Hóa đơn",
            command=billing_gui,
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=payment_btn_image,
            fg_color="#2b2b2b",
        )
        payment_btn.place(x=40, y=400)

        def customer_management_gui():
            customer = customtkinter.CTkToplevel()
            customer_management.CustomerManagement(customer)
            customer.mainloop()

        manage_customers_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-regular-24.png"
            )
        )
        manage_customers_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Quản lý khách hàng",
            command=customer_management_gui,
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=manage_customers_btn_image,
            fg_color="#2b2b2b",
        )
        manage_customers_btn.place(x=40, y=300)

        def driver_management_gui():
            driver = customtkinter.CTkToplevel()
            driver_management.DriverManagement(driver)
            driver.mainloop()

        manage_drivers_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/car-regular-24.png"
            )
        )
        manage_drivers_btn = customtkinter.CTkButton(
            master=left_frame,
            command=driver_management_gui,
            text="Quản lý tài xế",
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=manage_drivers_btn_image,
            fg_color="#2b2b2b",
        )
        manage_drivers_btn.place(x=40, y=350)

        def active_booking_gui():
            root = customtkinter.CTkToplevel()
            active_booking.ActiveBooking(root)
            root.mainloop()

        view_customer_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/book-content-regular-24.png"
            )
        )
        view_customer_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Thông tin phân công",
            command=active_booking_gui,
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=view_customer_btn_image,
            fg_color="#2b2b2b",
        )
        view_customer_btn.place(x=40, y=250)

        def billing_history_gui():
            main = customtkinter.CTkToplevel()
            admin_billing_history.AdminBillingHistory(main)
            main.mainloop()

        view_driver_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/money-withdraw-regular-24.png"
            )
        )
        view_driver_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Lịch sử hóa đơn",
            command=billing_history_gui,
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=view_driver_btn_image,
            fg_color="#2b2b2b",
        )
        view_driver_btn.place(x=40, y=450)

        def logout():
            self.main.destroy()
            root = customtkinter.CTk()
            login.Login(root)
            root.mainloop()

        logout_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/log-out-circle-regular-24.png"
            )
        )
        logout_btn = customtkinter.CTkButton(
            master=left_frame,
            command=logout,
            text="Đăng xuất",
            fg_color="#2b2b2b",
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=logout_btn_image,
        )
        logout_btn.place(x=40, y=500)

        themelbl = customtkinter.CTkLabel(
            left_frame, text="Giao diện:", font=side_menu_font
        )
        themelbl.place(x=40, y=550)

        def combobox_callback(choice):
            customtkinter.set_appearance_mode(choice)
            if choice == "light":
                user_image_label["bg"] = "#dbdbdb"

                style1.configure(
                    "Treeview",
                    background="#dbdbdb",
                    fieldbackground="#dbdbdb",
                    foreground="black",
                )
                welcome_label.configure(fg_color="#dbdbdb")
                welcome_label.configure(text_color="#2b2b2b")

            if choice == "dark":
                user_image_label["bg"] = "#2b2b2b"

                welcome_label.configure(fg_color="#2b2b2b")
                welcome_label.configure(text_color="white")
                style1.configure(
                    "Treeview",
                    background="#2b2b2b",
                    fieldbackground="#2b2b2b",
                    foreground="white",
                )

        combobox = customtkinter.CTkComboBox(
            master=left_frame,
            values=["dark", "light"],
            command=combobox_callback,
            font=side_menu_font,
            width=200,
        )
        combobox.place(x=40, y=580)
        combobox.set("dark")  # set initi

        # +++++++++++++++++++++++++++++Center Frame+++++++++++++++++++++++++++++++++++++++
        frame_center = customtkinter.CTkFrame(
            master=self.main,
            width=1200,
            height=750,
            corner_radius=20,
        )
        frame_center.place(x=320, y=100)

        parent_tab = customtkinter.CTkTabview(frame_center, width=1170)
        parent_tab.place(x=15, y=10)

        parent_tab.add("Trang chủ")
        parent_tab.add("Tìm kiếm")
        parent_tab.add("Thống kê")

        # +++++++++++++++++++++++++++++++++++Home Tab 1 Frame++++++++++++++++++++++++++++++++++++
        frame1 = customtkinter.CTkFrame(
            master=parent_tab.tab("Trang chủ"), width=250, height=150, corner_radius=20
        )
        frame1.place(x=30, y=20)
        result = total_customer()
        tmp_result = result[0]
        frame1_label2 = customtkinter.CTkLabel(
            master=frame1,
            text="Tổng \nkhách hàng \n\n{}".format(tmp_result[0]),
            font=label_font,
        )
        frame1_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 2 Frame++++++++++++++++++++++++++++++++++++
        frame2 = customtkinter.CTkFrame(
            master=parent_tab.tab("Trang chủ"), width=250, height=150, corner_radius=20
        )
        frame2.place(x=310, y=20)
        booking_result = total_booking()
        booking_result2 = booking_result[0]
        frame2_label2 = customtkinter.CTkLabel(
            master=frame2,
            text="Tổng \nđặt xe taxi \n\n{}".format(booking_result2[0]),
            font=label_font,
        )
        frame2_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 3 Frame++++++++++++++++++++++++++++++++++++
        frame3 = customtkinter.CTkFrame(
            master=parent_tab.tab("Trang chủ"), width=250, height=150, corner_radius=20
        )
        frame3.place(x=590, y=20)
        driver_result = total_driver()
        driver_result2 = driver_result[0]
        frame3_label2 = customtkinter.CTkLabel(
            master=frame3,
            text="Tổng số \ntài xế \n\n{}".format(driver_result2[0]),
            font=label_font,
        )
        frame3_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 4 Frame++++++++++++++++++++++++++++++++++++
        frame4 = customtkinter.CTkFrame(
            master=parent_tab.tab("Trang chủ"), width=250, height=150, corner_radius=20
        )
        frame4.place(x=870, y=20)
        total_result = total_revenue()
        total_result2 = total_result[0]

        if total_result2 is not None and total_result2[0] is not None:
            # Định dạng tiền tệ: chuyển 1000000 -> "1.000.000 VND"
            formatted_amount = "{:,.0f} VND".format(total_result2[0]).replace(",", ".")
        else:
            formatted_amount = (
                "0 VND"  # Hoặc giá trị mặc định khác nếu total_result2[0] là None
            )

        frame4_label2 = customtkinter.CTkLabel(
            master=frame4,
            text=f"Tổng \ndoanh thu \n\n{formatted_amount}",
            font=label_font,
        )
        frame4_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Service Tab 1 Frame++++++++++++++++++++++++++++++++++++
        tab2_frame1 = customtkinter.CTkFrame(
            master=parent_tab.tab("Tìm kiếm"), width=250, height=150, corner_radius=20
        )
        tab2_frame1.place(x=310, y=20)

        def search_customers11():
            root = customtkinter.CTkToplevel()
            search_customers.SearchCustomer(root)
            root.mainloop()

        frame1_label1 = customtkinter.CTkButton(
            master=tab2_frame1,
            text="Tìm kiếm \nkhách hàng",
            command=search_customers11,
            font=label_font,
            fg_color="#2b2b2b",
        )
        frame1_label1.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Service Tab 2 Frame++++++++++++++++++++++++++++++++++++
        tab2_frame2 = customtkinter.CTkFrame(
            master=parent_tab.tab("Tìm kiếm"), width=250, height=150, corner_radius=20
        )
        tab2_frame2.place(x=620, y=20)

        def search_drivers11():
            root = customtkinter.CTkToplevel()
            search_drivers.SearchDrivers(root)
            root.mainloop()

        frame2_label2 = customtkinter.CTkButton(
            master=tab2_frame2,
            text="Tìm kiếm \nTài xế",
            command=search_drivers11,
            font=label_font,
            fg_color="#2b2b2b",
        )
        frame2_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Report Tab 1 Frame++++++++++++++++++++++++++++++++++++
        tab3_frame1 = customtkinter.CTkFrame(
            master=parent_tab.tab("Thống kê"), width=250, height=150, corner_radius=20
        )
        tab3_frame1.place(x=30, y=20)

        def customer_report720():
            root = customtkinter.CTkToplevel()
            customer_report.CustomerReport(root)
            root.mainloop()

        tab3_label1 = customtkinter.CTkButton(
            master=tab3_frame1,
            text="Thống kê \nkhách hàng",
            command=customer_report720,
            font=label_font,
            fg_color="#2b2b2b",
        )
        tab3_label1.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Report Tab 2 Frame++++++++++++++++++++++++++++++++++++
        tab3_frame2 = customtkinter.CTkFrame(
            master=parent_tab.tab("Thống kê"), width=250, height=150, corner_radius=20
        )
        tab3_frame2.place(x=310, y=20)

        def driver_report720():
            root = customtkinter.CTkToplevel()
            driver_report.DriverReport(root)
            root.mainloop()

        tab3_label2 = customtkinter.CTkButton(
            master=tab3_frame2,
            text="Thống kê \ntài xế",
            command=driver_report720,
            font=label_font,
            fg_color="#2b2b2b",
        )
        tab3_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Report Tab 3 Frame++++++++++++++++++++++++++++++++++++
        tab3_frame3 = customtkinter.CTkFrame(
            master=parent_tab.tab("Thống kê"), width=250, height=150, corner_radius=20
        )
        tab3_frame3.place(x=590, y=20)

        def booking_report720():
            root = customtkinter.CTkToplevel()
            booking_report.BookingReport(root)
            root.mainloop()

        tab3_label3 = customtkinter.CTkButton(
            master=tab3_frame3,
            text="Thống kê \nđặt xe",
            command=booking_report720,
            font=label_font,
            fg_color="#2b2b2b",
        )
        tab3_label3.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Report Tab 4 Frame++++++++++++++++++++++++++++++++++++
        tab4_frame4 = customtkinter.CTkFrame(
            master=parent_tab.tab("Thống kê"), width=250, height=150, corner_radius=20
        )
        tab4_frame4.place(x=870, y=20)

        def billing_report720():
            root = customtkinter.CTkToplevel()
            billing_report.BillingReport(root)
            root.mainloop()

        tab4_label4 = customtkinter.CTkButton(
            master=tab4_frame4,
            command=billing_report720,
            text="Thống kê \ndoanh thu",
            font=label_font,
            fg_color="#2b2b2b",
        )
        tab4_label4.place(relx=0.5, rely=0.5, anchor=CENTER)

        style1 = ttk.Style()
        style1.theme_use("default")
        style1.configure(
            "Treeview",
            background="#2b2b2b",
            foreground="white",
            rowheight=25,
            fieldbackground="#2b2b2b",
            bordercolor="#343638",
            borderwidth=0,
            font=("Times New Roman", 16),
        )
        style1.map("Treeview", background=[("selected", "#22559b")])

        style1.configure(
            "Treeview.Heading",
            background="#565b5e",
            foreground="white",
            relief="flat",
            font=("Times New Roman", 17),
        )
        style1.map(
            "Treeview.Heading",
            background=[("active", "#3484F0")],
        )

        booking_table_tree_view2 = ttk.Treeview(frame_center)
        booking_table_tree_view2["columns"] = (
            "bookingid",
            "pickup",
            "date",
            "time",
            "dropoff",
            "kilomet",
            "status",
            "customerid",
            "driverid",
        )
        booking_table_tree_view2.column("#0", width=0, stretch=0)
        booking_table_tree_view2.column("bookingid", width=100, anchor=CENTER)
        booking_table_tree_view2.column("pickup", width=235, anchor=CENTER)
        booking_table_tree_view2.column("date", width=150, anchor=CENTER)
        booking_table_tree_view2.column("time", width=150, anchor=CENTER)
        booking_table_tree_view2.column("dropoff", width=235, anchor=CENTER)
        booking_table_tree_view2.column("kilomet", width=150, anchor=CENTER)
        booking_table_tree_view2.column("status", width=180, anchor=CENTER)
        booking_table_tree_view2.column("customerid", width=100, anchor=CENTER)
        booking_table_tree_view2.column("driverid", width=150, anchor=CENTER)

        booking_table_tree_view2.heading("#0", text="", anchor=CENTER)
        booking_table_tree_view2.heading("bookingid", text="Mã đặt xe", anchor=CENTER)
        booking_table_tree_view2.heading("pickup", text="Điểm đón", anchor=CENTER)
        booking_table_tree_view2.heading("date", text="Ngày đặt", anchor=CENTER)
        booking_table_tree_view2.heading("time", text="Giờ đặt", anchor=CENTER)
        booking_table_tree_view2.heading("dropoff", text="Điểm đến", anchor=CENTER)
        booking_table_tree_view2.heading("kilomet", text="Cây số", anchor=CENTER)
        booking_table_tree_view2.heading("status", text="Trạng thái", anchor=CENTER)
        booking_table_tree_view2.heading("customerid", text="Mã KH", anchor=CENTER)
        booking_table_tree_view2.heading("driverid", text="Mã tài xế", anchor=CENTER)

        def booking_table_tree_view11():
            book_result = select_all()
            i = 0
            for ro in book_result:
                booking_table_tree_view2.insert(
                    parent="",
                    index="end",
                    values=(
                        ro[0],
                        ro[1],
                        ro[2],
                        ro[3],
                        ro[4],
                        ro[8],
                        ro[5],
                        ro[6],
                        ro[7],
                    ),
                )
                i = i + 1

        booking_table_tree_view11()
        booking_table_tree_view2.place(x=15, y=360)


if __name__ == "__main__":
    main = customtkinter.CTk()
    AdminDashboard(main)
    main.mainloop()
