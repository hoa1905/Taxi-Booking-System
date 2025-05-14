from datetime import date
from time import strftime
from tkinter import *
import customtkinter
from tkinter import ttk
from tkinter import messagebox
from reportlab.lib.units import inch
from dbms.billing_backend import billing_table, insert_billing
from dbms.booking_backend import driver_update_booking
from libs.billing_libs import BillingLibs
from libs.booking_libs import BookingLibs
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Đăng ký font hỗ trợ tiếng Việt
pdfmetrics.registerFont(TTFont("TimesNewRoman", "C:/Windows/Fonts/times.ttf"))
pdfmetrics.registerFont(TTFont("TimesNewRomanBold", "C:/Windows/Fonts/timesbd.ttf"))


class AdminPayment:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.title("Hệ thống đặt xe taxi | Hệ thống hoá đơn")
        self.main.resizable(0, 0)
        width = 1400
        height = 450
        my_screen_width = self.main.winfo_screenwidth()
        my_screen_height = self.main.winfo_screenheight()
        xCordinate = int((my_screen_width / 2) - (width / 2))
        yCordinate = int((my_screen_height / 2) - (height / 2))
        self.main.geometry(
            "{}x{}+{}+{}".format(width, height, xCordinate + 100, yCordinate)
        )
        self.main.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )

        # ++++++++++++++++++++++++++++++++Font Collection+++++++++++++++++++++++++++++++++++++++++++
        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="normal"
        )
        font = customtkinter.CTkFont(family="Times New Roman", size=20, weight="bold")
        num = random.randint(1000, 100000)

        def only_numbers(char):
            # Validate for numbers only
            if (char.isdigit()) or (char == ""):
                return True
            else:
                return False

        validation = self.main.register(only_numbers)

        self.km_txt = StringVar()
        self.unit_txt = StringVar()

        def calculate(var=None, index=None, mode=None):
            km_raw = km_txt.get().replace(",", ".").strip()
            unit_raw = unit_txt.get().replace(".", "").strip()

            try:
                if km_raw and unit_raw:
                    km = float(km_raw)
                    unit = float(unit_raw)
                    total = km * unit

                    total_txt.delete(0, END)
                    total_txt.insert(0, "{:,.0f}".format(total).replace(",", "."))
                else:
                    total_txt.delete(0, END)
            except ValueError:
                total_txt.delete(0, END)
                total_txt.insert(0, "Giá trị sai")

        assign_booking_frame = customtkinter.CTkFrame(
            self.main, width=400, corner_radius=20
        )
        assign_booking_frame.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        title11_lbl = customtkinter.CTkLabel(
            master=assign_booking_frame, text="HỆ THỐNG HÓA ĐƠN", font=font
        )
        title11_lbl.place(x=50, y=20)

        name_lbl = customtkinter.CTkLabel(
            assign_booking_frame, text="Khách hàng: ", font=font720
        )
        name_lbl.place(x=30, y=100)

        name_txt = customtkinter.CTkEntry(assign_booking_frame, font=font720, width=200)
        name_txt.bind("<Button-1>", lambda e: "break")
        name_txt.bind("<Key>", lambda e: "break")
        name_txt.place(x=140, y=100)

        credit_lbl = customtkinter.CTkLabel(
            assign_booking_frame, text="Số tín dụng: ", font=font720
        )
        credit_lbl.place(x=30, y=150)

        credit_txt = customtkinter.CTkEntry(
            assign_booking_frame, font=font720, width=200
        )
        credit_txt.bind("<Button-1>", lambda e: "break")
        credit_txt.bind("<Key>", lambda e: "break")
        credit_txt.place(x=140, y=150)

        km_lbl = customtkinter.CTkLabel(
            assign_booking_frame, text="Cây số: ", font=font720
        )
        km_lbl.place(x=30, y=200)

        km_txt = customtkinter.CTkEntry(
            assign_booking_frame,
            textvariable=self.km_txt,
            validatecommand=(validation, "%P"),
            font=font720,
            width=200,
        )
        km_txt.bind("<Button-1>", lambda e: "break")
        km_txt.bind("<Key>", lambda e: "break")
        km_txt.place(x=140, y=200)

        unit_lbl = customtkinter.CTkLabel(
            assign_booking_frame, text="Giá:", font=font720
        )
        unit_lbl.place(x=30, y=250)

        unit_txt = customtkinter.CTkEntry(
            assign_booking_frame,
            textvariable=self.unit_txt,
            validatecommand=(validation, "%P"),
            font=font720,
            width=200,
        )
        unit_txt.insert(0, "{:,}".format(12000).replace(",", "."))
        unit_txt.configure(state="readonly")
        unit_txt.place(x=140, y=250)

        total_lbl = customtkinter.CTkLabel(
            assign_booking_frame, text="Tổng cộng:", font=font720
        )
        total_lbl.place(x=30, y=300)

        total_txt = customtkinter.CTkEntry(
            assign_booking_frame, font=font720, width=200
        )
        total_txt.bind("<Button-1>", lambda e: "break")
        total_txt.bind("<Key>", lambda e: "break")
        total_txt.place(x=140, y=300)

        # Trace the variables
        self.unit_txt.trace_add("write", calculate)
        self.km_txt.trace_add("write", calculate)

        bookingid = Entry(self.main)

        pick_up_address_txt = Entry(self.main)
        drop_off_address_txt = Entry(self.main)
        date_txt = Entry(self.main)
        time_txt = Entry(self.main)

        def generate_bill():
            name = name_txt.get()
            km = km_txt.get().replace(",", ".").strip()
            unit = unit_txt.get().replace(".", "").strip()
            total = total_txt.get().replace(".", "").strip()

            try:
                km_val = float(km)
                unit_val = float(unit)
                total_val = float(total)
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                return

            bookingid1 = bookingid.get()
            todatedate = date.today()

            billing = BillingLibs(
                name=name,
                km=km_val,
                unit=unit_val,
                total=total_val,
                bookingid=bookingid1,
                date=todatedate,
            )
            result = insert_billing(billing)

            booking = BookingLibs(bookingstatus="Đã thanh toán", bookingid=bookingid1)
            updatebookingResult = driver_update_booking(booking)
            if result == True:
                update_booking_result_lbl.configure(
                    text="Hóa đơn đã được tạo thành công"
                )
                booking_table_tree_view.delete(*booking_table_tree_view.get_children())
                billing_tabel()

                # Tạo tên file theo định dạng: "tên khách hàng - ngày đặt - giờ đặt - num"
                customer_name = name_txt.get()
                booking_date = date_txt.get()
                my_path = "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Hoa_don_{}_{}_{}.pdf".format(
                    customer_name, booking_date, num
                )

                c = canvas.Canvas(my_path, pagesize=letter)

                # Các đường kẻ
                c.setStrokeColorRGB(1, 0, 0)
                c.setLineWidth(2)
                c.line(1 * inch, 8 * inch, 7.5 * inch, 8 * inch)

                # Tiêu đề hệ thống và thông tin
                c.setFont("TimesNewRomanBold", 13)
                c.drawString(2 * inch, 10 * inch, "Hệ thống đặt xe taxi")
                c.drawString(
                    2 * inch,
                    9.6 * inch,
                    "Phạm Tấn Hòa, Nguyễn Thanh Hoan - VKU-Lập trình Python (3)",
                )
                c.drawString(2 * inch, 9.2 * inch, "Số điện thoại: 0123456789")
                c.drawString(6.5 * inch, 10 * inch, "Số hóa đơn: {}".format(num))

                # In đậm, kích thước lớn cho tiêu đề "HÓA ĐƠN TAXI"
                c.setFont("TimesNewRomanBold", 30)
                c.drawString(2.8 * inch, 8.1 * inch, "HÓA ĐƠN TAXI")

                # Logo
                c.drawImage(
                    "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo2.jpg",
                    0.2 * inch,
                    8.9 * inch,
                )

                # Thông tin ngày, giờ
                today_date = date.today()
                c.setFont("TimesNewRoman", 13)
                c.drawString(1 * inch, 7.5 * inch, "Ngày: {}".format(today_date))
                currenttime = strftime("%I:%M:%S")
                c.drawString(6 * inch, 7.5 * inch, "Giờ: {}".format(currenttime))

                # Thông tin khách hàng
                c.drawString(
                    1 * inch, 7 * inch, "Tên khách hàng: {}".format(name_txt.get())
                )
                c.drawString(
                    1 * inch,
                    6.7 * inch,
                    "Điểm đón: {}".format(pick_up_address_txt.get()),
                )
                c.drawString(
                    1 * inch,
                    6.4 * inch,
                    "Điểm đến: {}".format(drop_off_address_txt.get()),
                )
                c.drawString(1 * inch, 6.1 * inch, "Ngày: {}".format(date_txt.get()))
                c.drawString(1 * inch, 5.8 * inch, "Giờ: {}".format(time_txt.get()))

                c.setStrokeColorRGB(1, 0, 0)
                c.setLineWidth(1)

                # Open line - Các đường kẻ
                c.line(1 * inch, 5.5 * inch, 7.5 * inch, 5.5 * inch)
                # Close line
                c.line(1 * inch, 5 * inch, 7.5 * inch, 5 * inch)

                # Mô tả
                c.drawString(1 * inch, 5.2 * inch, "Mô tả")
                c.drawString(3 * inch, 5.2 * inch, "Cây số")
                c.drawString(5 * inch, 5.2 * inch, "Giá")
                c.drawString(6.5 * inch, 5.2 * inch, "Tổng tiền")

                # ++++++++++++++++++++++++++++++++++++++Table Data+++++++++++++++++++++++++++++++
                # Dữ liệu mô tả
                c.drawString(
                    1 * inch, 4.7 * inch, "Từ {}".format(pick_up_address_txt.get())
                )

                # Description data
                c.drawString(
                    1 * inch, 4.4 * inch, "đến {}".format(drop_off_address_txt.get())
                )

                # Kilometer Data
                c.drawString(3 * inch, 4.7 * inch, "{} KM".format(km_txt.get()))

                # Unit Data
                unit_value = 12000
                formatted_unit = "{:,.0f}".format(unit_value).replace(",", ".") + " VND"
                c.drawString(5 * inch, 4.7 * inch, formatted_unit)

                # Total Data
                c.drawString(6.5 * inch, 4.7 * inch, "{} VND".format(total_txt.get()))

                # Lưu trang
                c.showPage()
                c.save()

            else:
                messagebox.showerror("Hệ thống đặt xe taxi", "Đã có lỗi xảy ra")

        available_driver_btn = customtkinter.CTkButton(
            assign_booking_frame,
            text="Tạo hóa đơn",
            command=generate_bill,
            font=font720,
            width=150,
        )
        available_driver_btn.place(x=150, y=350)

        update_booking_result_lbl = customtkinter.CTkLabel(
            assign_booking_frame, text="", font=font720
        )
        update_booking_result_lbl.place(x=80, y=390)

        table_frame = customtkinter.CTkFrame(master=self.main, width=840)
        table_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10), pady=10)

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

        booking_table_tree_view = ttk.Treeview(table_frame)
        booking_table_tree_view.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        booking_table_tree_view["columns"] = (
            "cid",
            "bookingid",
            "did",
            "name",
            "credit",
            "date",
            "time",
            "pickupaddress",
            "dropoffaddress",
            "kilomet",
            "drivername",
        )
        booking_table_tree_view.column("#0", width=0, stretch=0)
        booking_table_tree_view.column("cid", width=0, stretch=0)
        booking_table_tree_view.column("bookingid", width=0, stretch=0)
        booking_table_tree_view.column("did", width=0, stretch=0)
        booking_table_tree_view.column("name", width=200, anchor=CENTER)
        booking_table_tree_view.column("credit", width=0, stretch=0)
        booking_table_tree_view.column("date", width=120, anchor=CENTER)
        booking_table_tree_view.column("time", width=100, anchor=CENTER)
        booking_table_tree_view.column("pickupaddress", width=200, anchor=CENTER)
        booking_table_tree_view.column("dropoffaddress", width=200, anchor=CENTER)
        booking_table_tree_view.column("kilomet", width=150, anchor=CENTER)
        booking_table_tree_view.column("drivername", width=200, anchor=CENTER)

        booking_table_tree_view.heading("#0", text="", anchor=CENTER)
        booking_table_tree_view.heading("cid", text="", anchor=CENTER)
        booking_table_tree_view.heading("bookingid", text="", anchor=CENTER)
        booking_table_tree_view.heading("did", text="", anchor=CENTER)
        booking_table_tree_view.heading("name", text="Khách hàng", anchor=CENTER)
        booking_table_tree_view.heading("credit", text="", anchor=CENTER)
        booking_table_tree_view.heading("date", text="Ngày đặt", anchor=CENTER)
        booking_table_tree_view.heading("time", text="Giờ đặt", anchor=CENTER)
        booking_table_tree_view.heading("pickupaddress", text="Điểm đón", anchor=CENTER)
        booking_table_tree_view.heading(
            "dropoffaddress", text="Điểm đến", anchor=CENTER
        )
        booking_table_tree_view.heading("kilomet", text="Cây số", anchor=CENTER)
        booking_table_tree_view.heading("drivername", text="Tên tài xế", anchor=CENTER)

        def get_select_item(a):
            name_txt.delete(0, END)
            credit_txt.delete(0, END)
            bookingid.delete(0, END)
            pick_up_address_txt.delete(0, END)
            drop_off_address_txt.delete(0, END)
            drop_off_address_txt.delete(0, END)
            km_txt.delete(0, END)
            date_txt.delete(0, END)
            time_txt.delete(0, END)

            select_item = booking_table_tree_view.selection()[0]
            name_txt.insert(0, booking_table_tree_view.item(select_item)["values"][3])
            credit_txt.insert(0, booking_table_tree_view.item(select_item)["values"][4])
            bookingid.insert(0, booking_table_tree_view.item(select_item)["values"][1])

            pick_up_address_txt.insert(
                0, booking_table_tree_view.item(select_item)["values"][7]
            )
            drop_off_address_txt.insert(
                0, booking_table_tree_view.item(select_item)["values"][8]
            )
            km_txt.insert(0, booking_table_tree_view.item(select_item)["values"][9])
            date_txt.insert(0, booking_table_tree_view.item(select_item)["values"][5])
            time_txt.insert(0, booking_table_tree_view.item(select_item)["values"][6])

        booking_table_tree_view.bind("<<TreeviewSelect>>", get_select_item)

        def billing_tabel():
            bill720 = billing_table()

            for b in bill720:
                booking_table_tree_view.insert(
                    parent="",
                    index="end",
                    values=(
                        b[0],
                        b[1],
                        b[2],
                        b[3],
                        b[4],
                        b[5],
                        b[6],
                        b[7],
                        b[8],
                        b[9],
                        b[10],
                    ),
                )

        billing_tabel()


if __name__ == "__main__":
    main = customtkinter.CTk()
    AdminPayment(main)
    main.mainloop()
