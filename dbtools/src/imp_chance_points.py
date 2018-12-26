#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import mysql.connector
from mysql.connector import errorcode

def imp_chance_points() :

    try:
        cnx = mysql.connector.connect(user='emuclient', password='ws2kdOxgJpr6OYaj', host='10.9.154.46', database='emucoo-fnt')
        cursor = cnx.cursor()

        fp = open('chcp.csv', 'r')
        for ln in fp.readlines():
            nm = ln.strip()
            sql0 = "select count(1) from t_opportunity where is_del = 0 and name='%s' " % nm
            cursor.execute(sql0)
            rs1 = cursor.fetchone()
            cnt, = rs1
            if cnt > 0:
                print 'has the chance [%s] in database' % nm
                continue
            sql1 = """
                insert into t_opportunity (type, name, create_type, is_del, is_use, description, front_can_create, modify_time, create_time, create_user_id, modify_user_id, org_id)
                values (%d, '%s', %d, %d, %d, '%s', %d, '%s', '%s', %d, %d, %d)
            """ % (0, nm, 1, 0, 1, nm, 0, '2018-08-22 16:00:00', '2018-08-22 16:00:00', 1, 1, 1)

            print sql1
            cursor.execute(sql1)

        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    except:
        print sys.exc_traceback
    finally:
        cursor.close()
        cnx.close()


if __name__ == '__main__':
    imp_chance_points()



