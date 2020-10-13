import pymysql
import Adafruit_DHT

DHT_PIN = 26
DHT_TYPE = Adafruit_DHT.DHT11

db = pymysql.connect(host='localhost',
        port=3306,
        user='root',
        password='1234',
        db='raspiDBK',
        charset='utf8')

hum, temp = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)
if hum is not None and temp is not None:
    print('Temp = (0:0.1f)*C Humidity =(1:0.1f)%'.format(temp,hum))
    with db.cursor() as cur:
            sql = """insert into sensor(time, hum, temp, illum)
                    values (now(), %s, %s, 0)"""
            print(sql)
            cur.execute(sql, (hum,temp))
            db.commit()

    with db.cursor() as cur:
        sql="select * from sensor"
        cur.execute(sql)
        rows = cur.fetchall()
        for row_data in rows:
            print(row_data)

else:
    print("nope")
