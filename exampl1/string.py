
#string
s = 'abcdef'
s1 = s[1:5]
print(s1)

s2 = s[2:5]
print(s2)

s3 = s[-3: -1]
print(s3)

s4 =s[-4:-1]
print(s4)

s5 = s[-4:]
print(s5)

s6 = s[0:]
print(s6)

s7 = s[:5]
print(s7)

s8 = s[:]
print(s8)

print(s*2)
print(s+"test"+"你好！")
#print("\n")
#print(" ")
print('')

#list
#           0    1   2    3   4   5   6
letters = ['c','h', 'e', 'c','k','i','o']
print(letters)
print(letters[1:4:2]) #hc
print(letters[1:6:2])   #hci
print(letters[1:5:2])   #hc

list = ['runoob', 786, 2.34, 'john', 70.2]
tinylist = [123, 'john']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print (tinylist * 2)
print(list + tinylist)

print("")

#---------------------
# tuple
# tuple = readonly list
tuple = ( 'runoob', 86, 2.33, 'john', 70.2)
'test,note, comment' #
tinytuple = (123, 'john')

print(tuple)
print(tuple[0])
print(tuple + tinytuple)
#print(tuple + tinylist) # error

#---------------------
# dictionary

print('')
print('----------------------dictionary-----------------------')
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = { 'name': 'john', 'code':6373, 'dept': 'sales'}

print (dict['one'])
print(dict[2])
print('')

print(tinydict)
print(tinydict.keys())
print(tinydict.values())
print("")





