from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456'
)

cursor = conn.cursor()
conn.select_db('test')
# 非查询性sql
# cursor.execute('create table test_pymysql(id int,info varchar(255))')
# 查询性sql
cursor.execute('select * from student')
results = cursor.fetchall()
for r in results:
    print(r)
conn.close()
