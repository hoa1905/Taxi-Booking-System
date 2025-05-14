from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from time import strftime
from tkinter import ttk, messagebox
from customer import login
from dbms.booking_backend import driver_update_booking
from dbms.driver_backend import (
    driver_riding_total,
    driver_total_booked,
    driver_ride_completed,
    driver_ride_cancelled,
)
from dbms.driver_management import (
    update_driver_status,
    driver_select_all,
    driver_select_all_booking,
    driver_password_change,
)
from driver import driver_profile, driver_trip_history
from libs import Global
from libs.booking_libs import BookingLibs
from libs.driver_libs import DriverLibs


class DriverDashboard:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        self.main.title(
            "Dashboard Tài xế | Xin chào {}".format(Global.current_driver[1])
        )
        self.main.screen_width = main.winfo_screenwidth()
        self.main.screen_height = main.winfo_screenheight()

        # Đặt kích thước và vị trí cửa sổ tại (0, 0)
        self.main.geometry(f"{self.main.screen_width}x{self.main.screen_height}+0+0")

        self.main.bind("<Escape>", lambda e: main.destroy())
        self.main.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )

        # ++++++++++++++++++++++++++++++++Font Collection+++++++++++++++++++++++++++++++++++++++++++
        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )
        label_font = customtkinter.CTkFont(
            family="Times New Roman", size=22, weight="normal"
        )
        side_menu_font = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )

        driver_id = Entry(self.main)
        driver_id.insert(0, Global.current_driver[0])

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

        # ++++++++++++++++++++++++++++TOP FRAME+++++++++++++++++++++++++++++++++++
        top_frame = customtkinter.CTkFrame(self.main, height=80)
        top_frame.pack(side=TOP, fill=BOTH)

        # +++++++++++++++++++++++++++Top Label++++++++++++++++++++++++++=
        welcome_lbl = customtkinter.CTkLabel(
            master=self.main,
            text="Dashboard Tài xế",
            fg_color="#2b2b2b",
            font=("Times New Roman", 25, "bold"),
        )
        welcome_lbl.place(x=100, y=25)

        def logout():
            self.main.destroy()
            main = customtkinter.CTk()
            login.Login(main)
            main.mainloop()

        # +++++++++++++++++++++++++++++++++++Welcome Label++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        welcome_label = customtkinter.CTkLabel(
            master=self.main,
            text="Xin chào {}".format(Global.current_driver[1]),
            font=("Times New Roman", 30, "bold"),
            text_color="white",
            fg_color="#2b2b2b",
        )
        welcome_label.place(x=1290, y=25)

        # ++++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++
        left_frame = customtkinter.CTkFrame(self.main, width=300)
        left_frame.pack(side=LEFT, fill=BOTH, padx=(10, 0), pady=10)

        cover_image = Image.open(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-solid-120.png"
        )
        photo1 = ImageTk.PhotoImage(cover_image)
        cover_mage_label = Label(left_frame, image=photo1, bg="#2a2d2e")
        cover_mage_label.image = photo1
        cover_mage_label.place(x=100, y=40)

        def trip_update_gui():
            root = customtkinter.CTkToplevel()
            root.title("Hệ thống đặt xe taxi")
            width = 1500
            height = 450
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

            trip_update_left_frame = customtkinter.CTkFrame(
                root, width=400, corner_radius=20
            )
            trip_update_left_frame.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

            title11_lbl = customtkinter.CTkLabel(
                master=trip_update_left_frame,
                text="Cập nhật chuyến đi",
                font=font720,
            )
            title11_lbl.place(x=110, y=20)

            bookingid_lbl = customtkinter.CTkLabel(
                trip_update_left_frame, text="Mã đặt xe: ", font=font720
            )
            bookingid_lbl.place(x=30, y=100)

            booking_id_txt = customtkinter.CTkEntry(
                trip_update_left_frame, font=font720, width=200
            )
            booking_id_txt.place(x=140, y=100)

            date_lbl = customtkinter.CTkLabel(
                trip_update_left_frame, text="Ngày đặt: ", font=font720
            )
            date_lbl.place(x=30, y=150)

            date_txt = customtkinter.CTkEntry(
                trip_update_left_frame, font=font720, width=200
            )
            date_txt.place(x=140, y=150)

            name_lbl = customtkinter.CTkLabel(
                trip_update_left_frame, text="Khách hàng:", font=font720
            )
            name_lbl.place(x=30, y=200)

            name_txt = customtkinter.CTkEntry(
                trip_update_left_frame, font=font720, width=200
            )
            name_txt.place(x=140, y=200)

            status_lbl = customtkinter.CTkLabel(
                trip_update_left_frame, text="Trạng thái:", font=font720
            )
            status_lbl.place(x=30, y=250)

            combo_data = ("Hoàn thành", "Chưa hoàn thành")
            booking_combo = customtkinter.CTkComboBox(
                trip_update_left_frame, values=combo_data, font=font720, width=200
            )
            booking_combo.place(x=140, y=250)

            update_booking_result_lbl = customtkinter.CTkLabel(
                trip_update_left_frame, text="", font=font720
            )
            update_booking_result_lbl.place(x=80, y=390)

            trip_update_right_frame = customtkinter.CTkFrame(
                root,
                width=1300,
            )
            trip_update_right_frame.pack(
                side=LEFT, fill=BOTH, expand=True, padx=(0, 10), pady=10
            )

            booking_table = ttk.Treeview(trip_update_right_frame)
            booking_table["columns"] = (
                "bookingid",
                "pickupaddress",
                "date",
                "time",
                "dropoffaddress",
                "kilomet",
                "price",
                "name",
                "bookingstatus",
            )
            booking_table.column("#0", width=0, stretch=0)
            booking_table.column("bookingid", width=100, anchor=CENTER)
            booking_table.column("pickupaddress", width=200, anchor=CENTER)
            booking_table.column("date", width=80, anchor=CENTER)
            booking_table.column("time", width=80, anchor=CENTER)
            booking_table.column("dropoffaddress", width=200, anchor=CENTER)
            booking_table.column("kilomet", width=100, anchor=CENTER)
            booking_table.column("price", width=150, anchor=CENTER)
            booking_table.column("name", width=150, anchor=CENTER)
            booking_table.column("bookingstatus", width=150, anchor=CENTER)

            booking_table.heading("#0", text="", anchor=CENTER)
            booking_table.heading("bookingid", text="Mã đặt xe", anchor=CENTER)
            booking_table.heading("pickupaddress", text="Điểm đón", anchor=CENTER)
            booking_table.heading("date", text="Ngày đặt", anchor=CENTER)
            booking_table.heading("time", text="Giờ đặt", anchor=CENTER)
            booking_table.heading("dropoffaddress", text="Điểm đến", anchor=CENTER)
            booking_table.heading("kilomet", text="Cây số", anchor=CENTER)
            booking_table.heading("price", text="Số tiền", anchor=CENTER)
            booking_table.heading("name", text="Khách hàng", anchor=CENTER)
            booking_table.heading("bookingstatus", text="Trạng thái", anchor=CENTER)

            def show_booking_table():
                id = driver_id.get()
                driver_result = driver_select_all_booking(id)
                for x in driver_result:
                    try:
                        kilometer = float(x[7])  # cột số 7 là kilomet
                        price = int(kilometer * 12000)
                        price_str = f"{price:,.0f}".replace(",", ".") + " VND"
                    except:
                        price_str = "0" + " VND"

                    booking_table.insert(
                        parent="",
                        index="end",
                        values=(
                            x[0],
                            x[1],
                            x[2],
                            x[3],
                            x[4],
                            x[7],
                            price_str,
                            x[5],
                            x[6],
                        ),
                    )

            booking_table.pack(fill=BOTH, expand=True, padx=10, pady=10)

            def get_driver_detail(a):
                booking_id_txt.delete(0, END)
                date_txt.delete(0, END)
                name_txt.delete(0, END)

                select_item2 = booking_table.selection()[0]

                booking_id_txt.insert(0, booking_table.item(select_item2)["values"][0])
                date_txt.insert(0, booking_table.item(select_item2)["values"][2])
                name_txt.insert(0, booking_table.item(select_item2)["values"][7])

            booking_table.bind("<<TreeviewSelect>>", get_driver_detail)

            def update_customer_booking():
                booking_id_txt.get()
                date_txt.get()
                name_txt.get()
                driver_id.get()

                update_booking = BookingLibs(
                    bookingstatus="Chưa thanh toán", bookingid=booking_id_txt.get()
                )
                update_booking_result = driver_update_booking(update_booking)

                driver = DriverLibs(did=driver_id.get(), driverstatus="Hoạt động")
                update_result = update_driver_status(driver)

                if update_booking_result == True:
                    update_booking_result_lbl.configure(
                        text="Chuyến đi {}".format(booking_combo.get())
                    )
                    driver_ride_cancelled(driver_id.get())
                    driver_ride_completed(driver_id.get())
                    driver_total_booked(driver_id.get())
                    driver_riding_total(driver_id.get())
                    booking_table.delete(*booking_table.get_children())
                    show_booking_table()
                    treeView.delete(*treeView.get_children())
                    show_booking()
                    switch2()

                else:
                    update_booking_result_lbl.configure(text="Đã có lỗi xảy ra")

            assign_btn = customtkinter.CTkButton(
                trip_update_left_frame,
                command=update_customer_booking,
                text="Cập nhật",
                font=font720,
                width=150,
            )
            assign_btn.place(x=150, y=330)

            show_booking_table()
            root.mainloop()

        completetrip_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/edit-alt-regular-24.png"
            )
        )
        completetrip_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Cập nhật chuyến đi",
            command=trip_update_gui,
            hover_color="black",
            font=side_menu_font,
            width=200,
            image=completetrip_image,
            fg_color="#2b2b2b",
            anchor="w",
        )
        completetrip_btn.place(x=40, y=250)

        def trip_history_gui():
            root = customtkinter.CTkToplevel()
            driver_trip_history.DriverHistory(root)
            root.mainloop()

        trip_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-regular-24.png"
            )
        )
        trip_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Lịch sử chuyến đi",
            command=trip_history_gui,
            hover_color="black",
            font=side_menu_font,
            width=200,
            image=trip_image,
            fg_color="#2b2b2b",
            anchor="w",
        )
        trip_btn.place(x=40, y=300)

        def my_profile():
            root = customtkinter.CTkToplevel()
            driver_profile.DriverProfile(root)
            root.mainloop()

        profile_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-account-solid-24.png"
            )
        )
        profile_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Hồ sơ cá nhân",
            command=my_profile,
            hover_color="black",
            font=side_menu_font,
            width=200,
            image=profile_image,
            fg_color="#2b2b2b",
            anchor="w",
        )
        profile_btn.place(x=40, y=350)

        def change_password_gui():
            password = customtkinter.CTkToplevel()
            password.title("Hệ thống đặt xe taxi | Đổi mật khẩu")
            password.iconbitmap(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
            )
            frame_width = 530
            frame_height = 400
            password.resizable(0, 0)
            screen_width = password.winfo_screenwidth()
            screen_height = password.winfo_screenheight()
            x_cordinate = int((screen_width / 2) - (frame_width / 2))
            y_cordinate = int((screen_height / 2) - (frame_height / 2))
            password.geometry(
                "{}x{}+{}+{}".format(
                    frame_width, frame_height, x_cordinate + 70, y_cordinate - 70
                )
            )

            frame = customtkinter.CTkFrame(password)
            frame.pack(fill=BOTH, expand=TRUE)

            font720 = customtkinter.CTkFont(
                family="Times New Roman", size=20, weight="normal"
            )

            img = ImageTk.PhotoImage(
                Image.open(
                    "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-solid-72.png"
                )
            )
            image_label = Label(password, image=img, bg="#2b2b2b")
            image_label.image = img
            image_label.place(x=200, y=40)

            title_lbl = customtkinter.CTkLabel(
                master=password,
                text="Đổi mật khẩu",
                font=font720,
                bg_color="#2b2b2b",
            )
            title_lbl.place(x=250, y=40)

            currentpw_lbl = customtkinter.CTkLabel(
                master=password, text="Mật khẩu mới: ", font=font720, bg_color="#2b2b2b"
            )
            currentpw_lbl.place(x=40, y=150)

            currentpw_txt = customtkinter.CTkEntry(
                master=password, font=font720, show="*", width=200
            )
            currentpw_txt.place(x=260, y=150)

            confirmpw_lbl = customtkinter.CTkLabel(
                master=password,
                text="Nhập lại mật khẩu mới: ",
                font=font720,
                bg_color="#2b2b2b",
            )
            confirmpw_lbl.place(x=40, y=220)

            conformpw_txt = customtkinter.CTkEntry(
                master=password, show="*", font=font720, width=200
            )
            conformpw_txt.place(x=260, y=220)

            def show_password():
                if i.get() == 1:
                    conformpw_txt.configure(show="")
                    currentpw_txt.configure(show="")
                else:
                    conformpw_txt.configure(show="*")
                    currentpw_txt.configure(show="*")

            i = customtkinter.IntVar()

            password_show = customtkinter.CTkCheckBox(
                password,
                text="Hiện mật khẩu",
                variable=i,
                command=show_password,
                bg_color="#2b2b2b",
            )
            password_show.place(x=260, y=260)

            idtxt = Entry(password)
            idtxt.insert(0, "{}".format(Global.current_driver[0]))

            def change_password():
                id = idtxt.get()
                password1 = currentpw_txt.get()
                new_password = conformpw_txt.get()

                if password1 == new_password:
                    password720 = DriverLibs(did=id, password=new_password)
                    change_password_result = driver_password_change(password720)

                    if change_password_result == True:
                        messagebox.showinfo(
                            "Hệ thống đặt xe taxi",
                            "Đổi mật khẩu thành công",
                        )
                        self.main.destroy()
                        root = customtkinter.CTk()
                        login.Login(root)
                        root.mainloop()
                    else:
                        messagebox.showerror(
                            "Hệ thống đặt xe taxi", "Đã có lỗi xảy ra!"
                        )

                else:
                    messagebox.showerror(
                        "Hệ thống đặt xe taxi",
                        "Mật khẩu mới không khớp với mật khẩu mới!",
                    )
                    password.destroy()

            confirm_btn = customtkinter.CTkButton(
                master=password,
                command=change_password,
                text="Đổi mật khẩu",
                font=font720,
            )
            confirm_btn.place(x=260, y=310)

        change_password_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/\key-solid-24.png"
            )
        )
        password_change_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Đổi mật khẩu",
            command=change_password_gui,
            hover_color="black",
            font=side_menu_font,
            width=200,
            image=change_password_image,
            fg_color="#2b2b2b",
            anchor="w",
        )
        password_change_btn.place(x=40, y=400)

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
            image=logout_btn_image,
            anchor="w",
        )
        logout_btn.place(x=40, y=450)

        def switch():
            global is_on

            if is_on:
                toggle_button.config(image=off)
                is_on = False
                driver_idd = driver_id.get()
                driver_info = DriverLibs(did=driver_idd, driverstatus="Không hoạt động")
                update_result = update_driver_status(driver_info)
                if update_result == True:
                    toggle_label.configure(
                        text="{} không hoạt động".format(Global.current_driver[1])
                    )

            else:
                toggle_button.config(image=on)
                is_on = True
                driver_idd = driver_id.get()
                driver_info = DriverLibs(did=driver_idd, driverstatus="Hoạt động")
                update_result = update_driver_status(driver_info)
                if update_result == True:
                    toggle_label.configure(
                        text="{} đang hoạt động".format(Global.current_driver[1])
                    )

        on = ImageTk.PhotoImage(
            Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/left.png"
            )
        )
        off = ImageTk.PhotoImage(
            Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/right.png"
            )
        )

        toggle_button = Button(
            left_frame,
            bg="#2a2d2e",
            image=on,
            bd=0,
            command=switch,
            activebackground="#2a2d2e",
        )
        toggle_button.place(x=140, y=650)

        toggle_label = customtkinter.CTkLabel(left_frame, text="", font=side_menu_font)
        toggle_label.place(x=45, y=560)

        def my_time():

            time_string = strftime("%I:%M:%S %p")  # time format
            l1.configure(text=time_string)
            l1.after(1000, my_time)  # time delay of 1000 milliseconds

        l1 = customtkinter.CTkLabel(master=left_frame, font=side_menu_font)
        l1.place(x=90, y=150)
        my_time()

        global is_on
        is_on = True

        # Define our switch function
        def switch2():
            global is_on
            driver_id1 = driver_id.get()
            select_result = driver_select_all(driver_id1)
            if select_result != None:
                if select_result[6] == "Hoạt động":
                    toggle_button.config(image=on)
                    toggle_label.configure(
                        text="{} đang hoạt động".format(Global.current_driver[1])
                    )
                elif select_result[6] == "Không hoạt động":
                    toggle_button.config(image=off)
                    toggle_label.configure(
                        text="{} không hoạt động".format(Global.current_driver[1])
                    )

                elif select_result[6] == "Đã phân công":
                    toggle_button.config(image=off)
                    toggle_label.configure(
                        text="{} đã đặt xe".format(Global.current_driver[1])
                    )

            else:
                pass

        switch2()

        themelbl = customtkinter.CTkLabel(
            left_frame, text="Giao diện:", font=side_menu_font
        )
        themelbl.place(x=50, y=600)

        def combobox_callback(choice):
            customtkinter.set_appearance_mode(choice)
            if choice == "light":
                cover_mage_label["bg"] = "#dbdbdb"
                toggle_button["bg"] = "#dbdbdb"
                style1.configure(
                    "Treeview",
                    background="#dbdbdb",
                    fieldbackground="#dbdbdb",
                    foreground="black",
                )
                welcome_label.configure(fg_color="#dbdbdb")
                welcome_label.configure(text_color="#2b2b2b")
                welcome_lbl.configure(fg_color="#dbdbdb")
            if choice == "dark":
                cover_mage_label["bg"] = "#2b2b2b"
                toggle_button["bg"] = "#2b2b2b"
                welcome_label.configure(fg_color="#2b2b2b")
                welcome_label.configure(text_color="white")
                style1.configure(
                    "Treeview",
                    background="#2b2b2b",
                    fieldbackground="#2b2b2b",
                    foreground="white",
                )
                welcome_lbl.configure(fg_color="#2b2b2b")

        combobox = customtkinter.CTkComboBox(
            master=left_frame,
            values=["dark", "light"],
            command=combobox_callback,
            font=side_menu_font,
        )
        combobox.place(x=55, y=640)
        combobox.set("dark")

        # ++++++++++++++++++++++++++++Top Frame++++++++++++++++++++++++++++++++++++++++++++++
        center_frame = customtkinter.CTkFrame(master=self.main, corner_radius=20)
        center_frame.pack(side=TOP, fill=BOTH, expand=TRUE, padx=10, pady=10)

        # +++++++++++++++++++++++++++++++++++Home Tab 1 Frame++++++++++++++++++++++++++++++++++++
        frame1 = customtkinter.CTkFrame(
            master=center_frame, width=250, height=150, corner_radius=20
        )
        frame1.place(x=30, y=20)
        driver_idd = driver_id.get()
        result = driver_riding_total(driver_idd)
        tmpResult = result[0]
        frame1_label2 = customtkinter.CTkLabel(
            master=frame1,
            text="Tổng số \nchuyến xe \n\n{}".format(tmpResult[0]),
            font=label_font,
        )
        frame1_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 2 Frame++++++++++++++++++++++++++++++++++++
        frame2 = customtkinter.CTkFrame(
            master=center_frame, width=250, height=150, corner_radius=20
        )
        frame2.place(x=310, y=20)
        booking_result = driver_total_booked(driver_id.get())
        booking_result2 = booking_result[0]
        frame2_label2 = customtkinter.CTkLabel(
            master=frame2,
            text="Tổng số \nđặt xe \n\n{}".format(booking_result2[0]),
            font=label_font,
        )
        frame2_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 3 Frame++++++++++++++++++++++++++++++++++++
        frame3 = customtkinter.CTkFrame(
            master=center_frame, width=250, height=150, corner_radius=20
        )
        frame3.place(x=590, y=20)
        driver_result = driver_ride_completed(driver_id.get())
        drive_result2 = driver_result[0]
        frame3_label2 = customtkinter.CTkLabel(
            master=frame3,
            text="Chuyến xe \nhoàn thành \n\n{}".format(drive_result2[0]),
            font=label_font,
        )
        frame3_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # +++++++++++++++++++++++++++++++++++Home Tab 4 Frame++++++++++++++++++++++++++++++++++++
        frame4 = customtkinter.CTkFrame(
            master=center_frame, width=250, height=150, corner_radius=20
        )
        frame4.place(x=870, y=20)
        employees_result = driver_ride_cancelled(driver_id.get())
        employees_result2 = employees_result[0]
        frame4_label2 = customtkinter.CTkLabel(
            master=frame4,
            text="Chuyến xe \nbị hủy \n\n{}".format(employees_result2[0]),
            font=label_font,
        )
        frame4_label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Treeview
        treeView = ttk.Treeview(center_frame)
        treeView.place(x=10, y=250, width=1450, height=600)

        treeView["columns"] = (
            "bookingid",
            "pickupaddress",
            "date",
            "time",
            "dropoffaddress",
            "kilomet",
            "price",
            "name",
            "bookingstatus",
        )
        treeView.column("#0", width=0, stretch=0)
        treeView.column("bookingid", width=100, anchor=CENTER)
        treeView.column("pickupaddress", width=100, anchor=CENTER)
        treeView.column("date", width=100, anchor=CENTER)
        treeView.column("time", width=100, anchor=CENTER)
        treeView.column("dropoffaddress", width=100, anchor=CENTER)
        treeView.column("kilomet", width=100, anchor=CENTER)
        treeView.column("price", width=100, anchor=CENTER)
        treeView.column("name", width=100, anchor=CENTER)
        treeView.column("bookingstatus", width=100, anchor=CENTER)

        treeView.heading("#0", text="", anchor=CENTER)
        treeView.heading("bookingid", text="Mã đặt xe", anchor=CENTER)
        treeView.heading("pickupaddress", text="Điểm đón", anchor=CENTER)
        treeView.heading("date", text="Ngày đặt", anchor=CENTER)
        treeView.heading("time", text="Giờ đặt", anchor=CENTER)
        treeView.heading("dropoffaddress", text="Điểm đến", anchor=CENTER)
        treeView.heading("kilomet", text="Cây số", anchor=CENTER)
        treeView.heading("price", text="Số tiền", anchor=CENTER)
        treeView.heading("name", text="Tên khách hàng", anchor=CENTER)
        treeView.heading("bookingstatus", text="Trạng thái", anchor=CENTER)

        def show_booking():
            id = driver_id.get()
            driver_result = driver_select_all_booking(id)
            for x in driver_result:
                try:
                    kilometer = float(x[7])  # cột số 7 là kilomet
                    price = int(kilometer * 12000)
                    price_str = f"{price:,.0f}".replace(",", ".") + " VND"
                except:
                    price_str = "0" + " VND"
                treeView.insert(
                    parent="",
                    index="end",
                    values=(x[0], x[1], x[2], x[3], x[4], x[7], price_str, x[5], x[6]),
                )

        show_booking()


if __name__ == "__main__":
    main = customtkinter.CTk()
    DriverDashboard(main)
    main.mainloop()
