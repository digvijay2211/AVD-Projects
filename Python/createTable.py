import pymysql

# Establish connection between python and mysql
def connection():
    conn = pymysql.connect(host='localhost', database='avd', user='root', password='digvijay@2211')
    cursor = conn.cursor()

    return cursor, conn

# Take input from user
def userinput():
    print("What you want to do: ")
    options = {1:'create table', 2: "delete from table"} # dir 
    for i,j in options.items(): # taking key as i and j as value in item() not call then only key is getting
        print(i,j)

    i = int(input("Select option from above list: "))

    # calling opretion fuc to perform specific task
    return opretion(i)

#  logic for which opretion need to perform
def opretion(a):
    
    op = None   # assign empty variable

    # Create table
    if a == 1:
        op = createTable()

    # calling fuc to execute opretion
    curseorFuc(op)
    print("table created succesful")

    # closing connection
    close()


# create table fun
def createTable():
    
    tb = input('Enter table name: ')
    col = int(input(f"How many col you want in {tb}: "))

    # create list for coloun name and datatype
    columns = [(input(f"Enter column name {i+1}: "), input(f"Enter datatype for column {i+1}: ")) for i in range(col)]

    columns_sql = ", ".join([f"{col_name} {data_type}" for col_name, data_type in columns]) #lst = [int(i)  for i in range(1,10)]

    # creating syntax for table creation
    table = f"create table {tb}({columns_sql})"

    # return syntax for table creation
    return table


        

# logic of executution DML command         
def curseorFuc(a):
    cursor.execute(a)

# close connection
def close():
    cursor.close()
    conn.close()
    print("connection close")

# calling function for takeing input from user
cursor, conn = connection() 
userinput()


