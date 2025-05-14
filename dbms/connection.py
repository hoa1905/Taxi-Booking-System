import mysql.connector
import sys


def Connect():
    conn = None

    try:
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Hoa30025091",
            database="taxi_booking_system",
        )
    except:
        print("Lỗi", sys.exc_info())
    finally:
        return conn
