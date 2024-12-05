from sqlconnection import *

cursor, conn = connection()

def delete_rows():
    id = int(input('enter no: '))
    str = "delete from city where id ='%d'"  # execute this SQL command at db server
    args = id

    cursor.execute(str %args)

    conn.commit()
    print('1 row is deleted')

#update rows
def update_rows():
    id = int(input('enter no: '))
    col_name =input("enter column name: ")
    col_value = input("enter value: ")

    str = f"update city set {col_name}='{col_value}' where id ={id}"  # execute this SQL command at db server

    print(str)
    cursor.execute(str)
    conn.commit()
    print('1 row is updated')


# close connection
def close():
    cursor.close()
    conn.close()
    print("connection close")


