from pymysql import Connection

# 获取到MYSQL数据库的链接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456'
)
# 不带查询的SQL语句
# cursor = conn.cursor()
# conn.select_db("sys")
# cursor.execute("CREATE TABLE test_pymysql(id int,"
#                "name varchar(10),"
#                "age int)")
# 查询性质的sql语句
cursor = conn.cursor()
conn.select_db("sys")
cursor.execute("select * from test_pymysql")
results: tuple = cursor.fetchall()
for r in results:
    print(r)
# 打印mysql数据库软件信息
# print(conn.get_server_info())
# 关闭数据库链接
conn.close()
