# create table fun
def create_table(cursor):

    tb = input('Enter table name: ')
    col = int(input(f"How many col you want in {tb}: "))

    # create list for coloun name and datatype
    columns = [(input(f"Enter column name {i + 1}: "), input(f"Enter datatype for column {i + 1}: ")) for i in
               range(col)]

    columns_sql = ", ".join(
        [f"{col_name} {data_type}" for col_name, data_type in columns])  # lst = [int(i)  for i in range(1,10)]

    # creating syntax for table creation
    table = f"create table {tb}({columns_sql})"

    # return syntax for table creation
    cursor.execute(table)
