import MySQLdb

host = "mysql_db"
db_name = "employees"
user = "user"
password = "password"

conn = MySQLdb.connect(
    host=host, db=db_name, user=user, password=password, charset="utf8"
)
cur = conn.cursor()
cur.execute("select * from test_user")
print(cur.fetchall())
