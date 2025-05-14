from tkinter import *
import customtkinter
from tkinter import ttk
from dbms.billing_backend import billing_history12


class AdminBillingHistory:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.title("Lịch sử hóa đơn của khách hàng")
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
            top_frame, text="Lịch sử hóa đơn của khách hàng", font=font1
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
            "name",
            "pickupaddress",
            "dropoffaddress",
            "date",
            "time",
            "km",
            "unit",
            "total",
        )
        tree_view.column("#0", width=0, stretch=0)
        tree_view.column("bookingid", width=100, anchor=CENTER)
        tree_view.column("name", width=200, anchor=CENTER)
        tree_view.column("pickupaddress", width=200, anchor=CENTER)
        tree_view.column("dropoffaddress", width=200, anchor=CENTER)
        tree_view.column("date", width=100, anchor=CENTER)
        tree_view.column("time", width=100, anchor=CENTER)
        tree_view.column("km", width=100, anchor=CENTER)
        tree_view.column("unit", width=100, anchor=CENTER)
        tree_view.column("total", width=300, anchor=CENTER)

        tree_view.heading("#0", text="", anchor=CENTER)
        tree_view.heading("bookingid", text="Mã đặt xe", anchor=CENTER)
        tree_view.heading("name", text="Tên khách hàng", anchor=CENTER)
        tree_view.heading("pickupaddress", text="Điểm đón", anchor=CENTER)
        tree_view.heading("dropoffaddress", text="Điểm đến", anchor=CENTER)
        tree_view.heading("date", text="Ngày đặt", anchor=CENTER)
        tree_view.heading("time", text="Giờ đặt", anchor=CENTER)
        tree_view.heading("km", text="KM", anchor=CENTER)
        tree_view.heading("unit", text="Đơn vị", anchor=CENTER)
        tree_view.heading("total", text="Tổng", anchor=CENTER)

        def format_currency(value):
            if value is None:
                return ""
            try:
                return "{:,.0f}".format(float(value)).replace(",", ".")
            except ValueError:
                return value

        def billing_table():
            history_result = billing_history12()
            for ro in history_result:
                tree_view.insert(
                    parent="",
                    index="end",
                    values=(
                        ro[0],
                        ro[1],
                        ro[2],
                        ro[3],
                        ro[4],
                        ro[5],
                        ro[6],
                        format_currency(ro[7]),
                        format_currency(ro[8]),
                    ),
                )

        billing_table()

        def get_sum(item=""):
            val = 0
            for row in tree_view.get_children(item):
                try:
                    value = tree_view.item(row)["values"][8]
                    # Nếu value là dạng chuỗi có định dạng kiểu VN (1.200,50)
                    value = str(value).replace(".", "").replace(",", ".").strip()
                    val += float(value)
                except (ValueError, IndexError, TypeError):
                    pass  # Bỏ qua nếu giá trị không hợp lệ

            # Thêm dòng hiển thị tổng cộng vào cuối
            tree_view.insert(
                parent="",
                index="end",
                values=(
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Tổng cộng: {:,}".format(int(val)).replace(",", ".") + " VND",
                ),
            )

        get_sum()


if __name__ == "__main__":
    main = customtkinter.CTk()
    AdminBillingHistory(main)
    main.mainloop()
