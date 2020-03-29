dict = {'a':1, 'b':2, 'b':3, 'a':9}
print(dict['b'])
print(dict)

print(dict['a'])
print(dict)

pass

def printme( str ):
    "打印任何传入的字符串"
    print(str)
    return

printme("我的第一个自定义函数")

a=[1,2,3,4]
a="Runoob"

#python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

def printinfo(arg1, *vartuble):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    for var in vartuble:
        print(var)
    return

printinfo(10)
printinfo(20,30,50,9)

#lambda
#lambda
#lambda
sum = lambda arg1, arg2: arg1 + arg2
print("和：", sum(10,20))
print("和：", sum(50, 20))

def sum(arg1, arg2):
    total = arg1 + arg2
    print("函数内：",total)
    return total

sum(10,5)


def printMax(x,y):
    '''打印两个数中的最大值
    
    两个值必须都是整型数。'''

    x=int(x)
    y=int(y)
    if x > y:
        print(x, '最大')
    else:
        print(y, '最大')

printMax(3,5)
print ( printMax.__doc__)

#---------------------
#函数的方法名也可以作为另一个函数的参数。
def add(x,y):
    return x+y

def mult(x,y):
    return x*y

def add_twice(func,x,y):
    return func(func(x,y), func(x,y))  ##add twice, add(add(x,y), add(x,y))

a=5
b=10
print(add_twice(add, 5,10)) #15+15=30
print(add_twice(mult, a,b)) #50*50=2500
print()

#-----------------------------
print(id(25))  
a = 25  
print(id(a))  
b = 25  
print(id(b))  
print(a is b) 





