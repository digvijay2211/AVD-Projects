from sqlconnection import connection
from delete_update import  delete_rows, update_rows

cursor, conn = connection()
# Take input from user
def userinput():
    print("What you want to do: ")
    options = {1:'create table', 2: "delete from table", 3: "update table"} # dir
    for i,j in options.items(): # taking key as i and j as value in item() not call then only key is getting
        print(i,j)

    i = int(input("Select option from above list: "))

    print(i)
    # calling opretion fuc to perform specific task
    return opretion(i)

#  logic for which opretion need to perform
def opretion(a):

    if a == 1:
        create_table()
        print("table created succesful")
    elif a == 2:
        delete_rows()
    elif a == 3:
        update_rows()

    # closing connection
    close()


# create table fun
def create_table():
    
    tb = input('Enter table name: ')
    col = int(input(f"How many col you want in {tb}: "))

    # create list for coloun name and datatype
    columns = [(input(f"Enter column name {i+1}: "), input(f"Enter datatype for column {i+1}: ")) for i in range(col)]

    columns_sql = ", ".join([f"{col_name} {data_type}" for col_name, data_type in columns]) #lst = [int(i)  for i in range(1,10)]

    # creating syntax for table creation
    table = f"create table {tb}({columns_sql})"

    # return syntax for table creation
    cursor.execute(table)

# close connection
def close():
    cursor.close()
    conn.close()
    print("connection close")

# calling function for takeing input from user

userinput()



