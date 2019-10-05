# _*_ coding: utf-8 _*_
import pymysql

db = pymysql.connect("localhost","root","31243124","test")
cursor = db.cursor()

class dbexec(object):
    def __init__(self):
        self.FIRST_NAME='MACC'
        self.LAST_NAME='chen'
        self.AGE=10
        self.SEX='M'
        self.INCOME=100
    def adddata(self,FIRST_NAME,LAST_NAME,AGE,SEX,INCOME):
        print(self.AGE)
        sql_2 = "INSERT INTO learnsql_1(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES(\'%s\',\'%s\',%d,\'%s\',%d)" %(FIRST_NAME,LAST_NAME,
                                                                                                                      AGE,SEX,INCOME)
        #sql_2 = "INSERT INTO learnsql_1(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ('%s' %self.FIRST_NAME+, '陈', 20, 'M', 2000)"
        cursor.execute(sql_2)
        db.commit()

    def deletedata(self,FIRST_NAME):
        sql = "delete from learnsql_1 where FIRST_NAME='%s'" % (FIRST_NAME)
        print(sql)
        cursor.execute(sql)
        db.commit()


# 使用 execute() 方法执行 SQL，如果表存在则删除
#cursor.execute("DROP TABLE IF EXISTS learnsql_1")

try:
    db0728 = dbexec()
    db0728.adddata('ccx', '陈', 20, 'M', 2000)
    db0728.deletedata('cc')
except:
    db.rollback()

db.close()
