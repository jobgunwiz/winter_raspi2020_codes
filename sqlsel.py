import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='raspiDBK', charset='utf8')

cursor = db.cursor() 

db.commit()

sql = """SELECT * FROM test_table"""
cursor.execute(sql)

result = cursor.fetchall()
for i in result:
    print(i)

db.close()
