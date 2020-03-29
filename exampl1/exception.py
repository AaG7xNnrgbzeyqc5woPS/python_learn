'''
BaseException
SystemExit
KeyboardInterrupt
Exception
Exception
StopIteration
StopIteration  #iteration

'''

try:
    fh = open("testfile","w")
    fh.write("这是一个测试文件，用户测试异常")
except IOError:
    print("Error: 没有找到文件或者读取文件失败！")
else:
    print("内容写入文件成功")
    fh.close()

#----------------------
try:
    fh = open("testfile","w")
    fh.write("这是一个测试文件，用户测试异常")
finally:
    print("Error: 没有找到文件或者读取文件失败")
    
