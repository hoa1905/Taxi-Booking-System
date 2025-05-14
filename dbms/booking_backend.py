from dbms.connection import Connect
import sys


def insert_booking(booking_info):
    conn = None
    sql = """
        INSERT INTO booking (
            pickupaddress,
            date,
            time,
            dropoffaddress,
            bookingstatus,
            cid,
            did,
            kilomet
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        booking_info.getPickupaddress(),
        booking_info.getDate(),
        booking_info.getTime(),
        booking_info.getDropoffaddress(),
        booking_info.getBookingstatus(),
        booking_info.getCid(),
        booking_info.getDid(),
        booking_info.getKilomet(),
    )
    insert_result = False

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        insert_result = True
    except Exception as e:
        print("Lỗi khi thêm booking:", e)
        print("Chi tiết:", sys.exc_info())
    finally:
        if conn:
            conn.close()
        return insert_result


def update_booking(booking_info):
    conn = None
    sql = """
        UPDATE booking
        SET pickupaddress = %s, date = %s, time = %s, dropoffaddress = %s,
            bookingstatus = %s, cid = %s, did = %s
        WHERE bookingid = %s
    """
    values = (
        booking_info.getPickupaddress(),
        booking_info.getDate(),
        booking_info.getTime(),
        booking_info.getDropoffaddress(),
        booking_info.getBookingstatus(),
        booking_info.getCid(),
        booking_info.getDid(),
        booking_info.getBookingid(),
    )
    update_booking_result = False

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        update_booking_result = True
    except Exception as e:
        print("Lỗi khi cập nhật booking:", e)
        print("Chi tiết:", sys.exc_info())
    finally:
        if conn:
            conn.close()
        return update_booking_result


def select_all():
    conn = None
    sql = "SELECT * FROM booking WHERE bookingstatus = 'Đang xử lý'"
    book_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        book_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return book_result


def total_booking():
    conn = None
    sql = "SELECT COUNT(bookingid) FROM booking"
    booking_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        booking_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return booking_result


def customer_booking_select_all(cid):
    conn = None
    sql = "SELECT * FROM booking WHERE cid = %s"
    values = (cid,)
    book_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        book_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return book_result


def driver_update_booking(booking_info):
    conn = None
    sql = "UPDATE booking SET bookingstatus = %s WHERE bookingid = %s"
    values = (booking_info.getBookingstatus(), booking_info.getBookingid())
    update_booking_result = False

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        update_booking_result = True
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return update_booking_result


def customer_booking_select_status_pending(cid):
    conn = None
    sql = "SELECT * FROM booking WHERE cid = %s AND bookingstatus = 'Đang xử lý'"
    values = (cid,)
    book_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        book_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return book_result


def delete_booking(bookingID):
    conn = None
    sql = "DELETE FROM booking WHERE bookingid = %s"
    values = (bookingID,)
    delete_result = False

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        delete_result = True
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return delete_result


def customer_check_booking(cidInfo):
    conn = None
    check_result = None
    sql = """
        SELECT date
        FROM booking
        WHERE cid = %s AND date = %s AND bookingstatus = 'Đang xử lý'
    """
    values = (cidInfo.getCid(), cidInfo.getDate())

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        check_result = cursor.fetchone()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return check_result


def assigned_status_booking():
    conn = None
    active_result = None
    sql = """
        SELECT
            booking.bookingid,
            customers.name,
            booking.pickupaddress, 
            booking.dropoffaddress,
            booking.date,
            booking.time,
            drivers.name,
            booking.bookingstatus,
            booking.kilomet
        FROM booking
        INNER JOIN customers ON booking.cid = customers.cid
        INNER JOIN drivers ON booking.did = drivers.did
        WHERE booking.bookingstatus = 'Đã phân công'
    """

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        active_result = cursor.fetchall()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return active_result


def total_revenue():
    conn = None
    sql = "SELECT SUM(total) FROM billing"
    total_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        total_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return total_result


def validate_admin_booking():
    conn = None
    sql = "SELECT date FROM booking WHERE bookingstatus = 'Đang xử lý'"
    validate_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        validate_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return validate_result


def cancel_status_booking_update(bid):
    conn = None
    sql = "UPDATE booking SET bookingstatus = 'Bị hủy' WHERE bookingid = %s"
    values = (bid,)
    update_booking_result = False

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        update_booking_result = True
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return update_booking_result
