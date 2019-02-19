import pymysql.cursors

oldconn = pymysql.connect(host='192.168.1.37', user='zlf', passwd='', db='a', use_unicode=True, charset="utf8",
                       cursorclass=pymysql.cursors.DictCursor)
oldcurs = oldconn.cursor()
sql = "select * from goods limit 1"
print(sql)
oldcurs.execute(sql)
oldres = oldcurs.fetchone()
print(oldres)

newconn = pymysql.connect(host='localhost', user='root', passwd='python', db='bookm')
newcurs=newconn.cursor()
sql="desc kind "
newcurs.execute(sql)
newres=newcurs.fetchone()
print(newres)