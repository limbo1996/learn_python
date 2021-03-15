import pymysql

conn = pymysql.connect(user = 'root', password = 'wx19960323', database = 'test')


cursor = conn.cursor()

sql = "SELECT * FROM students;"
cursor.execute(sql)

results = cursor.fetchall()
print(results)
results[0]
for row in results:
    print(row)

