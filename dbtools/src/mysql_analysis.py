#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode


def data_handle():
    '''

    :return:
    '''

    try:
        # cnx = mysql.connector.connect(user='emotwo', password='emu2018two', host='192.168.16.173', database='emucoo-cfb')
        cnx = mysql.connector.connect(user='emotwo', password='emu2018two', host='192.168.16.189', database='625')
        cursor = cnx.cursor()
        cursor.execute(
            "SELECT a.id, a.task_item_id, a.loop_work_id, b.task_id, b.type FROM t_operate_data_for_work a LEFT JOIN t_loop_work b ON a.loop_work_id = b.id")
        opt_data_arr = []
        for optdata in cursor:
            opt_data_arr.append(optdata)

        cursor.execute(
            "SELECT id, task_id,name, feedback_text_name, feedback_text_description, feedback_num_name, feedback_num_type, feedback_img_name, feedback_img_max_count,feedback_img_from_album, feedback_img_example_id, preinstall_score, preinstall_weight, feedback_need_text, feedback_img_type, feedback_need_num FROM t_operate_option")
        opt_item_arr = []
        for opt in cursor:
            opt_item_arr.append(opt)

        sql_template = """
            update t_operate_data_for_work set name = '%s', num_option_name ='%s', num_option_type = %d, img_option_name = '%s', num_need = %d, img_need = %d, img_option_max_count = %d, 
            img_option_from_album = %d, img_example_id = %d, txt_need = %d, txt_option_name = '%s', txt_option_description = '%s', pre_score = %s, pre_weight = %s 
            where id = %d 
        """
        for opt_data_id, task_item_id, loop_work_id, task_id, work_type in opt_data_arr:
            for opt_id, t_id, opt_nm, opt_txt_nm, opt_txt_dcp, opt_num_nm, opt_num_tp, opt_img_nm, opt_img_cnt, opt_img_alb, opt_img_xmp, opt_scr, opt_wgt, opt_nd_txt, opt_img_tp, opt_nd_num in opt_item_arr:
                opt_nm = opt_nm if opt_nm else ''
                opt_txt_nm = opt_txt_nm if opt_txt_nm else ''
                opt_txt_dcp = opt_txt_dcp if opt_txt_dcp else ''
                opt_num_nm = opt_num_nm if opt_num_nm else ''
                opt_num_tp = opt_num_tp if opt_num_tp else 0
                opt_img_nm = opt_img_nm if opt_img_nm else ''
                opt_img_cnt = opt_img_cnt if opt_img_cnt else 0
                opt_img_alb = opt_img_alb if opt_img_alb else 0
                opt_img_xmp = opt_img_xmp if opt_img_xmp else 0
                opt_scr = opt_scr if opt_scr else '0'
                opt_wgt = opt_wgt if opt_wgt else '0'
                opt_nd_txt = opt_nd_txt if opt_nd_txt else 0
                opt_img_tp = opt_img_tp if opt_img_tp else 0
                opt_nd_num = opt_nd_num if opt_nd_num else 0

                # print opt_id, t_id, opt_nm, opt_txt_nm, opt_txt_dcp, opt_num_nm, opt_num_tp, opt_img_nm, opt_img_cnt, opt_img_alb, opt_img_xmp, opt_scr, opt_wgt, opt_nd_txt, opt_img_tp, opt_nd_num
                if work_type == 1:
                    if t_id == task_id and task_item_id == opt_id:
                        k1 = opt_img_tp if opt_img_tp == 0 else 1
                        opt_img_cnt = 4 if opt_img_cnt == 0 and k1 == 1 else opt_img_cnt
                        sql1 = sql_template % (
                            opt_nm, opt_txt_nm, opt_num_tp, opt_img_nm, opt_nd_num, k1, opt_img_cnt, opt_img_alb,
                            opt_img_xmp, opt_nd_txt, opt_txt_nm, opt_txt_dcp, opt_scr, opt_wgt, opt_data_id)
                        print sql1
                        cursor.execute(sql1)
                        break
                else:
                    if t_id == task_id:
                        k2 = 0 if opt_img_tp == 1 else 1
                        k3 = 1 if opt_img_tp == 3 else 0
                        opt_img_cnt = 4 if opt_img_cnt == 0 and k2 == 1 else opt_img_cnt
                        sql2 = sql_template % (
                            opt_nm, opt_txt_nm, opt_num_tp, opt_img_nm, opt_nd_num, k2, opt_img_cnt, k3, opt_img_xmp,
                            opt_nd_txt, opt_txt_nm, opt_txt_dcp, opt_scr, opt_wgt, opt_data_id)
                        print sql2
                        cursor.execute(sql2)
                        break

        cnx.commit()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        cursor.close()
    cnx.close()



if __name__ == '__main__':
    data_handle()
