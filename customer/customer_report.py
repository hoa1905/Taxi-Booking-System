from tkinter import *
import pandas
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter


class CustomerReport:
    def __init__(self, main):
        self.main = main
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.main.title("Thống kê khách hàng")
        self.main.iconbitmap(
            "D:/VKU/Nam IV_Ky II/Lap trinh Python/Cuoi ky/Taxi Booking System/Images/logo.ico"
        )
        self.main.title("Hệ thống đặt xe taxi | Thống kê khách hàng")
        self.main.resizable(0, 0)
        frame_width = 900
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

        font1 = customtkinter.CTkFont(family="Times New Roman", size=30, weight="bold")

        top_frame = customtkinter.CTkFrame(self.main, height=100)
        top_frame.pack(side=TOP, fill=BOTH)

        title_label = customtkinter.CTkLabel(
            top_frame, text="THỐNG KÊ KHÁCH HÀNG", font=font1
        )
        title_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        frame = Frame(self.main, bg="white")
        frame.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

        try:
            sql_engine = create_engine(
                "mysql+pymysql://root:Hoa30025091@localhost/taxi_booking_system"
            )
            db_connection = sql_engine.connect()
            print("Kết nối CSDL thành công.")
        except SQLAlchemyError as e:
            print("Kết nối CSDL thất bại:", e)

        query = "SELECT gender, COUNT(cid) as Customer FROM customers GROUP BY gender"
        df = pandas.read_sql(query, db_connection, index_col="gender")
        fig = df.plot.pie(
            title="Số lượng khách hàng theo giới tính",
            y="Customer",
            autopct="%1.0f%%",
            figsize=(5, 5),
        ).get_figure()
        plot2 = FigureCanvasTkAgg(fig, frame)
        plot2.get_tk_widget().place(x=20, y=30)

        query2 = "SELECT *, COUNT(cid) as ID FROM booking GROUP BY date"
        df2 = pandas.read_sql(query2, db_connection, index_col="date")
        fig2 = df2.plot.line(
            title="Phân tích đặt xe hàng ngày", y="ID", figsize=(5, 5)
        ).get_figure()
        plot2 = FigureCanvasTkAgg(fig2, frame)
        plot2.get_tk_widget().place(x=550, y=0)


if __name__ == "__main__":
    main = customtkinter.CTk()
    CustomerReport(main)
    main.mainloop()
