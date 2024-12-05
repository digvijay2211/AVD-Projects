def delete_rows(cursor, conn):

    id = int(input('enter no: '))
    str = "delete from pra where id ='%d'"  # execute this SQL command at db server
    args = id

    cursor.execute(str %args)

    conn.commit()

    cursor.close()
    print('1 row is deleted')

#update rows
def update_rows(cursor, conn):
    id = int(input('enter no: '))
    col_name =input("enter column name: ")
    col_value = input("enter value: ")

    str = f"update pra set {col_name}='{col_value}' where id ={id}"  # execute this SQL command at db server

    print(str)
    cursor.execute(str)
    conn.commit()
    print('1 row is updated')



