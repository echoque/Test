# coding:utf-8
import sys
import requests
#sys.setdefaultencoding('utf-8')

def test():
   r=requests.get('http://app.58.com/api/log/api/info/citynew/1',allow_redirects=False)
   print r.status_code
   print r.history
   index= r.content

   savedata(index)



def savedata(index):
  with open('C:\\Users\\zhongyaqi\\Desktop\\testSX12.txt',"ab")  as f:
      f.write(index)
      print '本次写入成功'






if __name__ == '__main__':
    test()
    #savedata()

# num = 5
# if num == 3:            # 判断num的值
#     print 'boss'
# elif num == 2:
#     print 'user'
# elif num == 1:
#     print 'worker'
# elif num < 0:           # 值小于零时输出
#     print 'error'
# else:
#     print 'roadman'     # 条件均不成立时输出