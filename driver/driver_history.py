from tkinter import *
import customtkinter
from tkinter import ttk

from dbms.driver_history_backend import customer_driver_history
from libs import Global


class DriverHistory:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.title("Lịch sử tài xế")
        self.main.resizable(0, 0)
        frame_width = 900
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
            text="Lịch sử tài xế",
            font=font1,
        )
        title_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        style1 = ttk.Style()
        style1.theme_use("default")
        style1.configure(
            "Tree_view",
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
            "did",
            "drivername",
            "date",
            "time",
            "pickupaddress",
            "dropoffaddress",
            "mobile",
        )
        tree_view.column("#0", width=0, stretch=0)
        tree_view.column("did", width=100, anchor=CENTER)
        tree_view.column("drivername", width=100, anchor=CENTER)
        tree_view.column("date", width=100, anchor=CENTER)
        tree_view.column("time", width=100, anchor=CENTER)
        tree_view.column("pickupaddress", width=100, anchor=CENTER)
        tree_view.column("dropoffaddress", width=100, anchor=CENTER)
        tree_view.column("mobile", width=100, anchor=CENTER)

        tree_view.heading("#0", text="", anchor=CENTER)
        tree_view.heading("did", text="Mã tài xế", anchor=CENTER)
        tree_view.heading("drivername", text="Tên tài xế", anchor=CENTER)
        tree_view.heading("date", text="Ngày đặt", anchor=CENTER)
        tree_view.heading("time", text="Giờ đặt", anchor=CENTER)
        tree_view.heading("pickupaddress", text="Điểm đón", anchor=CENTER)
        tree_view.heading("dropoffaddress", text="Điểm đến", anchor=CENTER)
        tree_view.heading("mobile", text="SĐT", anchor=CENTER)

        customer_id = Entry(self.main)
        customer_id.insert(0, Global.current_user[0])

        def booking_history():
            customer_idd = customer_id.get()

            history_result = customer_driver_history(customer_idd)

            for ro in history_result:
                tree_view.insert(
                    parent="",
                    index="end",
                    values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]),
                )

        booking_history()


if __name__ == "__main__":
    main = customtkinter.CTk()
    DriverHistory(main)
    main.mainloop()
