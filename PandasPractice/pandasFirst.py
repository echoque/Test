#!/usr/bin/python
# -*- encoding:utf-8 -*-
import numpy as np, pandas as pd
# arr1 = np.arange(10)
# print arr1
# print type(arr1)
# s1 = pd.Series(arr1)
# print s1
# print type(s1)
#
# dic1 = {'a':10,'b':20,'c':30,'d':40,'e':50}
# print dic1
# print type(dic1)
# s2 = pd.Series(dic1)
# print s2
# print type(s2)


#DataFrame的创建
#数据框的创建主要有三种方式：
#通过二维数组创建数据框

# arr2 = np.array(np.arange(12)).reshape(4,3)
# print arr2
# print type(arr2)
# df1 = pd.DataFrame(arr2)
# print df1
# print type(df1)

#二数据索引index
#1、通过索引值或索引标签获取数据
# s4 = pd.Series(np.array([1,1,2,3,5,8]))
# print s4
# print pd.Series(np.array(['a','d','b','c']))

#三利用pandas分析数据
student = pd.io.parsers.read_csv('D:\\permission0726.txt')
#查询数据的前5行或末尾5行

print student.head()
print student.tail()