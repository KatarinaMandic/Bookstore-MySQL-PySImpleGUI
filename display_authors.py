import mysql.connector as con

db = con.connect(
    host = 'localhost',
    port = 3306,
    user = 'pyadmin2',
    password = '1234',
    database = 'py_bookstore'
)