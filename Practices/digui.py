# coding:utf-8
# __author__ = 'zhongyaqi'
import random
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

number=raw_input("请输入一个正整数:")
print(fac(number))