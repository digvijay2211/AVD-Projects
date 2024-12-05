from sqlconnection import *
cursor,conn=connection()

def insert_opration():
    str1 = input("enter the table name:")
    # no_col=int(input("how many colume are to be changed"))

    col_name = input("enter the colum name in sequence :")
    value = input("enter the value: ")

    str = f"insert into {str1}({col_name}) values({value})"

    print(str)
    cursor.execute(str)
    conn.commit()
    print("insert succesfully")

cursor.close()
conn.close()