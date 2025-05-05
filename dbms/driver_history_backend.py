from dbms.connection import Connect
import sys


def customer_driver_history(cid):
    conn = None
    sql = """
        SELECT booking.did, drivers.name, booking.date, booking.time,
            booking.pickupaddress, booking.dropoffaddress, drivers.mobile
        FROM customers
        INNER JOIN booking ON customers.cid = booking.cid
        INNER JOIN drivers ON booking.did = drivers.did where customers.cid = %s
        ORDER BY booking.bookingid DESC
    """
    values = (cid,)
    history_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        history_result = cursor.fetchall()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return history_result
