#!/usr/bin/env python
#-*- coding=utf-8 -*
#获取1301到1500中间的200个数字，并用","隔开
a=[index for index  in range(1301,1501)]
string= str(a)
#print string.replace("[","").replace("]","").replace(", ",",")

#将list中的str转换成int、float
data = ['1','3.2','2']
data = map(eval, data)
#print data


#将list中的int\float转换成str
array=[1,2,3.2,4,5]
new_array=map(str,array)
#print new_array

array1=[1,2,3,4,5]
new_array1=[str(x) for x in array1]
#print new_array1

#reduce
def multiply(a,b):
    return a*b
print reduce(multiply,(1,2,3,4))

#filter
# def is_odd(x):
#     return x%2==1
# print filter(is_odd,(1,2,3,4,5,6))
print filter((lambda x:x%2==1),(1,2,3,4,5,6))

print help(sorted)

#sorted
print sorted(["zara","asb","hm"],reverse=True)

#将嵌套列表排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
new_dict=dict(L)
# b=sorted(new_dict.items(),key=lambda x: x[0],reverse=False)
# c=sorted(new_dict.items(),key=lambda x: x[1],reverse=False)
# print b,c


#字典遍历
# for key in new_dict.keys():
#     print key
# for item in new_dict.items():
#     print item
for value in new_dict.values():
    print value
print sorted(new_dict.items(),key=lambda x:x[1])


