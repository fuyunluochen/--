from pymysql import Connection

conn = Connection(
    host='localhost',  # 名称
    port=3306,  # 端口
    user='root',  # 用户
    password='123456',  # 密码
    autocommit=True  # 自动提交
)

cursor = conn.cursor()
conn.select_db('sys')
cursor.execute("insert into student value(10086,'向航','18')")
conn.commit()
conn.close()
