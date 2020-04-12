pip install ffmpy3
#另外，必须已经安装了 ffmpeg，并且测试通过
# ffmpeg包，有3个命令文件，我放在 C:/Windows/system32 目录下，以便系统能找到。


>>> import ffmpy3
>>> ff = ffmpy3.FFmpeg(
...     inputs={'input.mp4': None},
...     outputs={'output.avi': None}
... )
>>> ff.run()

#运行成功，生成了 output.avi
#s使用 ffplay output.avi 可以正常播放
# OK!

#浏览了 ffmpy3 其它复杂用法。

# 视频推流
#http://www.ruanyifeng.com/blog/2020/01/ffmpeg.html


容器： 
container
ffmpeg -formats
学习了 上面的教程，ffmpeg 的使用，讲的非常好，转码方面的应用
但是没有讲 如何推流。。。

教案：
ffmpeg -f gdigrab -video_size 1024*768 -framerate 15 \
    -i desktop -pix_fmt guv420p -codec:v libx264 \
    -bf o -g 300 -f flv rtmp://ip:ports/myapp/{学号}
#估计是推流到服务器上去
#抓取本地 桌面，声音 摄像头等，编码到服务器上。
# ip: port, 4——7.9-821-5.2-21:1-935



