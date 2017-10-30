# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json
file_object = open('d:\\city.txt')
try:
    all_the_text = file_object.read( )
finally:
    file_object.close( )
print "*******************"
print all_the_text
print type(all_the_text)
ob=json.loads(all_the_text)
ob=json.load()
print "*******************"
print type(ob)

 # file_object = open('d:\\city.txt')
        # try:
        #     all_the_text = file_object.read( )
        # finally:
        #     file_object.close( )
        # print all_the_text
        # ob=json.dumps(all_the_text)
        # print "*********************************************"
        # print ob
        #
        # lines=[line.decode('utf-8') for line in file_object.readlines()]
        # print lines
