# _*_ coding: utf-8 _*_
import pymysql

db = pymysql.connect("localhost","root","31243124","test")
cursor = db.cursor()

class dbexec(object):
    def __init__(self,FIRST_NAME,LAST_NAME, AGE, SEX, INCOME):
        self.FIRST_NAME=FIRST_NAME
        self.LAST_NAME=LAST_NAME
        self.AGE=AGE
        self.SEX=SEX
        self.INCOME=INCOME
    def adddata(self):
        print(self.AGE)
        sql_2 = "INSERT INTO learnsql_1(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES(\'%s\',\'%s\',%d,\'%s\',%d)" %(self.FIRST_NAME,self.LAST_NAME,
                                                                                                                      self.AGE,self.SEX,self.INCOME)
        #sql_2 = "INSERT INTO learnsql_1(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ('%s' %self.FIRST_NAME+, '陈', 20, 'M', 2000)"
        cursor.execute(sql_2)
        db.commit()
db0728=dbexec('Maca', '陈', 20, 'M', 2000)
db0729=dbexec('Macx', '陈', 20, 'M', 2000)


# 使用 execute() 方法执行 SQL，如果表存在则删除
#cursor.execute("DROP TABLE IF EXISTS learnsql_1")

try:
    #cursor.execute(sql)
    db0728.adddata()
    db0729.adddata()
except:
    db.rollback()

db.close()
