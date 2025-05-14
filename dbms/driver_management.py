from dbms.connection import Connect
import sys


def insert_record(driver_info):
    conn = None
    sql = "INSERT INTO drivers VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (
        driver_info.getDid(),
        driver_info.getName(),
        driver_info.getMobile(),
        driver_info.getEmail(),
        driver_info.getLicense(),
        driver_info.getPassword(),
        driver_info.getDriverstatus(),
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
        del sql
        del conn
        return result


def search_record(did):
    conn = None
    sql = "SELECT * FROM drivers WHERE did = %s"
    values = (did,)
    search_result = None
    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        search_result = cursor.fetchone()
        cursor.close()
        conn.close()

    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return search_result


def delete_record(did):
    conn = None
    sql = "DELETE FROM drivers WHERE did = %s"
    values = (did,)
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


def update_record(driver_info):
    conn = None
    sql = "UPDATE drivers SET name = %s, mobile = %s, email = %s, license = %s WHERE did = %s"
    values = (
        driver_info.getName(),
        driver_info.getMobile(),
        driver_info.getEmail(),
        driver_info.getLicense(),
        driver_info.getDid(),
    )
    update_result = False

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        update_result = True
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return update_result


def update_driver_status(driver_info):
    conn = None
    sql = "UPDATE drivers SET driverstatus = %s WHERE did = %s"
    values = (driver_info.getDriverstatus(), driver_info.getDid())
    update_result = False

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        update_result = True
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return update_result


def driver_select_all(driverID):
    conn = None
    sql = "SELECT * FROM drivers WHERE did = %s"
    values = (driverID,)
    select_desult = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        select_desult = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return select_desult


def total_driver():
    conn = None
    sql = "SELECT COUNT(did) FROM drivers"
    driver_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        driver_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return driver_result


def available_driver():
    conn = None
    sql = "SELECT * FROM drivers WHERE driverstatus = 'Hoạt động'"
    available_driver = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        available_driver = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return available_driver


def select_all_driver():
    conn = None
    sql = "SELECT * FROM drivers"
    available_driver = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        available_driver = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return available_driver


def driver_select_all_booking(did):
    conn = None
    sql = """
        SELECT booking.bookingid, booking.pickupaddress, booking.date,
            booking.time, booking.dropoffaddress, customers.name, booking.bookingstatus, booking.kilomet
        FROM booking
        INNER JOIN customers ON booking.cid = customers.cid
        WHERE booking.did = %s AND booking.bookingstatus = 'Đã phân công'
    """
    values = (did,)
    driver_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        driver_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return driver_result


def driver_select_all22(name11):
    conn = None
    sql = "SELECT * FROM drivers WHERE name LIKE '%{}%'".format(name11)
    select_desult = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        select_desult = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return select_desult


def driver_trip_history(did):
    conn = None
    sql = """
        SELECT customers.cid, customers.name, booking.date,
            booking.time, booking.pickupaddress, booking.dropoffaddress, booking.kilomet
        FROM booking
        INNER JOIN customers ON booking.cid = customers.cid
        WHERE booking.did = %s AND booking.bookingstatus = 'Chưa thanh toán'
    """
    values = (did,)
    driver_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        driver_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return driver_result


def driver_password_change(Driver):
    conn = None
    sql = "UPDATE drivers SET password = %s WHERE did = %s"
    values = (Driver.getPassword(), Driver.getDid())
    change_password_result = False

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        change_password_result = True
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return change_password_result
