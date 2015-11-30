#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from utilities import Utilities
from utildb import UtilDb
from datetime import date
import os

u = Utilities('192.168.1.100', 'alexandr', 'rfqkfc')

# initialisation of DB and tables
def init_databse(self):
    uu = UtilDb('192.168.1.100', 'alexandr', 'rfqkfc')
    uu.init_db()
    uu.init_tables()


# insert ls from dbf in Mysql
def insert_ls(f_name):
    cwd = os.getcwd()
    p = unicode(os.path.join(cwd, f_name))
    u.ins_data_mysql(p)


# insert ls from Mysql in dbf using pku
def vnesti_ls_dbf(papk):
    u.walk_files_edit_dbf(papk)


# insert oborots in Mysql from dbf
def insert_oborots(f_name):
    # u.per_oborots_mysql("E:/Django_projects/SZN/n082015.dbf")
    u.per_oborots_mysql(f_name)


# insert oborots from Mysql in dbf
def insert_oborots_dbf(papka):
    u.walk_data_correct_dbf_ams5(papka)
    #u.walk_data_correct_dbf_new(papka)
    # u.walk_naim_correct_dbf(papka)

#u.per_oborots_mysql_ams("E:/Django_projects/SZN/zagr/AMS5/10.dbf")
#insert_oborots("E:/Django_projects/SZN/zagr/AMS5/07.dbf")
#vnesti_ls_dbf('musor/dop')
insert_oborots_dbf('sod/ams5')
#u.walk_files_cr_dbf()
#insert_ls("E:/Django_projects/SZN/dopls.dbf");

#ls = u.search_ls(505095)
#rr = u.search_saldo(ls, 3, 3)
#print(ls)
#print(u.kolmes(ls, date(2015, 10, 01), 10))
#print u.search_saldo_ams5(ls,4,10)
# print(u.kolmes(3880, date(2015, 8, 01), 1))
u.gl_conn.close()

