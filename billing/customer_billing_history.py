from tkinter import *
import customtkinter
from tkinter import ttk
from dbms.billing_backend import customer_billing_history
from libs import Global


class CustomerBillingHistory:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.title("Lịch sử hóa đơn")
        self.main.resizable(0, 0)
        frame_width = 1200
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
            text="Lịch sử hóa đơn",
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
            "pickupaddress",
            "dropoffaddress",
            "date",
            "time",
            "km",
            "unit",
            "total",
        )
        tree_view.column("#0", width=0, stretch=0)
        tree_view.column("pickupaddress", width=100, anchor=CENTER)
        tree_view.column("dropoffaddress", width=200, anchor=CENTER)
        tree_view.column("date", width=200, anchor=CENTER)
        tree_view.column("time", width=200, anchor=CENTER)
        tree_view.column("km", width=100, anchor=CENTER)
        tree_view.column("unit", width=100, anchor=CENTER)
        tree_view.column("total", width=250, anchor=CENTER)

        tree_view.heading("#0", text="", anchor=CENTER)
        tree_view.heading("pickupaddress", text="Điểm đón", anchor=CENTER)
        tree_view.heading("dropoffaddress", text="Điểm đến", anchor=CENTER)
        tree_view.heading("date", text="Ngày đặt", anchor=CENTER)
        tree_view.heading("time", text="Giờ đặt", anchor=CENTER)
        tree_view.heading("km", text="KM", anchor=CENTER)
        tree_view.heading("unit", text="Giá", anchor=CENTER)
        tree_view.heading("total", text="Tổng tiền", anchor=CENTER)

        customerid = Entry(self.main)
        customerid.insert(0, Global.current_user[0])

        def format_currency(value):
            if value is None:
                return ""
            try:
                return "{:,.0f}".format(float(value)).replace(",", ".")
            except ValueError:
                return value

        def billing_table():
            id = customerid.get()
            billingHistory = customer_billing_history(id)

            for ro in billingHistory:
                tree_view.insert(
                    parent="",
                    index="end",
                    values=(
                        ro[0],
                        ro[1],
                        ro[2],
                        ro[3],
                        ro[4],
                        format_currency(ro[5]),
                        format_currency(ro[6]),
                    ),
                )

        billing_table()

        def get_sum(item=""):
            val = 0
            for row in tree_view.get_children(item):
                # print(trv.item(row)["values"][3])# print price
                val = val + tree_view.item(row)["values"][6]
            print(val)
            tree_view.insert(
                parent="",
                index="end",
                values=("", "", "", "", "", "", "Tổng cộng: {} VND".format(val)),
            )

        get_sum()


if __name__ == "__main__":
    main = customtkinter.CTk()
    CustomerBillingHistory(main)
    main.mainloop()
