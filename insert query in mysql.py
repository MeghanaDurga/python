import pymysql
con=pymysql.connect(user='root',password='chinni@123',host='localhost',database='mysql')
cur= con.cursor()
cur.execute('''insert into employee1(empno,empname,sal,job,deptno)values(%s,%s,%s,%s,%s)''',
            [9,'MEGHANA',189000,'MANAGER',2])
con.commit()
cur.close()
con.close()
