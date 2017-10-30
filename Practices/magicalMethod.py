# coding:utf-8
# __author__ = 'zhongyaqi'
#构造和析构
class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getPeri(self):
        return (self.x+self.y)*2
    def gerArea(self):
        return self.x*self.y

rect=Rectangle(3,4)
print rect.gerArea()
print rect.getPeri()