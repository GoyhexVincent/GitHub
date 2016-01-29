#!/usr/bin/env python
# -*- coding: utf-8 -*-

Index_lv3  = open("index_lv3.txt","r")


for line in Index_lv3:
    data_in = line
    data_out = data_in.encode('LATIN1').decode('UTF-8')
    print(data_out)

