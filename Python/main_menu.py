from sqlconnection import connection
from delete_update import  delete_rows, update_rows
from insert_table import insert_opration
from create_table import create_table

cursor, conn = connection()
# Take input from user
def userinput():
    print("What you want to do: ")
    options = {1:'create table', 2: "delete from table", 3: "update table", 4:"insert into table"} # dir
    for i,j in options.items(): # taking key as i and j as value in item() not call then only key is getting
        print(i,j)

    i = int(input("Select option from above list: "))
    # calling opretion fuc to perform specific task
    return opretion(i)

#  logic for which opretion need to perform
def opretion(a):

    if a == 1:
        create_table(cursor)
        print("table created succesful")
    elif a == 2:
        delete_rows(cursor, conn)
    elif a == 3:
        update_rows(cursor, conn)
    if a== 4:
        insert_opration(cursor, conn)
    # closing connection
    cursor.close()
    conn.close()

# calling function for takeing input from user
userinput()



