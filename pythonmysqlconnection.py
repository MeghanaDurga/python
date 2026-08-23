import pymysql

con = pymysql.connect(
    user='root',
    password='chinni@123',
    host='localhost',
    database='mysql'
)
print(con)
