import pymysql
def connectDB():
    return pymysql.connect(
        host="localhost",
        user="root",
        port=3309,
        database='inventory_db',
        cursorclass=pymysql.cursors.DictCursor
    )

conn = connectDB()
if conn:
    print("Connect database successfully!")