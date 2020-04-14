PyQt5（designer）入门教程
https://blog.csdn.net/azuremouse/article/details/90338961
这一篇文章 比较合适，入门pyqt

1, 安装 pip install PyQt5==5.13.0
2. 安装 pip install pyqt5-tools==5.13.0
3. 安装 pip install PyQtWebEngine=5.13.0

检查 desiger安装 ：
1. Win+S呼出Cornata主面板（搜索框），输入designer，可以启动 designer
2. 命令行 输入 designer, 可以启动成功
3. pyuic5 ，返回： “Error: one input ui-file must be specified” OK
4. pyuic5 --version
5. designer --version


1.  建立一个 qt_helloworld 项目
跟着做，运行
可以看到建立了一个窗口
OK

2. 练习2
继续做上个练习的教程，
   10）组件自适应
   11） Interaction
     按钮，在控制台可以输出 预设的信息。
    ok！

3. 练习3 
  GUI的汇率转换器
  1, 新建一个目录 Conversion, 下面的工作都在这里目录里面
  2. 建立一个新的符合要求的窗口 Conversion.ui
  3. 转换 pyuic5 -o Conversion.py Conversion.ui
  4. 新建立一个文件 main.py, 将 qt_helloworld目录下的 main.py内容拷贝进来
  5. 修改 main.py  关联 Conversion，调试运行没有错误
  6， 运行 main.py 可以启动汇率转换窗口，点 中间转换按钮，命令行输出练习2一样的信息。
  7. 现在已经 完成到 练习2 的情形，可以继续教程。

  8. 按照教程 继续改写 main.py
  9. 反复调试 main.py 终于成功！
  10. 注意： 
      setText，这里需要注意大小写，一点都不能差。估计是QT内部的函数需要大小写吧。
      测试下了， python关注大小写.
  11. 完毕！

4. 练习4
  多线程，不建议练习。这个难度比较大。先放着。







