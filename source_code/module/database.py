'''
Created on Jan 10, 2017

@author: hanif
'''

import pymysql
import os
import sshtunnel
from sshtunnel import SSHTunnelForwarder

mysqlhostip = os.getenv('MYSQL_HOST','localhost')
mysqluser = os.getenv('MYSQL_USER')
mysqlpassword = os.getenv('MYSQL_PWD')
privatekey = os.getenv('PK')

server = SSHTunnelForwarder(
    (mysqlhostip, 22),
    ssh_username=privatekey,
    KEY_PASSWORD='~/.ssh/id_rsa',
    remote_bind_address=('127.0.0.1', 3306)
)
server.start()

class Database:
    def connect(self):
        return pymysql.connect(host='127.0.0.1',user=mysqluser,password=mysqlpassword,db='crud_flask',port=3306)

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)", (data['name'],data['phone'],data['address'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
