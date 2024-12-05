import pymysql
from credentials import *

# Establish connection between python and mysql
def connection():
    conn = pymysql.connect(host=host, database=database, user=user, password=password)
    cursor = conn.cursor()

    return cursor, conn