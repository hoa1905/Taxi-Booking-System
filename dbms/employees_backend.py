import sys
from dbms.connection import Connect


def insert_record(employees_info):
    conn = None
    sql = "INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (
        employees_info.getEmid(),
        employees_info.getName(),
        employees_info.getDob(),
        employees_info.getGender(),
        employees_info.getMobile(),
        employees_info.getEmail(),
        employees_info.getAddress(),
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


def update_record(employees_info):
    conn = None
    sql = "UPDATE employees SET name = %s, dob = %s, gender = %s, mobile = %s, email = %s, address = %s WHERE emid = %s"
    values = (
        employees_info.getName(),
        employees_info.getDob(),
        employees_info.getGender(),
        employees_info.getMobile(),
        employees_info.getEmail(),
        employees_info.getAddress(),
        employees_info.getEmid(),
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


def search_employees(emid):
    conn = None
    sql = "SELECT * FROM employees WHERE emid = %s"
    values = (emid,)
    employees_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        employees_result = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del values, sql, conn
        return employees_result


def delete_record(emid):
    conn = None
    sql = "DELETE FROM employees WHERE emid = %s"
    values = (emid,)
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


def total_employees():
    conn = None
    sql = "SELECT COUNT(emid) FROM employees"
    employees_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        employees_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return employees_result


def select_allemployees():
    conn = None
    sql = "SELECT * FROM employees"
    employees_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        employees_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return employees_result


def search_employees111(name11):
    conn = None
    sql = "SELECT * FROM employees WHERE name LIKE '%{}%'".format(name11)
    employees_result = None

    try:
        conn = Connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        employees_result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Lỗi", sys.exc_info())
    finally:
        del sql, conn
        return employees_result
