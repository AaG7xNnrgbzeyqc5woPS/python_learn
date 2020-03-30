class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d " % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

#-------------------------------
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
    
t = Test()
t.prt()

#------------------------------
'''
class Test1:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)

t = Test1
t.prt()
# 这个特性不支持，看来必须用self
# TypeError: prt() missing 1 required positional argument: 'runoob'
'''

#------------------------------------
# class Employee
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

emp1.age = 7 # add age attr
emp1.age = 8 # fixed age attr
#del emp1.age 
#print(empl)

print(hasattr(emp1, 'age'))
print(getattr(emp1, 'age'))
setattr(emp1, 'age', 9)
print(getattr(emp1,'age'))
delattr(emp1,'age')

print(emp1.__dict__)  #类的属性字典
print(emp1.__doc__)   #文档，注释
# print(emp1.__name__) # 未定义
print(emp1.__class__)  #类名
print(emp1.__module__) #某块名，主程序为 '__main__'
#print(emp1.__bases__) #父类，不持支


#----------------------
# 类的属性和方法的开放性
# 类的成员的可访问性，通过类名和方法名前面加 “_”和“__”，单划线和双划线来区分
# public公开： 名字前面不加下划线，本类，子类，以及类外的所有函数，代码都可以访问。
# protect保护: 单划线，本类，以及子类的成员函数可以访问
# private私有： 双划线, 只有本垒的成员函数可以访问


#特例：
#Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName
class Runoob:
    __site = "www.runoob.com"

runoob = Runoob()
print(runoob._Runoob__site)  #OK

