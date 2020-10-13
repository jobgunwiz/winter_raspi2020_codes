import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='raspiDBK', charset='utf8')

cursor = db.cursor()

sql = """CREATE TABLE test_table(
        idx INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(256) NOT NULL,
        nick VARCHAR(256) NOT NULL
        );"""
       

cursor.execute(sql)

db.commit()

db.close()
