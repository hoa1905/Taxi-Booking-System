from tkinter import *
import customtkinter
from tkinter import ttk
from dbms.booking_backend import assigned_status_booking


class ActiveBooking:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.title("Thông tin phân công tài xế")
        self.main.resizable(0, 0)
        frame_width = 1350
        frame_height = 500
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.main.geometry(
            "{}x{}+{}+{}".format(
                frame_width, frame_height, x_cordinate + 50, y_cordinate + 50
            )
        )
        self.main.bind("<Escape>", lambda e: self.main.destroy())
        self.main.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )

        font1 = customtkinter.CTkFont(family="Times New Roman", size=30, weight="bold")

        top_frame = customtkinter.CTkFrame(self.main, height=80)
        top_frame.pack(side=TOP, fill=BOTH)

        titlelabel = customtkinter.CTkLabel(
            top_frame, text="THÔNG TIN PHÂN CÔNG TÀI XẾ", font=font1
        )
        titlelabel.place(relx=0.5, rely=0.5, anchor=CENTER)

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

        treeView = ttk.Treeview(self.main)
        treeView.pack(side=BOTTOM, fill=BOTH, expand=True)
        treeView["columns"] = (
            "bookingid",
            "customername",
            "pickupaddress",
            "dropoffaddress",
            "kilomet",
            "date",
            "time",
            "drivername",
            "bookingstatus",
        )
        treeView.column("#0", width=0, stretch=0)
        treeView.column("bookingid", width=100, anchor=CENTER)
        treeView.column("customername", width=200, anchor=CENTER)
        treeView.column("pickupaddress", width=200, anchor=CENTER)
        treeView.column("dropoffaddress", width=200, anchor=CENTER)
        treeView.column("kilomet", width=150, anchor=CENTER)
        treeView.column("date", width=100, anchor=CENTER)
        treeView.column("time", width=100, anchor=CENTER)
        treeView.column("drivername", width=100, anchor=CENTER)
        treeView.column("bookingstatus", width=100, anchor=CENTER)

        treeView.heading("#0", text="", anchor=CENTER)
        treeView.heading("bookingid", text="Mã đặt xe", anchor=CENTER)
        treeView.heading("customername", text="Tên khách hàng", anchor=CENTER)
        treeView.heading("pickupaddress", text="Điểm đón", anchor=CENTER)
        treeView.heading("dropoffaddress", text="Điểm đến", anchor=CENTER)
        treeView.heading("kilomet", text="Cây số", anchor=CENTER)
        treeView.heading("date", text="Ngày đặt", anchor=CENTER)
        treeView.heading("time", text="Giờ đặt", anchor=CENTER)
        treeView.heading("drivername", text="Tên tài xế", anchor=CENTER)
        treeView.heading("bookingstatus", text="Trạng thái", anchor=CENTER)

        def booking_table():

            active_result = assigned_status_booking()

            for ro in active_result:
                treeView.insert(
                    parent="",
                    index="end",
                    values=(
                        ro[0],
                        ro[1],
                        ro[2],
                        ro[3],
                        ro[8],
                        ro[4],
                        ro[5],
                        ro[6],
                        ro[7],
                    ),
                )

        booking_table()


if __name__ == "__main__":
    main = customtkinter.CTk()
    ActiveBooking(main)
    main.mainloop()
