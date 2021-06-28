import os
import pymysql.connections

MY_SQL_HOST = 'localhost'
MY_SQL_PORT = 8306
MY_SQL_USER = 'root'
MY_SQL_PASSWORD = '123456'
MY_SQL_DATABASE = 'buckets'

conn = pymysql.connect(
    host=MY_SQL_HOST,
    user=MY_SQL_USER,
    password=MY_SQL_PASSWORD,
    port=MY_SQL_PORT,
    db=MY_SQL_DATABASE,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
