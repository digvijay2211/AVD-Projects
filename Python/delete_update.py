#delete rows

import pymysql
 
def delete_rows(id):
    conn = pymysql.connect(host='localhost', database='assig', user='root', password='Admin@123')

    cursor = conn.cursor()  # create cursor object

    str = "delete from city where id ='%d'"  # execute this SQL command at db server
    args = (id)

    cursor.execute(str %args)

    conn.commit()
    print('1 row is deleted')

    cursor.close() 
    conn.close() 

x =int(input('enter no: '))
delete_rows(x)

#update rows


def update_rows(id):
    conn = pymysql.connect(host='localhost', database='assig', user='root', password='Admin@123')

    cursor = conn.cursor()  # create cursor object
    col_name =input("enter column name: ")
    col_value = input("enter value: ")

    str = f"update city set {col_name}='{col_value}' where id ={id}"  # execute this SQL command at db server

    print(str)
    cursor.execute(str)

    conn.commit()
    print('1 row is updated')

    cursor.close() 
    conn.close() 

x =int(input('enter no: '))
update_rows(x)


