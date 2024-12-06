def delete_rows(cursor, conn):

    tbname = input("enter the table name: ")
    tbid = int(input("enter id no: "))
    str1 = f"delete from {tbname} where id = '{tbid}'"  # execute this SQL command at db server

    cursor.execute(str1)
    conn.commit()
    print('row is deleted')

    cursor.close()

#update rows
def update_rows(cursor, conn):
    tbname = input("enter the table name: ")
    id = int(input('enter no: '))
    col_name =input("enter column name: ")
    col_value = input("enter value: ")

    str2 = f"update {tbname} set {col_name} ='{col_value}' where id = '{id}'"  # execute this SQL command at db server
    cursor.execute(str2)
    conn.commit()
    print(' row is updated')

    cursor.close()


