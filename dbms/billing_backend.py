from dbms.connection import Connect
import sys


def insert_billing(billing_id):
    conn = None
    sql = "INSERT INTO billing (name, km, unit, total, bookingid, date) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (
        billing_id.getName(),
        billing_id.getKm(),
        billing_id.getUnit(),
        billing_id.getTotal(),
        billing_id.getBookingid(),
        billing_id.getDate(),
    )
    result = False

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return result


def billing_table():
    conn = None
    sql = """
        SELECT 
            customers.cid, 
            booking.bookingid, 
            booking.did, 
            customers.name AS customer_name, 
            customers.credit, 
            booking.date,
            booking.time, 
            booking.pickupaddress, 
            booking.dropoffaddress, 
            booking.kilomet,
            drivers.name AS driver_name
        FROM booking
        LEFT JOIN customers ON booking.cid = customers.cid
        LEFT JOIN drivers ON booking.did = drivers.did
        WHERE booking.bookingstatus = 'Chưa thanh toán'
    """
    result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return result


def billing_history12():
    conn = None
    sql = """
        SELECT 
            b.bookingid, 
            c.name AS customer_name, 
            b.pickupaddress, 
            b.dropoffaddress, 
            b.date, 
            b.time, 
            bl.km, 
            bl.unit, 
            bl.total 
        FROM booking b
        LEFT JOIN billing bl ON b.bookingid = bl.bookingid 
        LEFT JOIN customers c ON b.cid = c.cid 
        WHERE b.bookingstatus = 'Đã thanh toán'
    """
    billing_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        billing_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return billing_result


def customer_billing_history(customer_info):
    conn = None
    sql = """
        SELECT
            booking.pickupaddress,
            booking.dropoffaddress,
            booking.date,
            booking.time,
            billing.km,
            billing.unit,
            billing.total
        FROM booking
        INNER JOIN billing ON booking.bookingid = billing.bookingid
        WHERE booking.cid = %s
    """
    values = (customer_info,)
    billing_history = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        billing_history = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return billing_history
