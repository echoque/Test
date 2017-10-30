# coding:utf-8
# __author__ = 'zhongyaqi'
import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

try:
    f=open(r"c:\ss.txt","w")
    print (f.write("我存在啦"))
    a=1+'1'
    f.close()
except OSError as reason:
    print("文件出错了"+str(reason))
except TypeError as reason:
    print("类型出错了"+str(reason))
finally:
    print(f.write("啦啦啦啦"))
