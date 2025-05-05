from tkinter import *
import customtkinter
from PIL import Image
from tkinter import ttk
from dbms.driver_management import (
    select_all_driver,
    driver_select_all22,
)


class SearchDrivers:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )
        self.main.title("Hệ thống đặt xe taxi | Tìm kiếm tài xế")
        self.main.resizable(0, 0)
        frame_width = 1000
        frame_height = 500
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        self.main.geometry(
            "{}x{}+{}+{}".format(
                frame_width, frame_height, x_cordinate + 200, y_cordinate
            )
        )

        font720 = customtkinter.CTkFont(
            family="Times New Roman", size=20, weight="bold"
        )

        top_frame = customtkinter.CTkFrame(self.main, height=80)
        top_frame.pack(side=TOP, fill=BOTH)

        # ++++++++++++++++++++++++++++ID Label+++++++++++++++++++++++++++++++++++++
        id_lbl = customtkinter.CTkLabel(
            master=top_frame, text="Tìm kiếm: ", font=font720
        )
        id_lbl.place(x=20, y=20)

        # ++++++++++++++++++++++++++++++ID TextField++++++++++++++++++++++++++++++++++++++++++++++++++
        id_txt = customtkinter.CTkEntry(
            master=top_frame, font=font720, placeholder_text="Tên tài xế", width=200
        )
        id_txt.place(x=100, y=20)

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
        tree_view.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        tree_view["columns"] = (
            "did",
            "name",
            "mobile",
            "email",
            "license",
            "driverstatus",
        )
        tree_view.column("#0", width=0, stretch=0)
        tree_view.column("did", width=100, anchor=CENTER)
        tree_view.column("name", width=150, anchor=CENTER)
        tree_view.column("mobile", width=100, anchor=CENTER)
        tree_view.column("email", width=100, anchor=CENTER)
        tree_view.column("license", width=100, anchor=CENTER)
        tree_view.column("driverstatus", width=200, anchor=CENTER)

        tree_view.heading("#0", text="", anchor=CENTER)
        tree_view.heading("did", text="Mã tài xế", anchor=CENTER)
        tree_view.heading("name", text="Name", anchor=CENTER)
        tree_view.heading("mobile", text="SĐT", anchor=CENTER)
        tree_view.heading("email", text="Email", anchor=CENTER)
        tree_view.heading("license", text="Số bằng lái xe", anchor=CENTER)
        tree_view.heading("driverstatus", text="Trạng thái tài xế", anchor=CENTER)

        def search_driver1():
            result = select_all_driver()
            for x in result:
                tree_view.insert(
                    parent="", index="end", values=(x[0], x[1], x[2], x[3], x[4], x[6])
                )

        search_driver1()

        def search():
            val = id_txt.get()
            driver_result = driver_select_all22(val)
            tree_view.delete(*tree_view.get_children())

            for xx in driver_result:
                tree_view.insert(
                    parent="",
                    index="end",
                    values=(xx[0], xx[1], xx[2], xx[3], xx[4], xx[6]),
                )

        search_image = customtkinter.CTkImage(
            light_image=Image.open(
                "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/search-alt-2-regular-24.png"
            )
        )
        delete_btn = customtkinter.CTkButton(
            master=top_frame,
            command=search,
            image=search_image,
            text="Tìm kiếm",
            font=font720,
            width=180,
        )
        delete_btn.place(x=320, y=20)


if __name__ == "__main__":
    main = customtkinter.CTk()
    SearchDrivers(main)
    main.mainloop()
