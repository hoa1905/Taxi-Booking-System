import sys
from dbms.connection import Connect


def insert_record(customer_info):
    conn = None
    sql = """
        INSERT INTO customers (
            name, dob, gender, mobile, email, address, password, credit, status
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        customer_info.getName(),
        customer_info.getDob(),
        customer_info.getGender(),
        customer_info.getMobile(),
        customer_info.getEmail(),
        customer_info.getAddress(),
        customer_info.getPassword(),
        customer_info.getCredit(),
        customer_info.getStatus(),
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


def update_record(customer_info):
    conn = None
    sql = """
        UPDATE customers
        SET name = %s, dob = %s, gender = %s, mobile = %s, email = %s,
            address = %s,credit = %s, status = %s WHERE cid = %s
    """
    values = (
        customer_info.getName(),
        customer_info.getDob(),
        customer_info.getGender(),
        customer_info.getMobile(),
        customer_info.getEmail(),
        customer_info.getAddress(),
        customer_info.getCredit(),
        customer_info.getStatus(),
        customer_info.getCid(),
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
        del sql
        del conn
        return update_result


def search_customer(cid):
    conn = None
    sql = "SELECT * FROM customers WHERE cid = %s"
    values = (cid,)
    customer_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        customer_result = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return customer_result


def delete_record(cid):
    conn = None
    sql = "DELETE FROM customers WHERE cid = %s"
    values = (cid,)
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


def search_customer2(name12):
    conn = None
    sql = "SELECT * FROM customers WHERE name LIKE '%{}%'".format(name12)
    customer_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        customer_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return customer_result


def update_customer_record(customer_info):
    conn = None
    sql = """
        UPDATE customers
        SET name = %s, dob = %s, gender = %s, mobile = %s,
            email = %s, address = %s,credit = %s WHERE cid = %s
    """
    values = (
        customer_info.getName(),
        customer_info.getDob(),
        customer_info.getGender(),
        customer_info.getMobile(),
        customer_info.getEmail(),
        customer_info.getAddress(),
        customer_info.getCredit(),
        customer_info.getCid(),
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
        del sql
        del conn
        return update_result
