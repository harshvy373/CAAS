import mysql.connector as con_obj

conn=""
cursor_obj=""
def connect():
    global conn, cursor_obj
    conn = con_obj.connect(
        host="185.210.145.52",
        user="u649387556_iproject",
        password="Remal@123",
        database="u649387556_ipproject"
    )
    cursor_obj = conn.cursor()

def select(q):
    connect()
    global conn, cursor_obj
    cursor_obj.execute(q)
    result=cursor_obj.fetchall()
    for x in result:
        return x

def ftcall(q):
    connect()
    global conn, cursor_obj
    cursor_obj.execute(q)
    result=cursor_obj.fetchall()
    return result

def find(q):
    connect()
    global conn, cursor_obj
    cursor_obj.execute(q)
    result=cursor_obj.fetchall()
    count=0
    for x in result:
        count+=1
    return count
    
def insert(q):
    connect()
    global conn, cursor_obj
    #conn.reconnect(attempts=1, delay=0)
    cursor_obj.execute(q)
    conn.commit()

def delete():
    global conn, cursor_obj


