from dbms.connection import Connect
import sys


def driver_riding_total(did):
    conn = None
    sql = "SELECT COUNT(bookingid) FROM booking WHERE did = %s"
    values = (did,)
    result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return result


def driver_total_booked(did):
    conn = None
    sql = "SELECT COUNT(bookingid) FROM booking WHERE did = %s AND bookingstatus = 'Đã phân công'"
    values = (did,)
    result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return result


def driver_ride_completed(did):
    conn = None
    sql = "SELECT COUNT(bookingid) FROM booking WHERE did = %s AND bookingstatus = 'Đã thanh toán'"
    values = (did,)
    result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return result


def driver_ride_cancelled(did):
    conn = None
    sql = "SELECT COUNT(bookingid) FROM booking WHERE did = %s AND bookingstatus = 'Chưa hoàn thành'"
    values = (did,)
    result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return result
