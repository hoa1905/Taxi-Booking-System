from tkinter import *
import customtkinter
from tkinter import ttk
from dbms.booking_backend import customer_booking_select_all
from libs import Global


class CustomerBookingHistory:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.title("Lịch sử đặt xe taxi")
        self.main.resizable(0, 0)
        frame_width = 1050
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

        # +++++++++++++++++++++++++++++Getting customer id using global++++++++++++++++++++++++++++
        customerid = customtkinter.CTkEntry(master=self.main)
        customerid.insert(0, Global.current_user[0])

        top_frame = customtkinter.CTkFrame(self.main, height=80)
        top_frame.pack(side=TOP, fill=BOTH)

        title_label = customtkinter.CTkLabel(
            top_frame,
            text="Lịch sử đặt xe taxi",
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
            "bookingid",
            "pickupaddress",
            "dropoffaddress",
            "date",
            "time",
        )
        tree_view.column("#0", width=0, stretch=0)
        tree_view.column("bookingid", width=100, anchor=CENTER)
        tree_view.column("pickupaddress", width=100, anchor=CENTER)
        tree_view.column("dropoffaddress", width=100, anchor=CENTER)
        tree_view.column("date", width=100, anchor=CENTER)
        tree_view.column("time", width=100, anchor=CENTER)

        tree_view.heading("#0", text="", anchor=CENTER)
        tree_view.heading("bookingid", text="Mã đặt xe taxi", anchor=CENTER)
        tree_view.heading("pickupaddress", text="Điểm đón", anchor=CENTER)
        tree_view.heading("dropoffaddress", text="Điểm đến", anchor=CENTER)
        tree_view.heading("date", text="Ngày đặt", anchor=CENTER)
        tree_view.heading("time", text="Giờ đặt", anchor=CENTER)
        tree_view.pack(side=TOP, fill=BOTH, expand=TRUE)

        def booking_history():
            book_result = customer_booking_select_all(customerid.get())

            for x in book_result:
                tree_view.insert(
                    parent="", index="end", values=(x[0], x[1], x[4], x[2], x[3])
                )

        booking_history()


if __name__ == "__main__":
    main = customtkinter.CTk()
    CustomerBookingHistory(main)
    main.mainloop()
