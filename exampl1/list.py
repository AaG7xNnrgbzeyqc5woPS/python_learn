test = ['a','','b','','c','','']
print(test)
test = [i for i in test if i != '' ]
print(test)

list_words = [ '你', '我', '他' ]
print(list_words)

s = 'abcdefg'
print(s[::-1]) #逆序输出
print(s[::2]) # 输出 'aceg'
#range(10)
#print(range(10)[::2]) #输出 2，4，6，8
print(s[6:2:-2]) #ge
print(s[::-2]) #geca

'''
列表解析 List Comprehensions
表达式：[expression for iter_val in iterable if cond_expr]

    [expression]：最后执行的结果
    [for iter_val in iterable]：这个可以是一个多层循环
    [if cond_expr]：两个for间是不能有判断语句的，判断语句只能在最后；顺序不定，默认是左到右。 

讨论下多个 for 循环的执行顺序。
'''
print( [(x,y)for x in [1,2] for y in [3,4]])
print( [(x,y)for x in [1,2] for y in [3,x]])

#print( [(x,y) for x in [1,y] for y in [3,4]] )  #不支持！NameError: name 'y' is not defined
