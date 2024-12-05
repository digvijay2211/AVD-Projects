import pymysql
import numpy as np
conn = pymysql.connect(host='localhost', database='practical', user='root', password='prasad@1997')
cursor=conn.cursor()

def insert_opration():
    str1 = str(input("enter the table name:"))
    # no_col=int(input("how many colume are to be changed"))

    col_name = (input("enter the colum name in sequence :"))
    value = (input("enter the value"))

    str = f"insert into {str1}({col_name}) values({value})"

    cursor.execute(str)
    conn.commit()
    print("insert succesfully")

insert_opration()
cursor.close()
conn.close()