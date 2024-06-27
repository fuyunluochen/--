from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)

cursor = conn.cursor()
conn.select_db('test')
cursor.execute("insert into student value(10086,'向航','18')")
conn.commit()
conn.close()
