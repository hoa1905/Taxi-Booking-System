import sys
from dbms.connection import Connect


def password_change(customerInfo):
    conn = None
    sql = "UPDATE customers SET password = %s WHERE cid = %s"
    values = (
        customerInfo.getPassword(),
        customerInfo.getCid(),
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
        print("Lỗi", sys.exc_value)
    finally:
        del values, sql, conn
        return result
