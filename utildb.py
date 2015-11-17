import mysql.connector
from mysql.connector import Error


class UtilDb(object):
    def __init__(self, host, user, pas):
        # host of mySql
        self.host = host
        # user for mySql
        self.user = user
        # password for mySql
        self.password = pas

    # --------------Connect to DB---------------------------------#
    def connect(self, db=None):
        try:
            # create connection
            if db is None:
                conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
            else:
                conn = mysql.connector.connect(host=self.host, database=db, user=self.user, password=self.password)
            return conn
        except Error as e:
            print("Can not connect to mySql! {}".format(e))
            exit(1)
        except:
            print('ERROR! Mysql server is not working')
            exit(1)

    # --------Create DB szn in MySql--------------------------------------#
    def init_db(self):
        # create connection
        conn = self.connect()
        # create cursor
        cursor = conn.cursor()
        try:
            # create db
            cursor.execute("CREATE DATABASE for_szn DEFAULT CHARACTER SET 'utf8' ")
            print("DB for_szn created!")
        except Error as err:
            print("Can not create DB szn! {}".format(err))
            # exit(1)
        finally:
            cursor.close()
            conn.close()

    # --------Del DB szn in MySql--------------------------------------#
    def del_db(self):
        # create connection
        conn = self.connect()
        # create cursor
        cursor = conn.cursor()
        try:
            # create db
            cursor.execute("DROP DATABASE for_szn")
            print("DB szn deleted!")
        except Error as err:
            print("Can not delete DB szn! {}".format(err))
            exit(1)
        finally:
            cursor.close()
            conn.close()

    # --------Create table szn_ls in MySql--------------------------------------#
    def init_tables(self):
        # create connection
        conn = self.connect('for_szn')
        # create cursor
        cursor = conn.cursor()
        try:
            # create table szn_ls
            cursor.execute(
                "CREATE TABLE szn_ls (id int(11) NOT NULL AUTO_INCREMENT,pku varchar(12) NOT NULL, adr varchar(150), ls int(11) NOT NULL,PRIMARY KEY (id),key (pku))")
            print("Table created!")
        except Error as er:
            print("Can not create table szn_ls! {}".format(er))
            # exit(1)
        finally:
            cursor.close()
            conn.close()

    # --------Del table szn_ls in MySql--------------------------------------#

    def del_tables(self):
        # create connection
        conn = self.connect('for_szn')
        # create cursor
        cursor = conn.cursor()
        try:
            # delete table szn_ls
            cursor.execute("DROP TABLE szn_ls")
            print("Table deleted!")
        except Error as er:
            print("Can not delete table szn_ls! {}".format(er))
            exit(1)
        finally:
            cursor.close()
            conn.close()
