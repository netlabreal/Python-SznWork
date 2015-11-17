#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
from mysql.connector import Error
from dbfpy import dbf
from utildb import UtilDb


class Utilities(object):
    gl_conn = None

    def __init__(self, host, user, pas):
        # host of mySql
        self.host = host
        # user for mySql
        self.user = user
        # password for mySql
        self.password = pas
        uu = UtilDb(host, user, pas)
        self.gl_conn = uu.connect('for_szn')

    # --------Poisk ls po pku_id in szn_ls---------------------------------------#

    def vib_data(self, pku_id):
        # create connection
        # conn = self.connect('for_szn')
        # create cursor
        try:
            cursor = self.gl_conn.cursor()
            # query data from table szn_ls
            cursor.execute("Select ls from szn_ls WHERE pku= %s ", (pku_id,))
            # Resultat
            row = cursor.fetchone()
            if row is not None:
                return row[0]
            else:
                return ""
        except Error as er:
            print("Can not read table szn_ls! {}".format(er))
        finally:
            cursor.close()

    # --------Poisk ls in our_ls table---------------------------------------#
    def search_ls(self, ls):
        rez = None
        try:
            cursor = self.gl_conn.cursor()
            # query data from table szn_ls
            cursor.execute("Select id, nomer from our_ls WHERE nomer= %s ", (ls,))
            # Resultat
            row = cursor.fetchone()
            if row is not None:
                rez = row[0]
        except Error as er:
            print("Can not read table szn_ls! {}".format(er))
        finally:
            cursor.close()
            return rez

    # --------Poisk usl in table---------------------------------------#

    def search_usl(self, usl):
        rez = None
        try:
            cursor = self.gl_conn.cursor()
            # query data from table usl
            cursor.execute("Select id, name from uslugi WHERE name= %s ", (usl,))
            # Resultat
            row = cursor.fetchone()
            if row is not None:
                rez = row[0]
        except Error as er:
            print("Can not read table szn_ls! {}".format(er))
        finally:
            cursor.close()
            return rez

    # --------return all months---------------------------------------#
    def all_months(self):
        rez = None
        try:
            cursor = self.gl_conn.cursor()
            # query data from table months
            cursor.execute("Select * from months order by data")
            # Resultat
            rows = cursor.fetchall()
            rez = rows
        except Error as er:
            print("Can not read table szn_ls! {}".format(er))
        finally:
            cursor.close()
            return rez

    # --------Poisk month in table---------------------------------------#
    def search_month(self, dat):
        rez = None
        try:
            cursor = self.gl_conn.cursor()
            # query data from table months
            cursor.execute("Select id from months WHERE data= %s ", (dat,))
            # Resultat
            row = cursor.fetchone()
            if row is not None:
                rez = row[0]
        except Error as er:
            print("Can not read table szn_ls! {}".format(er))
        finally:
            cursor.close()
            return rez

    # --------Poisk usluga name in table---------------------------------------#
    def search_usluganame(self, uname):
        rez = None
        try:
            cursor = self.gl_conn.cursor()
            # query data from table months
            cursor.execute("Select usl_id from szn_uslugi WHERE name= %s ", (uname,))
            # Resultat
            row = cursor.fetchone()
            if row is not None:
                rez = row[0]
        except Error as er:
            print("Can not read table szn_ls! {}".format(er))
        finally:
            cursor.close()
            return rez

    # --------Poisk month in table---------------------------------------#
    def search_org(self, org):
        rez = None
        try:
            cursor = self.gl_conn.cursor()
            # query data from table months
            cursor.execute("Select id from organizations WHERE name= %s ", (org,))
            # Resultat
            row = cursor.fetchone()
            if row is not None:
                rez = row[0]
        except Error as er:
            print("Can not read table szn_ls! {}".format(er))
        finally:
            cursor.close()
            return rez

    # --------Poisk or insert ls in our_ls table---------------------------------------#

    def search_ins_ls(self, ls):
        rez = self.search_ls(ls)
        if rez is None:
            try:
                cursor = self.gl_conn.cursor()
                cursor.execute("Insert into our_ls(nomer) values(%s)", (ls,))
                self.gl_conn.commit()
                # query data from table szn_ls
                cursor.execute("Select id, nomer from our_ls WHERE nomer= %s ", (ls,))
                row = cursor.fetchone()
                rez = row[0]
            except Error as er:
                print("Can not read table szn_ls! {}".format(er))
            finally:
                cursor.close()
        return rez

    # --------Poisk or insert usl in table---------------------------------------#

    def search_ins_usl(self, usl):
        rez = self.search_usl(usl)
        if rez is None:
            try:
                cursor = self.gl_conn.cursor()
                cursor.execute("Insert into uslugi(name) values(%s)", (usl,))
                self.gl_conn.commit()
                # query data from table szn_ls
                cursor.execute("Select id, name from uslugi WHERE name= %s ", (usl,))
                row = cursor.fetchone()
                rez = row[0]
            except Error as er:
                print("Can not read table szn_ls! {}".format(er))
            finally:
                cursor.close()
        return rez

    # --------Poisk or insert month in months table---------------------------------------#

    def search_ins_month(self, dat):
        rez = self.search_month(dat)
        if rez is None:
            try:
                cursor = self.gl_conn.cursor()
                # insert data into table months
                cursor.execute("Insert into months(data) values(%s)", (dat,))
                self.gl_conn.commit()
                # query data from table months
                cursor.execute("Select id from months WHERE data= %s ", (dat,))
                row = cursor.fetchone()
                rez = row[0]
            except Error as er:
                print("Can not read table szn_ls! {}".format(er))
            finally:
                cursor.close()
        return rez

     # --------Poisk or insert org in organizations table---------------------------------------#

    def search_ins_org(self, org):
        rez = self.search_org(org)
        if rez is None:
            try:
                cursor = self.gl_conn.cursor()
                cursor.execute("Insert into organizations(name) values(%s)", (org,))
                self.gl_conn.commit()
                rez = self.search_org(org)
            except Error as er:
                print("Can not read table szn_ls! {}".format(er))
            finally:
                cursor.close()
        return rez

    # --------Poisk saldo in saldo table---------------------------------------#

    def search_saldo(self, ls, month, uslid):
        rez = None
        try:
            cursor = self.gl_conn.cursor()
            # query data from table months
            cursor.execute("Select * from oborots WHERE ls= %s and month=%s and usl=%s", (ls, month, uslid,))
            # Resultat
            row = cursor.fetchone()
            if row is not None:
                rez = row
        except Error as er:
            print("Can not read table szn_ls! {}".format(er))
        finally:
            cursor.close()
            return rez

    # --------Open dbf and write it in MySql---------------------------------------#

    def ins_data_mysql(self, path):
        try:
            cursor = self.gl_conn.cursor()
            # create connection
            rr = os.path.isfile(path)
            # open dbf with data
            dbf_f = dbf.Dbf(path)
            # Kol-vo zapisey dbf
            count = dbf_f.recordCount
            if count != 0:
                for record in dbf_f:
                    # pku from dbf
                    pku = record['pku']
                    # Address from dbf
                    adr = str(record['adr']).decode('cp866')
                    # ls from dbf
                    va = record['ls']
                    if va is not None:
                        # preobraz float k int
                        ls = int(va)
                        try:
                            # Vnesenie data in MySql
                            cursor.execute("INSERT INTO szn_ls (pku,ls,adr) VALUES (%s,%s,%s)", (pku, ls, adr))
                            self.gl_conn.commit()
                            print(unicode(ls) + " -> " + pku)
                        except Error as err:
                            print(format(err))
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            # self.gl_conn.close()

    # -----------------------------------------------#

    # --------Open dbf with oborots and write it in MySql---------------------------------------#

    def per_oborots_mysql(self, path):
        try:
            cursor = self.gl_conn.cursor()
            rr = os.path.isfile(path)
            # open dbf with data
            dbf_f = dbf.Dbf(path)
            # Kol-vo zapisey dbf
            count = dbf_f.recordCount
            if count != 0:
                for record in dbf_f:
                    # ls from dbf
                    ls = self.search_ins_ls(record['ls'])
                    # Usluga from dbf
                    usl = self.search_ins_usl(str(record['usluga']).decode('cp866'))
                    # month from dbf
                    mon = self.search_ins_month(record['month'])
                    # org from dbf
                    org = self.search_ins_org(str(record['org']).decode('cp866'))
                    # prop from dbf
                    prop = record['prop']
                    # plosh from dbf
                    plosh = record['plosh']
                    # tarif from dbf
                    tarif = record['tarif']
                    # vx from dbf
                    vx = record['vx']
                    # nach from dbf
                    nach = record['nach']
                    # vist from dbf
                    vist = record['vist']
                    # opl from dbf
                    opl = record['opl']
                    # isx from dbf
                    isx = record['isx']
                    try:
                        # Vnesenie data in MySql
                        cursor.execute("INSERT INTO oborots (ls,month,usl,plosh,prop,tarif,vx,nach,vist,opl,isx,org) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (ls, mon, usl,plosh,prop,tarif,vx,nach,vist,opl,isx,org,))
                        self.gl_conn.commit()
                        print(unicode(ls) + " -> INSERTED")
                    except Error as err:
                        print(format(err))
            dbf_f.close()
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    # -----------------------------------------------#

    # -------------Proxod files v papke path i zapolnenie dbf------------------------#
    def walk_naim_correct_dbf(self, papka):
        col = 0;
        # Tek papka
        cwd = os.getcwd()
        # Tek papka + path
        path_i = unicode(os.path.join(cwd, papka))
        # Perebor Tek Papka + path
        for name in os.listdir(path_i):
            # put k filu
            path = os.path.join(path_i, name)
            if os.path.isfile(path):
                try:
                    dbf_file = dbf.Dbf(path)
                    for rec in dbf_file:
                        col += 1
                        ls = self.search_ls(rec['LS'])
                        if ls is not None:
                            rmon = rec['DATEP']
                            month = self.search_month(rec['DATEP'])
                            if month is not None:
                                rs = self.search_saldo(ls, month, 1)
                                if rs is not None:
                                    rec['PL'] = rs[10]
                                    rec['KOLP'] = rs[11]
                                    rec['NORM'] = rs[10]
                                    rec['PRIZN'] = 1
                                    rec['TARIF'] = rs[4]
                                    rec['FAKTP'] = rs[6]
                                    rec['FAKTPER'] = rs[7]
                                    rec['MESD'] = self.kolmes(ls, rmon, 1)
                                    # Save data in dbf
                                    rec.store()
                                rrr = 1
                            else:
                                print("Not found month! Record %s"%col)
                        else:
                            print("Not found ls! Record %s"%col)
                except Exception as e:
                    print(e)
                finally:
                    dbf_file.close()

    # -------------Proxod files v papke path i zapolnenie dbf------------------------#
    def walk_data_correct_dbf(self, papka):
        col = 0;
        # Tek papka
        cwd = os.getcwd()
        # Tek papka + path
        path_i = unicode(os.path.join(cwd, papka))
        # Perebor Tek Papka + path
        for name in os.listdir(path_i):
            # put k filu
            path = os.path.join(path_i, name)
            if os.path.isfile(path):
                try:
                    dbf_file = dbf.Dbf(path)
                    for rec in dbf_file:
                        col += 1
                        ls = self.search_ls(rec['LS'])
                        if(rec['LS']=='503561'):
                            rrr = 1

                        if ls is not None:
                            rmon = rec['DATEP']
                            month = self.search_month(rec['DATEP'])
                            if month is not None:
                                usl = self.search_usluganame(str(rec['GKU']).decode('cp866'))
                                if usl is not None:
                                    rs = self.search_saldo(ls, month, usl)
                                    if rs is not None:
                                        rec['PL'] = rs[10]
                                        rec['KOLP'] = rs[11]
                                        #***********************************
                                        if(usl == 7 or usl == 8 or usl == 9):
                                            if(rs[4] != 0):
                                                rec['NORM'] = round(rs[6] / rs[4], 2)
                                        else:
                                            rec['NORM'] = rs[10]
                                        #***********************************
                                        rec['PRIZN'] = 1
                                        rec['TARIF'] = rs[4]
                                        rec['FAKTP'] = rs[6]
                                        rec['FAKTPER'] = rs[7]
                                        rec['MESD'] = self.kolmes(ls, rmon, usl)
                                        # Save data in dbf
                                        rec.store()
                                    else:
                                        rec['PRIZN'] = 1
                                        # Save data in dbf
                                        rec.store()
                                else:
                                    print("Not found usluga! Record %s"%col)
                            else:
                                print("Not found month! Record %s"%col)
                        else:
                            print("Not found ls! Record %s"%col)
                except Exception as e:
                    print(e)
                finally:
                    dbf_file.close()
                    print("File %s is edited!" % path)

    # -------------Proxod files v papke path i prostavit ls in dbf------------------------#

    def walk_files_edit_dbf(self, papka):
        # Tek papka
        cwd = os.getcwd()
        # Tek papka + path
        path_i = unicode(os.path.join(cwd, papka))
        # Perebor Tek Papka + path
        for name in os.listdir(path_i):
            # put k filu
            path = os.path.join(path_i, name)
            # proverka is file
            if os.path.isfile(path):
                # Prostavit LS is MySql
                self.edit_dbf(path)
    # -----------------------------------------------#

    # -------------Proxod files v papke path i create itog dbf from dbf files------------------------#

    def walk_files_cr_dbf(self):
        # Count of files
        n_f = 0
        # Tek papka
        cwd = os.getcwd()
        # Tek papka + path
        path_i = unicode(os.path.join(cwd, 'cppn'))
        # create itog.dbf
        # res_dbf = dbf.Dbf(unicode(os.path.join(path_i, 'itog.dbf')), new=True)
        # Perebor Tek Papka + path
        for name in os.listdir(path_i):
            # put k filu
            path = os.path.join(path_i, name)
            # proverka is file
            if os.path.isfile(path) and name != 'itog.dbf':
                if path[-3:].lower() == "dbf":
                    # Zapisat file v csv
                    self.write_dbf(path, n_f)
                    n_f += 1
    # -----------------------------------------------#

    # --------Open all dbf files in path and write it in one dbf---------------------------------------#

    def write_dbf(self, dbf_path, nom_f):
        # kol-vo rows in dbf
        col = 0
        try:
            # open dbf
            dbf_ff = dbf.Dbf(dbf_path)
            # fields dbf
            pole_f = dbf_ff.fieldDefs
            # if file is first
            if nom_f == 0:
                # If file first -> create itog.dbf
                res_dbf = dbf.Dbf(unicode(os.path.join(os.path.dirname(dbf_path), 'itog.dbf')), new=True)
                # perebor all fifields in dbf
                for k in pole_f:
                    # Add fields from dbf -> new dbf
                    res_dbf.addField(k)
                # Add field ORG
                res_dbf.addField(("ORG", "C", 150),)
                res_dbf.close()
            # open itog.dbf
            res_dbf = dbf.Dbf(unicode(os.path.join(os.path.dirname(dbf_path), 'itog.dbf')))
            # Perebor all records in dbf
            for rec in dbf_ff:
                # create new record
                n_rec = res_dbf.newRecord()
                # Perebor all name of fields
                for r in dbf_ff.fieldDefs:
                    n_rec[r.name] = rec[r.name]
                n_rec['ORG'] = unicode(dbf_path).encode('cp866')
                n_rec.store()
                col += 1
                print" \rObrabativaetsa: %s zapis file:" % str(col)+" "+dbf_path,
            res_dbf.close()
            dbf_ff.close()
            print("File %s was writed to itog.dbf!" % dbf_path)
        except Exception as e:
            print(str(e)+" "+unicode(dbf_path).encode('utf-8'))

    # -----------Izmenenie dbf------------------------------------#
    def edit_dbf(self, f):
        # Error open file
        par = 0
        # Kol-vo zapisey v dbf
        col = 0
        # Naideno v Mysql
        naideno = 0
        # Ne naideno v Mysql
        nenaideno = 0
        try:
            # Open dbf
            dbf_file = dbf.Dbf(f)
            for rec in dbf_file:
                col += 1
                # Poisk pku v mySql
                r = self.vib_data(rec['PKU'])
                if r != "":
                    rec['LS'] = r
                    # Save ls v dbf
                    rec.store()
                    naideno += 1
                else:
                    nenaideno += 1
                print"\rObrabativaetsa :%s" % col,
            par = 1
        except:
            print("ERROR!!! Cant open file %s" % f)
        finally:
            if par == 0:
                print("File %s ne obrabotan" % unicode(f))
            else:
                dbf_file.close()
                print("File %s obrabotan! Kol-vo zapisey: %s, naideno: %s, ne naideno: %s" % (unicode(f), col, naideno, nenaideno,))
# -----------------------------------------------#

    # -----------Kol-vo months dolga------------------------------------#

    def kolmes(self, ls, month, uslid):
        # kol-vo mes dolga
        col_mon = 0
        # id month in Mysql
        m_id = self.search_month(month)
        # all months in table
        allmon = self.all_months()
        # list of oborots if months <= month
        rez = [self.search_saldo(ls, mon[0], uslid) for mon in allmon if mon[1] <= month]
        # first month
        first = 0
        # list of dolga
        dolg = []
        # oplata for all months
        oplata = 0
        if rez is not None:
            for r in rez:
                if r is not None:
                    oplata += r[8]
                    if first != 0 and m_id != r[2]:
                        dolg.append(r[6])
                    else:
                        if m_id != r[2]:
                            dolg.append(round(r[5]+r[7], 2))
                        first = 1
        # if list is not empty
        if len(dolg) > 0:
            for k in dolg:
                oplata = round(oplata - k, 2)
                if oplata < 0:
                    col_mon += 1
        return col_mon
