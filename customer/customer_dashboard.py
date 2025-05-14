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
import openrouteservice
from openrouteservice import convert
from tkcalendar import DateEntry
from tktimepicker import AnalogPicker, AnalogThemes, constants
from billing import customer_billing_history
from customer import (
    customer_booking_history,
    view_profile,
)
from dbms.booking_backend import (
    insert_booking,
    customer_booking_select_status_pending,
    delete_booking,
    customer_check_booking,
)
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
            master=top_frame, text="Dashboard Khách hàng", font=title_font
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
        profile_btn.place(x=50, y=200)

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
        manage_customers_btn.place(x=50, y=250)

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
        manage_drivers_btn.place(x=50, y=300)

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
        billing_btn.place(x=50, y=350)

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
        view_customer_btn.place(x=50, y=400)

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
        logout_btn.place(x=50, y=450)

        # -----------------------------Theme Function------------------------------------------

        theme_lbl = customtkinter.CTkLabel(
            left_frame, text="Giao diện:", font=side_menu_font
        )
        theme_lbl.place(x=50, y=500)

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
        combobox.place(x=50, y=530)
        combobox.set("dark")  # set initi

        # +++++++++++++++++++++++++++++++Bottom Frame++++++++++++++++++++++++++++++++++++++++

        parent_tab = customtkinter.CTkTabview(self.root)
        parent_tab.pack(side=TOP, fill=BOTH, padx=10, pady=(0, 20), expand=TRUE)

        # ++++++++++++++++++++++Booking Tab Frame+++++++++++++++++++++++++++++++++++++++++++
        parent_tab.add("Đặt xe")

        pick_up_address_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Đặt xe"), text="Điểm đón:", font=label_font
        )
        pick_up_address_lbl.place(x=50, y=80)

        pick_up_address_txt = customtkinter.CTkEntry(
            master=parent_tab.tab("Đặt xe"), font=font720, width=250
        )
        pick_up_address_txt.place(x=230, y=90)

        date_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Đặt xe"), text="Ngày đón: ", font=label_font
        )
        date_lbl.place(x=50, y=150)

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
            parent_tab.tab("Đặt xe"),
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
        date_lbl_txt.place(x=285, y=180)

        pick_up_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Đặt xe"), text="Giờ đón:", font=label_font
        )
        pick_up_lbl.place(x=50, y=210)

        def update_time(time):
            pick_up_time_lbl.delete(0, len(pick_up_time_lbl.get()))
            pick_up_time_lbl.insert(0, str("{}:{} {}".format(*time)))

        def time_720():
            top = customtkinter.CTkToplevel(parent_tab.tab("Đặt xe"))
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
            master=parent_tab.tab("Đặt xe"), font=font720, width=190
        )
        pick_up_time_lbl.bind("<Button-1>", lambda e: "break")
        pick_up_time_lbl.bind("<Key>", lambda e: "break")
        pick_up_time_lbl.place(x=230, y=210)

        time_img = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/time-five-regular-24.png"
            )
        )
        pick_up_time_btn = customtkinter.CTkButton(
            master=parent_tab.tab("Đặt xe"),
            image=time_img,
            text="",
            fg_color="black",
            command=time_720,
            font=font720,
            width=50,
        )
        pick_up_time_btn.place(x=430, y=210)

        drop_off_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Đặt xe"), text="Điểm đến:", font=label_font
        )
        drop_off_lbl.place(x=50, y=270)

        drop_off_txt1 = customtkinter.CTkEntry(
            master=parent_tab.tab("Đặt xe"), font=font720, width=250
        )
        drop_off_txt1.place(x=230, y=270)

        # Tự động cập nhật bản đồ khi người dùng thoát ra khỏi ô nhập địa chỉ
        drop_off_txt1.bind("<FocusOut>", lambda event: update_map())

        kilomet_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Đặt xe"), text="Cây số (km):", font=label_font
        )
        kilomet_lbl.place(x=50, y=330)

        kilomet_txt = customtkinter.CTkEntry(
            master=parent_tab.tab("Đặt xe"),
            font=font720,
            width=250,
            state="disabled",  # Không cho người dùng nhập liệu
        )
        kilomet_txt.place(x=230, y=330)

        total_amount_lbl = customtkinter.CTkLabel(
            parent_tab.tab("Đặt xe"), text="Số tiền:", font=label_font
        )
        total_amount_lbl.place(x=50, y=390)

        total_amount_txt = customtkinter.CTkEntry(
            master=parent_tab.tab("Đặt xe"),
            font=font720,
            width=250,
            state="disabled",  # Không cho người dùng nhập liệu
        )
        total_amount_txt.place(x=230, y=390)

        def request_booking():
            update_map()
            pick_up = pick_up_address_txt.get()
            date720 = date_lbl_txt.get()
            pick_up_time = pick_up_time_lbl.get()
            dropoff = drop_off_txt1.get()
            cid11 = customerid.get()
            kilomet = kilomet_txt.get()

            booking = BookingLibs(cid=cid11, date=date720)
            check_result = customer_check_booking(booking)

            pick_up_coords = get_coordinates_from_address(pick_up)
            drop_off_coords = get_coordinates_from_address(dropoff)

            # Kiểm tra nếu không tìm được tọa độ
            if pick_up_coords is None or drop_off_coords is None:
                messagebox.showerror(
                    "Hệ thống đặt xe taxi",
                    "Không thể tìm thấy tọa độ cho một hoặc cả hai địa chỉ.",
                )
                return

            if (
                pick_up_address_txt.get() == ""
                or pick_up_time_lbl.get() == ""
                or drop_off_txt1.get() == ""
                or date_lbl_txt.get() == ""
                or kilomet_txt.get() == ""
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
                    pickupaddress=pick_up,
                    date=date720,
                    time=pick_up_time,
                    dropoffaddress=dropoff,
                    bookingstatus="Đang xử lý",
                    cid=cid11,
                    kilomet=kilomet,
                )
                insert_result = insert_booking(booking)
                print("Kết quả chèn vào: ", insert_result)

                if insert_result:
                    messagebox.showinfo(
                        "Hệ thống đặt xe taxi",
                        "Đặt xe thành công!",
                    )
                    pending_status_booking_table.delete(
                        *pending_status_booking_table.get_children()
                    )
                    booking_table()

                    # Reset các trường nhập liệu
                    pick_up_address_txt.delete(0, "end")
                    drop_off_txt1.delete(0, "end")
                    pick_up_time_lbl.delete(0, "end")

                    # Đặt lại ngày về hôm nay
                    date_lbl_txt.set_date(datetime.date.today())

                    kilomet_txt.configure(state="normal")
                    kilomet_txt.delete(0, "end")
                    kilomet_txt.configure(state="disabled")

                    total_amount_txt.configure(state="normal")
                    total_amount_txt.delete(0, "end")
                    total_amount_txt.configure(state="disabled")

                    # Xóa marker và tuyến đường trên bản đồ
                    global pick_up_marker, drop_off_marker, route_line
                    if pick_up_marker:
                        pick_up_marker.delete()
                        pick_up_marker = None
                    if drop_off_marker:
                        drop_off_marker.delete()
                        drop_off_marker = None
                    if route_line:
                        route_line.delete()
                        route_line = None
                else:
                    messagebox.showerror(
                        "Hệ thống đặt xe taxi",
                        "Đã xảy ra lỗi khi thêm đơn đặt xe. Vui lòng thử lại.",
                    )

        booking_btn = customtkinter.CTkButton(
            master=parent_tab.tab("Đặt xe"),
            command=request_booking,
            text="Đặt xe",
            font=label_font,
        )
        booking_btn.place(x=230, y=470)

        map_frame = Frame(parent_tab.tab("Đặt xe"), bg="white")
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

                # Xóa marker và tuyến đường cũ
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

                # Gọi OpenRouteService để lấy tuyến đường
                client = openrouteservice.Client(
                    key="5b3ce3597851110001cf62485be4cfcadac24e138154a530c7ef654b"
                )  # Thay bằng API key thực tế

                coords = (
                    (pick_up_lng, pick_up_lat),
                    (drop_off_lng, drop_off_lat),
                )  # Lưu ý: longitude(kinh đố) trước!

                try:
                    route = client.directions(
                        coordinates=coords, profile="driving-car", format="geojson"
                    )

                    # Lấy tọa độ tuyến đường
                    route_coords = route["features"][0]["geometry"]["coordinates"]
                    distance_m = route["features"][0]["properties"]["summary"][
                        "distance"
                    ]
                    distance_km = round(distance_m / 1000, 2)

                    # Cập nhật giá trị khoảng cách vào ô kilomet_txt
                    # Khi cần cập nhật giá trị:
                    kilomet_txt.configure(state="normal")
                    kilomet_txt.delete(0, "end")  # Xóa giá trị cũ trong ô
                    kilomet_txt.insert(
                        0, f"{distance_km:.2f}"
                    )  # Thêm giá trị mới vào ô
                    kilomet_txt.configure(state="disabled")

                    # Cập nhật giá trị Số tiền vào ô total_amount_txt
                    # Định dạng tiền tệ với dấu chấm phân cách hàng nghìn
                    formatted_amount = (
                        "{:,.0f}".format(distance_km * 12000).replace(",", ".") + " VND"
                    )
                    # Thêm vào ô nhập liệu (read-only)
                    total_amount_txt.configure(state="normal")
                    total_amount_txt.delete(0, "end")  # Xóa giá trị cũ trong ô
                    total_amount_txt.insert(
                        0, formatted_amount
                    )  # Thêm giá trị mới vào ô
                    total_amount_txt.configure(state="disabled")

                    # Đổi tọa độ để map_widget hiểu (lat, lng)
                    route_latlng = [(coord[1], coord[0]) for coord in route_coords]

                    # Vẽ tuyến đường
                    route_line = map_widget.set_path(route_latlng, color="blue")

                    # Hiển thị khoảng cách
                    # messagebox.showinfo(
                    #     "Thông tin khoảng cách",
                    #     f"Khoảng cách từ điểm đón đến điểm đến là: {distance_km} km",
                    # )

                except Exception as e:
                    print("Lỗi khi gọi API OpenRouteService:", e)
                    messagebox.showerror(
                        "Lỗi",
                        "Không thể tính toán tuyến đường. Vui lòng kiểm tra kết nối hoặc API Key.",
                    )
            else:
                print("Không thể tìm thấy tọa độ cho một hoặc cả hai địa chỉ.")

        # ++++++++++++++++++++++pending status boking table+++++++++++++++++++++++++
        parent_tab.add("Đang xử lý")

        # Frame chính cho tab "Đang xử lý"
        pending_status_booking_frame = customtkinter.CTkFrame(
            master=parent_tab.tab("Đang xử lý"),
        )
        pending_status_booking_frame.pack(fill=BOTH, pady=(10, 10))

        pending_status_booking_id = Entry(self.root)

        def cancel_booking():
            booking_id = pending_status_booking_id.get()
            if not booking_id:
                messagebox.showwarning(
                    "Hệ thống đặt xe taxi", "Vui lòng chọn đơn cần hủy!"
                )
                return

            confirm = messagebox.askyesno(
                "Xác nhận", "Bạn có chắc muốn hủy đặt xe này?"
            )
            if not confirm:
                return

            # Gọi hàm xóa đơn đặt xe trạng thái đang xử lý
            delete_result = delete_booking(booking_id)
            if delete_result == True:
                messagebox.showinfo(
                    "Hệ thống đặt xe taxi", "Đặt xe đã được hủy thành công!"
                )
                # Cập nhật lại bảng (xóa dữ liệu cũ, gọi lại từ DB)
                pending_status_booking_table.delete(
                    *pending_status_booking_table.get_children()
                )
                booking_table()

            else:
                messagebox.showerror("Hệ thống đặt xe taxi", "Đã có lỗi xảy ra!")

        # Nút hủy
        cancel_booking_btn = customtkinter.CTkButton(
            master=pending_status_booking_frame,
            command=cancel_booking,
            text="Hủy",
            font=label_font,
            width=100,
        )
        cancel_booking_btn.pack(side=BOTTOM, pady=10)

        # Bảng Treeview nằm phía trên nút hủy
        pending_status_booking_table = ttk.Treeview(pending_status_booking_frame)
        pending_status_booking_table.pack(
            side=TOP, fill=BOTH, expand=True, pady=(10, 0)
        )

        # -----------------------------Cấu hình bảng-----------------------------------------
        pending_status_booking_table["columns"] = (
            "id",
            "pick_up_address",
            "date",
            "time",
            "dropoffaddress",
            "kilomet",
            "price",
            "status",
        )
        pending_status_booking_table.column("#0", width=0, stretch=0)
        pending_status_booking_table.column("id", width=100, anchor=CENTER)
        pending_status_booking_table.column("pick_up_address", width=300, anchor=CENTER)
        pending_status_booking_table.column("date", width=150, anchor=CENTER)
        pending_status_booking_table.column("time", width=150, anchor=CENTER)
        pending_status_booking_table.column("dropoffaddress", width=300, anchor=CENTER)
        pending_status_booking_table.column("kilomet", width=150, anchor=CENTER)
        pending_status_booking_table.column("price", width=200, anchor=CENTER)
        pending_status_booking_table.column("status", width=150, anchor=CENTER)

        pending_status_booking_table.heading("#0", text="", anchor=CENTER)
        pending_status_booking_table.heading("id", text="Mã", anchor=CENTER)
        pending_status_booking_table.heading(
            "pick_up_address", text="Điểm đón", anchor=CENTER
        )
        pending_status_booking_table.heading("date", text="Ngày", anchor=CENTER)
        pending_status_booking_table.heading("time", text="Giờ", anchor=CENTER)
        pending_status_booking_table.heading(
            "dropoffaddress", text="Điểm đến", anchor=CENTER
        )
        pending_status_booking_table.heading("kilomet", text="Cây số", anchor=CENTER)
        pending_status_booking_table.heading("price", text="Giá tiền", anchor=CENTER)
        pending_status_booking_table.heading("status", text="Trạng thái", anchor=CENTER)

        def display_selected_booking(event):
            selected_item = pending_status_booking_table.selection()
            if selected_item:
                booking_id = pending_status_booking_table.item(selected_item)["values"][
                    0
                ]
                pending_status_booking_id.delete(0, END)
                pending_status_booking_id.insert(0, booking_id)

        pending_status_booking_table.bind(
            "<<TreeviewSelect>>", display_selected_booking
        )

        # -----------------------------Display data in table function------------------------------------------
        def booking_table():
            cus_idd = Entry(self.root)
            cus_idd.insert(0, Global.current_user[0])
            iddd = cus_idd.get()
            book_result = customer_booking_select_status_pending(iddd)
            for ro in book_result:
                try:
                    kilometer = float(ro[8])  # cột số 8 là kilomet
                    price = int(kilometer * 12000)
                    price_str = f"{price:,.0f}".replace(",", ".") + " VND"
                except:
                    price_str = "0" + " VND"

                pending_status_booking_table.insert(
                    parent="",
                    index="end",
                    values=(
                        ro[0],  # id
                        ro[1],  # pick_up_address
                        ro[2],  # date
                        ro[3],  # time
                        ro[4],  # dropoffaddress
                        ro[8],  # kilomet
                        price_str,  # <-- giá tiền),
                        ro[5],  # status
                    ),
                )

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

        booking_table()


if __name__ == "__main__":
    root = customtkinter.CTk()
    CustomerDashboard(root)
    root.mainloop()
