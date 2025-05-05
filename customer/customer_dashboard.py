from tkinter import *
import customtkinter
from datetime import date, datetime
from tkinter import ttk
from datetime import date
import datetime
from time import strftime
from geopy.geocoders import Nominatim
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
import pandas
from tkintermapview import TkinterMapView
from tkcalendar import DateEntry
from tktimepicker import AnalogPicker, AnalogThemes, constants
from billing import customer_billing_history
from customer import (
    customer_booking_history,
    view_profile,
)
from dbms.booking_backend import (
    insert_booking,
    customer_booking_select_all,
    customer_booking_select_status_booked,
    update_customer_booking1,
    delete_booking,
    customer_check_booking,
)
from dbms.customer_backend import validate_customer_booking
from dbms.customer_management import delete_record
from dbms.password_change_backend import password_change
from driver import driver_history
from libs import Global
from libs.booking_libs import BookingLibs
from tkinter import messagebox
from sqlalchemy import create_engine
from libs.customer_libs import CustomerLibs
from . import login

# Biến toàn cục lưu marker và polyline
pick_up_marker = None
drop_off_marker = None
route_line = None


class CustomerDashboard(customtkinter.CTk):

    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.root.screen_width = root.winfo_screenwidth()
        self.root.screen_height = root.winfo_screenheight()
        self.root.geometry(f"{self.root.screen_width}x{self.root.screen_height}+0+0")
        self.root.title("Dashboard khách hàng | Hệ thống đặt xe taxi")
        self.root.bind("<Escape>", lambda e: root.destroy())
        self.root.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )

        # ++++++++++++++++++++++++++++++Menu+++++++++++++++++++++++++++++++=
        parent_menu = Menu(self.root)

        # -------------------------Exit function-----------------------
        def exit():
            self.root.destroy()

        # ------------------------Logout function--------------------------
        def logout():
            self.root.destroy()
            root = customtkinter.CTk()
            login2 = login.Login(root)
            root.mainloop()

        file = Menu(parent_menu, tearoff=0)
        file.add_command(label="Mở")
        file.add_command(label="Đăng xuất", command=logout)
        file.add_command(label="Thoát", command=exit)

        parent_menu.add_cascade(label="File", menu=file)
        self.root.config(menu=parent_menu)

        # ++++++++++++++++++++++++++++++++Font Collection+++++++++++++++++++++++++++++++++++++++++++
        title_font = customtkinter.CTkFont(
            family="Times New Roman", size=30, weight="bold"
        )
        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )
        label_font = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )
        side_menu_font = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )

        # +++++++++++++++++++++++++++++Getting customer id using global++++++++++++++++++++++++++++
        customerid = customtkinter.CTkEntry(master=self.root)
        customerid.insert(0, Global.current_user[0])

        # ++++++++++++++++++++++++++++++++Top Frame+++++++++++++++++++++++++++++++++++
        top_frame = customtkinter.CTkFrame(master=self.root, height=100)
        top_frame.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        # -----------------------------Title Label-----------------------------------------
        title_lbl = customtkinter.CTkLabel(
            master=top_frame, text="HỆ THỐNG ĐẶT XE TAXI", font=title_font
        )
        title_lbl.pack(side=LEFT, pady=20, padx=10)

        # -------------------------------------Welcome Label----------------------------------
        log_name_lbl = customtkinter.CTkLabel(
            master=top_frame,
            text="Xin chào: {}".format(Global.current_user[1]),
            font=title_font,
        )
        log_name_lbl.pack(side=RIGHT, pady=20, padx=10)

        # +++++++++++++++++++++++++++++++Left Frame+++++++++++++++++++++++++++++++++++++++
        left_frame = customtkinter.CTkFrame(master=self.root, width=300)
        left_frame.pack(side=LEFT, fill=BOTH, padx=(10, 0), pady=10)

        cover_image = Image.open(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-solid-120.png"
        )
        photo1 = ImageTk.PhotoImage(cover_image)
        cover_image_label = Label(left_frame, image=photo1, bg="#2a2d2e")
        cover_image_label.image = photo1
        cover_image_label.place(x=100, y=40)

        def my_time():
            time_string = strftime("%I:%M:%S %p")  # time format
            l1.configure(text=time_string)
            l1.after(1000, my_time)  # time delay of 1000 milliseconds

        l1 = customtkinter.CTkLabel(master=left_frame, font=font720)
        l1.place(x=90, y=150)
        my_time()

        # ------------------------------Dashboard button-----------------------------------------
        assign_driver_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/edit-alt-regular-24.png"
            )
        )
        assign_driver_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Dashboard",
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=assign_driver_btn_image,
            fg_color="#2b2b2b",
        )
        assign_driver_btn.place(x=50, y=200)

        # ---------------------------Open profile function----------------------------
        def open_view_profile():
            main = customtkinter.CTkToplevel()
            view_profile.ViewCustomerProfile(main)
            main.mainloop()

        # -----------------------------My Profile Button------------------------------------------
        profile_img = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-account-solid-24.png"
            )
        )
        profile_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Hồ sơ cá nhân",
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            command=open_view_profile,
            image=profile_img,
            fg_color="#2b2b2b",
        )
        profile_btn.place(x=50, y=250)

        # -----------------------------Booking History Function------------------------------------------
        def open_customer_booking_history():
            main = customtkinter.CTkToplevel()
            customer_booking_history.CustomerBookingHistory(main)
            main.mainloop()

        # -----------------------------Booking History Button------------------------------------------
        manage_customers_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-regular-24.png"
            )
        )
        manage_customers_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Lịch sử đặt xe",
            command=open_customer_booking_history,
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=manage_customers_btn_image,
            fg_color="#2b2b2b",
        )
        manage_customers_btn.place(x=50, y=300)

        # -----------------------------Driver History Function------------------------------------------
        def driver_history_720():
            root = customtkinter.CTkToplevel()
            driver_history.DriverHistory(root)
            root.mainloop()

        # -----------------------------Driver History Button------------------------------------------
        manage_drivers_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/car-regular-24.png"
            )
        )
        manage_drivers_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Lịch sử tài xế",
            command=driver_history_720,
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=manage_drivers_btn_image,
            fg_color="#2b2b2b",
        )
        manage_drivers_btn.place(x=50, y=350)

        # -----------------------------Billing History Function------------------------------------------
        def customer_billing_history_gui():
            main = customtkinter.CTkToplevel()
            customer_billing_history.CustomerBillingHistory(main)
            main.mainloop()

        # -----------------------------Billing Button------------------------------------------
        billing_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/id-card-regular-24.png"
            )
        )
        billing_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Hóa đơn",
            command=customer_billing_history_gui,
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=billing_btn_image,
            fg_color="#2b2b2b",
        )
        billing_btn.place(x=50, y=400)

        # -----------------------------Change password toplevel gui------------------------------------------
        def change_password_gui():
            password = customtkinter.CTkToplevel()
            password.title("Hệ thống đặt xe taxi | Đổi mật khẩu khách hàng")
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
            image_label.place(x=150, y=40)

            title_lbl = customtkinter.CTkLabel(
                master=password,
                text="Đổi mật khẩu",
                font=font720,
                bg_color="#2b2b2b",
            )
            title_lbl.place(x=200, y=40)

            current_pw_lbl = customtkinter.CTkLabel(
                master=password, text="Mật khẩu mới: ", font=font720, bg_color="#2b2b2b"
            )
            current_pw_lbl.place(x=50, y=150)

            current_pw_txt = customtkinter.CTkEntry(
                master=password, font=font720, show="*", width=200
            )
            current_pw_txt.place(x=250, y=150)

            confirm_pw_lbl = customtkinter.CTkLabel(
                master=password,
                text="Nhâp lại mật khẩu mới: ",
                font=font720,
                bg_color="#2b2b2b",
            )
            confirm_pw_lbl.place(x=50, y=220)

            conform_pw_txt = customtkinter.CTkEntry(
                master=password, show="*", font=font720, width=200
            )
            conform_pw_txt.place(x=250, y=220)

            def show_password():
                if i.get() == 1:
                    conform_pw_txt.configure(show="")
                    current_pw_txt.configure(show="")
                else:
                    conform_pw_txt.configure(show="*")
                    current_pw_txt.configure(show="*")

            i = customtkinter.IntVar()

            password_show = customtkinter.CTkCheckBox(
                password,
                text="Hiện mật khẩu",
                variable=i,
                command=show_password,
                bg_color="#2b2b2b",
            )
            password_show.place(x=250, y=260)

            id_txt = Entry(password)
            id_txt.insert(0, "{}".format(Global.current_user[0]))

            def change_password():
                customerid = id_txt.get()
                password1 = current_pw_txt.get()
                new_password = conform_pw_txt.get()

                if password1 == new_password:
                    password720 = CustomerLibs(cid=customerid, password=new_password)
                    result = password_change(password720)
                    if result == True:
                        messagebox.showinfo(
                            "Hệ thống đặt xe taxi",
                            "Đổi mật khẩu thành công!",
                        )
                        self.root.destroy()
                        root = customtkinter.CTk()
                        login.Login(root)
                        root.mainloop()
                    else:
                        messagebox.showerror(
                            "Hệ thống đặt xe taxi",
                            "Đã có lỗi xảy ra!",
                        )

                else:
                    messagebox.showerror(
                        "Hệ thống đặt xe taxi",
                        "Mật khẩu không khớp. Vui lòng thử lại!",
                    )

            confirm_btn = customtkinter.CTkButton(
                master=password,
                command=change_password,
                text="Đổi mật khẩu",
                font=font720,
            )
            confirm_btn.place(x=250, y=310)

        # -----------------------------Change Password Button------------------------------------------
        view_customer_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/key-solid-24.png"
            )
        )
        view_customer_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Đổi mật khẩu",
            command=change_password_gui,
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=view_customer_btn_image,
            fg_color="#2b2b2b",
        )
        view_customer_btn.place(x=50, y=450)

        # -----------------------------Delete account function------------------------------------------
        def delete_account():
            delete_account_dialog = customtkinter.CTkInputDialog(
                text="Bạn có muốn xóa tài khoản của mình không? Nếu bạn muốn xóa thì hãy nhập CÓ hoặc KHÔNG để hủy",
                title="Xóa tài khoản",
            )
            dialog_result = delete_account_dialog.get_input()
            if dialog_result == "CÓ":
                customer_idd = customerid.get()
                delete_result = delete_record(customer_idd)
                if delete_result:
                    messagebox.showinfo(
                        "Hệ thống đặt xe taxi",
                        "Tài khoản của bạn đã được xóa thành công!",
                    )
                    self.root.destroy()
                    root = customtkinter.CTk()
                    login.Login(root)
                    root.mainloop()
            else:
                messagebox.showinfo(
                    "Hệ thống đặt xe taxi",
                    "Việc xóa tài khoản đã bị hủy bỏ",
                )

        # -----------------------------Delete Account Button------------------------------------------
        delete_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/user-x-regular-24.png"
            )
        )
        detete_account_btn = customtkinter.CTkButton(
            master=left_frame,
            command=delete_account,
            text="Xóa tài khoản",
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            image=delete_btn_image,
            fg_color="#2b2b2b",
        )
        detete_account_btn.place(x=50, y=500)

        # -----------------------------Logout Function------------------------------------------
        def logout():
            self.root.destroy()
            root = customtkinter.CTk()
            login.Login(root)
            root.mainloop()

        # -----------------------------Logout Button------------------------------------------
        logout_btn_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/log-out-circle-regular-24.png"
            )
        )
        logout_btn = customtkinter.CTkButton(
            master=left_frame,
            text="Đăng xuất",
            fg_color="#2b2b2b",
            hover_color="black",
            font=side_menu_font,
            width=200,
            anchor="w",
            command=logout,
            image=logout_btn_image,
        )
        logout_btn.place(x=50, y=550)

        # -----------------------------Theme Function------------------------------------------

        theme_lbl = customtkinter.CTkLabel(
            left_frame, text="Giao diện:", font=side_menu_font
        )
        theme_lbl.place(x=50, y=600)

        def combobox_callback(choice):
            customtkinter.set_appearance_mode(choice)
            if choice == "light":
                cover_image_label["bg"] = "#dbdbdb"

                style1.configure(
                    "Treeview",
                    background="#dbdbdb",
                    fieldbackground="#dbdbdb",
                    foreground="black",
                )
                log_name_lbl.configure(fg_color="#dbdbdb")
                log_name_lbl.configure(text_color="#2b2b2b")

            if choice == "dark":
                cover_image_label["bg"] = "#2b2b2b"
                log_name_lbl.configure(fg_color="#2b2b2b")
                log_name_lbl.configure(text_color="white")
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
        combobox.place(x=50, y=630)
        combobox.set("dark")  # set initi

        # +++++++++++++++++++++++++++++++Bottom Frame++++++++++++++++++++++++++++++++++++++++

        parent_tab = customtkinter.CTkTabview(self.root)
        parent_tab.pack(side=TOP, fill=BOTH, padx=10, pady=(0, 20), expand=TRUE)

        # ++++++++++++++++++++++Home Tab Frame+++++++++++++++++++++++++++++++++++++++++++
        parent_tab.add("Trang chủ")

        # +++++++++++++++++++++++++Welcome Label+++++++++++++++++++
        current_time = datetime.datetime.now()
        current_time.hour
        if current_time.hour < 12:
            text = "Chào buổi sáng"
        elif 12 <= current_time.hour < 18:
            text = "Chào buổi chiều"
        else:
            text = "Chào buổi tối"

        welcome_lbl = customtkinter.CTkLabel(
            master=parent_tab.tab("Trang chủ"),
            text="{} {}!".format(text, Global.current_user[1]),
            font=title_font,
        )
        welcome_lbl.place(x=10, y=20)

        pick_up_address_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Trang chủ"), text="Điểm đón:", font=label_font
        )
        pick_up_address_lbl.place(x=50, y=140)

        pick_up_address_txt = customtkinter.CTkEntry(
            master=parent_tab.tab("Trang chủ"), font=font720, width=250
        )
        pick_up_address_txt.place(x=230, y=140)

        date_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Trang chủ"), text="Ngày đón: ", font=label_font
        )
        date_lbl.place(x=50, y=210)

        dt = date.today()
        style = ttk.Style()
        style.configure(
            "my.DateEntry",
            fieldbackground="#2a2d2e",
            background="red",
            foreground="black",
            arrowcolor="white",
        )

        date_lbl_txt = DateEntry(
            parent_tab.tab("Trang chủ"),
            font=("Times New Roman", 20, "normal"),
            width=21,
            date_pattern="yyyy-MM-dd",
            selectmode="day",
            style="my.DateEntry",
            background="green",
            bordercolor="red",
            selectbackground="green",
            mindate=dt,
            disableddaybackground="grey",
        )
        date_lbl_txt.place(x=285, y=260)

        pick_up_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Trang chủ"), text="Giờ đón:", font=label_font
        )
        pick_up_lbl.place(x=50, y=270)

        def update_time(time):
            pick_up_time_lbl.delete(0, len(pick_up_time_lbl.get()))
            pick_up_time_lbl.insert(0, str("{}:{} {}".format(*time)))

        def time_720():
            top = customtkinter.CTkToplevel(parent_tab.tab("Trang chủ"))
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
                master=top, text="Ok", command=lambda: update_time(time_picker.time())
            )
            ok_btn.pack()

        time = ()

        pick_up_time_lbl = customtkinter.CTkEntry(
            master=parent_tab.tab("Trang chủ"), font=font720, width=190
        )
        pick_up_time_lbl.bind("<Button-1>", lambda e: "break")
        pick_up_time_lbl.bind("<Key>", lambda e: "break")
        pick_up_time_lbl.place(x=230, y=270)

        time_img = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/time-five-regular-24.png"
            )
        )
        pick_up_time_btn = customtkinter.CTkButton(
            master=parent_tab.tab("Trang chủ"),
            image=time_img,
            text="",
            fg_color="black",
            command=time_720,
            font=font720,
            width=50,
        )
        pick_up_time_btn.place(x=430, y=270)

        drop_off_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Trang chủ"), text="Điểm đến:", font=label_font
        )
        drop_off_lbl.place(x=50, y=330)

        drop_off_txt1 = customtkinter.CTkEntry(
            master=parent_tab.tab("Trang chủ"), font=font720, width=250
        )
        drop_off_txt1.place(x=230, y=330)

        def request_booking():
            pick_up = pick_up_address_txt.get()
            date720 = date_lbl_txt.get()
            picuptime = pick_up_time_lbl.get()
            dropoff = drop_off_txt1.get()
            cid11 = customerid.get()

            booking = BookingLibs(cid=cid11, date=date720)
            check_result = customer_check_booking(booking)

            if (
                pick_up_address_txt.get() == ""
                or pick_up_time_lbl.get() == ""
                or drop_off_txt1.get() == ""
                or date_lbl_txt.get() == ""
            ):
                messagebox.showwarning(
                    "Hệ thống đặt xe taxi",
                    "Vui lòng điền tất cả các trường",
                )

            elif check_result != None:
                messagebox.showwarning(
                    "Hệ thống đặt xe taxi",
                    "Bạn đã đặt xe vào ngày hôm nay",
                )

            else:
                booking = BookingLibs(
                    pick_up_address=pick_up,
                    date=date720,
                    time=picuptime,
                    dropoffaddress=dropoff,
                    bookingstatus="Pending",
                    cid=cid11,
                )
                insert_result = insert_booking(booking)
                print("Kết quả chèn vào: ", insert_result)
                messagebox.showinfo(
                    "Hệ thống đặt xe taxi",
                    "Đặt xe thành công!",
                )
                update_booking_table.delete(*update_booking_table.get_children())
                booking_table()

        booking_btn = customtkinter.CTkButton(
            master=parent_tab.tab("Trang chủ"),
            command=request_booking,
            text="Đặt xe",
            font=label_font,
        )
        booking_btn.place(x=230, y=400)

        map_frame = Frame(parent_tab.tab("Trang chủ"), bg="white")
        map_frame.place(x=700, y=80)

        # Khởi tạo bản đồ
        map_widget = TkinterMapView(map_frame, width=770, height=600, corner_radius=0)
        map_widget.pack(side=RIGHT, fill=BOTH, pady=(10), padx=(10))
        map_widget.set_tile_server(
            "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=10
        )

        # Đặt vị trí mặc định bản đồ ở Đà Nẵng (Việt Nam)
        map_widget.set_position(16.0471, 108.2068)
        map_widget.set_zoom(6)

        # Khởi tạo geolocator để sử dụng API Geocoding (Nominatim)
        geolocator = Nominatim(user_agent="myGeocoder")

        # Hàm lấy tọa độ
        def get_coordinates_from_address(address):
            try:
                location = geolocator.geocode(address)
                if location:
                    return location.latitude, location.longitude
                else:
                    return None
            except Exception as e:
                print(f"Lỗi lấy tọa độ: {e}")
                return None

        # Hàm cập nhật bản đồ
        def update_map():
            global pick_up_marker, drop_off_marker, route_line

            pick_up_address = pick_up_address_txt.get()
            drop_off_address = drop_off_txt1.get()

            pick_up_coords = get_coordinates_from_address(pick_up_address)
            drop_off_coords = get_coordinates_from_address(drop_off_address)

            if pick_up_coords and drop_off_coords:
                pick_up_lat, pick_up_lng = pick_up_coords
                drop_off_lat, drop_off_lng = drop_off_coords

                map_widget.set_position(pick_up_lat, pick_up_lng)
                map_widget.set_zoom(14)

                # Xóa marker và đường cũ nếu có
                if pick_up_marker:
                    pick_up_marker.delete()
                if drop_off_marker:
                    drop_off_marker.delete()
                if route_line:
                    route_line.delete()

                # Tạo marker mới
                pick_up_marker = map_widget.set_marker(
                    pick_up_lat, pick_up_lng, text="Điểm đón"
                )
                drop_off_marker = map_widget.set_marker(
                    drop_off_lat, drop_off_lng, text="Điểm đến"
                )

                # Vẽ đường nối
                route_line = map_widget.set_path(
                    [(pick_up_lat, pick_up_lng), (drop_off_lat, drop_off_lng)],
                    color="blue",
                )
            else:
                print("Không thể tìm thấy tọa độ cho một hoặc cả hai địa chỉ.")

        # Gọi nút cập nhật
        update_map_button = customtkinter.CTkButton(
            parent_tab.tab("Trang chủ"),
            text="Cập nhật bản đồ",
            font=font720,
            command=update_map,
        )
        update_map_button.place(x=230, y=450)
        # ++++++++++++++++++++++Update Booking+++++++++++++++++++++++++
        parent_tab.add("Cập nhật đặt xe")

        update_bboking_frame = customtkinter.CTkFrame(
            master=parent_tab.tab("Cập nhật đặt xe"), width=470
        )
        update_bboking_frame.pack(side=LEFT, fill=BOTH, pady=(50, 100))

        self.pick_uptxt1 = StringVar()

        update_pick_up_address_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Cập nhật đặt xe"),
            bg_color="#333333",
            text="Điểm đón: ",
            font=label_font,
        )
        update_pick_up_address_lbl.place(x=20, y=150)

        update_pick_up_address_txt = customtkinter.CTkEntry(
            master=parent_tab.tab("Cập nhật đặt xe"), font=font720, width=250
        )
        update_pick_up_address_txt.place(x=170, y=150)

        date_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Cập nhật đặt xe"),
            bg_color="#333333",
            text="Ngày đón: ",
            font=label_font,
        )
        date_lbl.place(x=20, y=200)

        dt = date.today()
        style = ttk.Style()
        style.configure(
            "my.DateEntry",
            fieldbackground="#2a2d2e",
            background="red",
            foreground="black",
            arrowcolor="white",
        )

        update_date_txt = DateEntry(
            parent_tab.tab("Cập nhật đặt xe"),
            font=("Times New Roman", 20, "normal"),
            width=21,
            date_pattern="yyyy-MM-dd",
            selectmode="day",
            style="my.DateEntry",
            background="green",
            bordercolor="red",
            selectbackground="green",
            mindate=dt,
            disableddaybackground="grey",
        )
        update_date_txt.place(x=210, y=240)

        pick_up_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Cập nhật đặt xe"),
            bg_color="#333333",
            text="Giờ đón:",
            font=label_font,
        )
        pick_up_lbl.place(x=20, y=250)

        def update_time_2(time):
            update_pick_up_txt.delete(0, len(update_pick_up_txt.get()))
            update_pick_up_txt.insert(0, str("{}:{} {}".format(*time)))

        def time_720():
            top = customtkinter.CTkToplevel(parent_tab.tab("Cập nhật đặt xe"))
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
                master=top, text="Ok", command=lambda: update_time_2(time_picker.time())
            )
            ok_btn.pack()

        time = ()

        update_pick_up_txt = customtkinter.CTkEntry(
            master=parent_tab.tab("Cập nhật đặt xe"),
            textvariable=self.pick_uptxt1,
            font=font720,
            width=190,
        )
        update_pick_up_txt.bind("<Button-1>", lambda e: "break")
        update_pick_up_txt.bind("<Key>", lambda e: "break")
        update_pick_up_txt.place(x=170, y=250)

        time_img = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/time-five-regular-24.png"
            )
        )
        pick_up_time_btn = customtkinter.CTkButton(
            master=parent_tab.tab("Cập nhật đặt xe"),
            image=time_img,
            text="",
            fg_color="black",
            command=time_720,
            font=font720,
            width=40,
        )
        pick_up_time_btn.place(x=375, y=252)

        drop_off_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Cập nhật đặt xe"),
            bg_color="#333333",
            text="Điểm đến:",
            font=label_font,
        )
        drop_off_lbl.place(x=20, y=300)

        update_drop_off_txt = customtkinter.CTkEntry(
            master=parent_tab.tab("Cập nhật đặt xe"), font=font720, width=250
        )
        update_drop_off_txt.place(x=170, y=300)

        update_booking_id = Entry(self.root)

        def update_customer_booking():
            today = date.today()
            today720 = str(today)

            validate_result = validate_customer_booking(customerid.get())
            val3 = validate_result[0]
            val4 = val3[0]

            if (
                update_booking_id.get() == ""
                or update_pick_up_address_txt.get() == ""
                or update_date_txt.get() == ""
                or update_pick_up_txt.get() == ""
                or update_drop_off_txt.get() == ""
            ):
                messagebox.showwarning(
                    "Hệ thống đặt xe taxi",
                    "Vui lòng điền tất cả các trường",
                )

            elif validate_result != None:
                date3 = update_date_txt.get()
                if date3 < today720:
                    messagebox.showwarning(
                        "Hệ thống đặt xe taxi",
                        "Ngày bạn chọn đã hết hạn. Vui lòng chọn ngày đón mới.!",
                    )
                else:
                    update_booking = BookingLibs(
                        bookingid=update_booking_id.get(),
                        pick_up_address=update_pick_up_address_txt.get(),
                        date=update_date_txt.get(),
                        time=update_pick_up_txt.get(),
                        dropoffaddress=update_drop_off_txt.get(),
                    )

                    update_booking_result = update_customer_booking1(update_booking)
                    if update_booking_result == True:

                        messagebox.showinfo(
                            "Hệ thống đặt xe taxi",
                            "Đặt xe đã được cập nhật thành công.",
                        )
                        update_booking_table.delete(
                            *update_booking_table.get_children()
                        )
                        booking_table()

                    else:
                        messagebox.showerror(
                            "Hệ thống đặt xe taxi", "Đã có lỗi xảy ra!"
                        )

        update_booking_btn = customtkinter.CTkButton(
            master=parent_tab.tab("Cập nhật đặt xe"),
            text="Cập nhật",
            command=update_customer_booking,
            font=label_font,
        )
        update_booking_btn.place(x=170, y=350)

        def cancel_booking():
            update_id = update_booking_id.get()
            delete_result = delete_booking(update_id)
            if delete_result == True:
                messagebox.showinfo(
                    "Hệ thống đặt xe taxi", "Đặt xe đã được hủy thành công!"
                )
                update_booking_table.delete(*update_booking_table.get_children())
                booking_table()

            else:
                messagebox.showerror("Hệ thống đặt xe taxi", "Đã có lỗi xảy ra!")

        cancel_booking_btn = customtkinter.CTkButton(
            master=parent_tab.tab("Cập nhật đặt xe"),
            command=cancel_booking,
            text="Hủy",
            font=label_font,
            width=100,
        )
        cancel_booking_btn.place(x=320, y=350)

        update_booking_table = ttk.Treeview(parent_tab.tab("Cập nhật đặt xe"))
        update_booking_table.pack(side=RIGHT, fill=BOTH, pady=(70, 0))

        # -----------------------------Update Booking Table-----------------------------------------
        update_booking_table["columns"] = (
            "id",
            "pick_up_address",
            "date",
            "time",
            "dropoffaddress",
            "driverid",
            "status",
        )
        update_booking_table.column("#0", width=0, stretch=0)
        update_booking_table.column("id", width=100, anchor=CENTER)
        update_booking_table.column("pick_up_address", width=200, anchor=CENTER)
        update_booking_table.column("date", width=120, anchor=CENTER)
        update_booking_table.column("time", width=100, anchor=CENTER)
        update_booking_table.column("dropoffaddress", width=200, anchor=CENTER)
        update_booking_table.column("status", width=100, anchor=CENTER)
        update_booking_table.column("driverid", width=100, anchor=CENTER)

        update_booking_table.heading("#0", text="", anchor=CENTER)
        update_booking_table.heading("id", text="Mã", anchor=CENTER)
        update_booking_table.heading("pick_up_address", text="Điểm đón", anchor=CENTER)
        update_booking_table.heading("date", text="Ngày", anchor=CENTER)
        update_booking_table.heading("time", text="Giờ", anchor=CENTER)
        update_booking_table.heading("dropoffaddress", text="Điểm đến", anchor=CENTER)
        update_booking_table.heading("driverid", text="Mã tài xế", anchor=CENTER)
        update_booking_table.heading("status", text="Trạng thái", anchor=CENTER)

        def display_selected_item(a):
            update_pick_up_address_txt.delete(0, END)
            update_date_txt.delete(0, END)
            update_pick_up_txt.delete(0, END)
            update_drop_off_txt.delete(0, END)
            update_booking_id.delete(0, END)

            selected_item = update_booking_table.selection()[0]
            update_booking_id.insert(
                0, update_booking_table.item(selected_item)["values"][0]
            )
            update_pick_up_address_txt.insert(
                0, update_booking_table.item(selected_item)["values"][1]
            )
            update_date_txt.insert(
                0, update_booking_table.item(selected_item)["values"][2]
            )
            update_pick_up_txt.insert(
                0, update_booking_table.item(selected_item)["values"][3]
            )
            update_drop_off_txt.insert(
                0, update_booking_table.item(selected_item)["values"][4]
            )

        update_booking_table.bind("<<TreeviewSelect>>", display_selected_item)

        # -----------------------------Display data in table function------------------------------------------
        def booking_table():
            cus_idd = Entry(self.root)
            cus_idd.insert(0, Global.current_user[0])
            iddd = cus_idd.get()
            book_result = customer_booking_select_status_booked(iddd)
            i = 0
            for ro in book_result:
                update_booking_table.insert(
                    parent="",
                    index="end",
                    values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[7], ro[5]),
                )
                i = i + 1

        # ++++++++++++++++++++++++++++++++++Riding History Tab+++++++++++++++++++++++++++++++
        parent_tab.add("Lịch sử chuyến đi")

        booking_history_table = ttk.Treeview(parent_tab.tab("Lịch sử chuyến đi"))

        booking_history_table["columns"] = (
            "bookingid",
            "pick_up_address",
            "dropoffaddress",
            "date",
            "time",
        )
        booking_history_table.column("#0", width=0, stretch=0)
        booking_history_table.column("bookingid", width=100, anchor=CENTER)
        booking_history_table.column("pick_up_address", width=100, anchor=CENTER)
        booking_history_table.column("dropoffaddress", width=100, anchor=CENTER)
        booking_history_table.column("date", width=100, anchor=CENTER)
        booking_history_table.column("time", width=100, anchor=CENTER)

        booking_history_table.heading("#0", text="", anchor=CENTER)
        booking_history_table.heading("bookingid", text="Mã đặt xe", anchor=CENTER)
        booking_history_table.heading("pick_up_address", text="Điểm đón", anchor=CENTER)
        booking_history_table.heading("dropoffaddress", text="Điểm đến", anchor=CENTER)
        booking_history_table.heading("date", text="Ngày", anchor=CENTER)
        booking_history_table.heading("time", text="Giờ", anchor=CENTER)
        booking_history_table.pack(side=TOP, fill=BOTH, expand=TRUE)

        def booking_history():
            book_result = customer_booking_select_all(customerid.get())

            for x in book_result:
                booking_history_table.insert(
                    parent="", index="end", values=(x[0], x[1], x[4], x[2], x[3])
                )

        booking_history()

        parent_tab.add("Báo cáo")
        parent_tab.tab("Báo cáo").configure(fg_color="white")

        # ++++++++++++++++++++++++++Tab Frame++++++++++++++++++++++
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

        cus_idd = Entry(self.root)
        cus_idd.insert(0, Global.current_user[0])
        iddd = cus_idd.get()

        try:
            sql_engine = create_engine(
                "mysql+pymysql://root:Hoa30025091@localhost/taxi_booking_system"
            )
            db_connection = sql_engine.connect()
            print("Kết nối CSDL thành công.")
        except SQLAlchemyError as e:
            print("Kết nối CSDL thất bại:", e)

        # -----------------------------Booking analysis------------------------------------------
        query720 = (
            "SELECT *, COUNT(bookingid) as ID  FROM booking WHERE cid="
            + iddd
            + " GROUP BY date"
        )
        df = pandas.read_sql(query720, db_connection, index_col="date")
        fig2 = df.plot.line(
            title="Biểu đồ thống kê số lần đặt xe", y="ID", figsize=(5.5, 6)
        ).get_figure()
        plot2 = FigureCanvasTkAgg(fig2, parent_tab.tab("Báo cáo"))
        plot2.get_tk_widget().place(x=450, y=5)

        booking_table()


if __name__ == "__main__":
    root = customtkinter.CTk()
    CustomerDashboard(root)
    root.mainloop()
