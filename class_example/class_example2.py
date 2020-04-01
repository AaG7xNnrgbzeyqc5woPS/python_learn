#https://www.liaoxuefeng.com/wiki/1016959663602400
#廖雪峰 中文，免费，零起点，完整示例，基于最新的Python 3版本。
# firefox打开有问题,左边的教程目录无法点开，需要用win10 自带的浏览器打开
#

# python对象销毁(垃圾回收)
# Python 使用了引用计数这一简单技术来跟踪和回收垃圾。

a = 40
print(a)

b = a
print(b)

c = [b]
print(c)

del a
b = 100
c[0] = -1
print(b,c,c[0])

#Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器

class Point:
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):  #不知道为什么析构函数未执行？？？
        print ("销毁！")
        class_name = self.__class__.__name__
        print( class_name, "销毁")

pt1 = Point
pt2 = pt1
pt3 = pt1
print( id(pt1), id(pt2), id(pt3))  #三个对象的id值是一样的，ok！
del pt1
del pt2
del pt3

##-----------------------
class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print( "调用父类构造函数")
 
   def parentMethod(self):
      print( '调用父类方法')
 
   def setAttr(self, attr):
      Parent.parentAttr = attr
 
   def getAttr(self):
      print ("父类属性 :", Parent.parentAttr)
 
class Child(Parent): # 定义子类
   def __init__(self):
      print ("调用子类构造方法")
 
   def childMethod(self):
      print ('调用子类方法')

 
c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值

###############

class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法



