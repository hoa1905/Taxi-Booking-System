import sys
from dbms.connection import Connect


def total_customer():
    conn = None
    sql = "SELECT COUNT(cid) FROM customers"
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


def select_all_customer():
    conn = None
    sql = "SELECT * FROM customers"
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


# def validate_customer_booking(cid):
#     conn = None
#     sql = "SELECT date FROM booking WHERE cid = %s AND bookingstatus = 'Pending'"
#     values = (cid,)
#     validate_result = None

#     try:
#         conn = Connect()
#         cursor = conn.cursor()
#         cursor.execute(sql, values)
#         validate_result = cursor.fetchall()
#         cursor.close()
#         conn.close()
#     except:
#         print("Lỗi", sys.exc_info())
#     finally:
#         del sql, conn
#         return validate_result
