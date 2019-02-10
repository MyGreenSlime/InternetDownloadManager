import mysql.connector
import sys
class DatabaseManage():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database = 'downloadmanager'
        )
    def insertNew(self,filename, url, kind, typefile, state):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO downloaded (filename,url,kind,typefile,state) VALUES (%s, %s, %s, %s, %s)"
        val = (filename, url, kind, typefile, state)
        mycursor.execute(sql, val)
        self.mydb.commit()
        sys.exit




