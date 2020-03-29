tup1 = ()
print(tup1)

tup1 = (50,)
print(tup1)
#del tup1
print(tup1)  # NameError: name 'tup1' is not defined

#tup1 = ()
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
 
print( "tup1[0]: ", tup1[0])
print( "tup2[1:5]: ", tup2[1:5])

print(len(tup1))
print(len(tup2))

for x in tup1 : print(x, end=", ")
print()
for i in tup2 : 
    print(i, end=" ")
print()

#任意无符号的对象，以逗号隔开，默认为元组，如下实例：
print ('abc', -4.24e93, 18+6.6j, 'xyz')

x, y = 1, 2
print(x, y)


tuple = (("all")) #小括号运算
print(tuple)   # 输出字符串 all

s = "abcdefg"
print(s)

tup=("all", )  #所以，如果元组只有1个元素，就必须加一个逗号，防止被当作括号运算：
print(tup)
    

