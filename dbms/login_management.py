from dbms.connection import Connect
import sys


def login(login_info):
    conn = None
    sql = "SELECT * FROM customers WHERE email = %s AND password = %s"
    values = (
        login_info.getEmail(),
        login_info.getPassword(),
    )
    user = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        user = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql
        del conn
        return user


def driver_login(driver_info):
    sql = "SELECT * FROM drivers WHERE email = %s AND password = %s"
    values = (
        driver_info.getEmail(),
        driver_info.getPassword(),
    )
    driver_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        driver_result = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql
        return driver_result


def admin_login(admin_info):
    sql = "SELECT * FROM admin WHERE email = %s AND password = %s"
    values = (
        admin_info.getEmail(),
        admin_info.getPassword(),
    )
    admin_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        admin_result = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql
        return admin_result
