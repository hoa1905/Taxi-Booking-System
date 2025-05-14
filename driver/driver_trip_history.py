from tkinter import *
import customtkinter
from tkinter import ttk
from dbms.driver_management import driver_trip_history
from libs import Global


class DriverHistory:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.title("Lịch sử chuyến đi")
        self.main.resizable(0, 0)
        frame_width = 1100
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

        title_label = customtkinter.CTkLabel(
            top_frame,
            text="Lịch sử chuyển đi của tài xế {}".format(Global.current_driver[1]),
            font=font1,
        )
        title_label.place(relx=0.5, rely=0.5, anchor=CENTER)

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

        tree_view = ttk.Treeview(self.main)
        tree_view.pack(side=BOTTOM, fill=BOTH, expand=True)
        tree_view["columns"] = (
            "cid",
            "name",
            "date",
            "time",
            "pickupaddress",
            "dropoffaddress",
            "kilomet",
            "price",
        )
        tree_view.column("#0", width=0, stretch=0)
        tree_view.column("cid", width=100, anchor=CENTER)
        tree_view.column("name", width=100, anchor=CENTER)
        tree_view.column("date", width=100, anchor=CENTER)
        tree_view.column("time", width=100, anchor=CENTER)
        tree_view.column("pickupaddress", width=100, anchor=CENTER)
        tree_view.column("dropoffaddress", width=100, anchor=CENTER)
        tree_view.column("kilomet", width=100, anchor=CENTER)
        tree_view.column("price", width=100, anchor=CENTER)

        tree_view.heading("#0", text="", anchor=CENTER)
        tree_view.heading("cid", text="Mã khách hàng", anchor=CENTER)
        tree_view.heading("name", text="Tên khách hàng", anchor=CENTER)
        tree_view.heading("date", text="Ngày đặt", anchor=CENTER)
        tree_view.heading("time", text="Giờ đặt", anchor=CENTER)
        tree_view.heading("pickupaddress", text="Điểm đón", anchor=CENTER)
        tree_view.heading("dropoffaddress", text="Điểm đến", anchor=CENTER)
        tree_view.heading("kilomet", text="Cây số", anchor=CENTER)
        tree_view.heading("price", text="Số tiền", anchor=CENTER)

        driver_id = Entry(self.main)
        driver_id.insert(0, Global.current_driver[0])

        def trip_history():
            id = driver_id.get()
            driver_result = driver_trip_history(id)

            for ro in driver_result:
                try:
                    kilometer = float(ro[6])
                    price = int(kilometer * 12000)
                    price_str = f"{price:,.0f}".replace(",", ".") + " VND"
                except:
                    price_str = "0" + " VND"

                tree_view.insert(
                    parent="",
                    index="end",
                    values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], price_str),
                )

        trip_history()


if __name__ == "__main__":
    main = customtkinter.CTk()
    DriverHistory(main)
    main.mainloop()
