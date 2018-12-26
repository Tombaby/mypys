#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mac_all_venders():
    '''

    :return:
    '''
    vendors = []
    fp = open('/Users/shayne/Downloads/oui.txt', 'r')
    idx = 0
    for ln in fp.readlines():
        idx += 1
        if '(hex)' in ln:
            ln = ln.replace('-', '')
            vendors.append(int(ln[0:6], 16))
            print idx, ln[0:6], int(ln[0:6], 16)

    a = reduce(lambda x, y : x + y, vendors) / len(vendors)
    print a

    vmax = vendors[0]
    print vmax

    for v in vendors:

        vmax = vmax if vmax - v < 0 else v

    print vmax




if __name__ == '__main__':
    mac_all_venders()
