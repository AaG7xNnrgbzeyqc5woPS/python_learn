播放工具
1. vlc 安装完成，下载一个视频，播放OK
2. ffplay 
   a. ffplay的介绍： 《FFmpeg命令行工具ffplay》
    https://www.jianshu.com/p/8cce27b1e294

   b. 《ffplay工具命令使用技巧浅析》
    https://blog.csdn.net/dosthing/article/details/80140645

3. 《FFmpeg详解》
https://blog.csdn.net/dosthing/article/details/79905552
安装：
a) 下载 ffmpeg源码：
 http://ffmpeg.org/download.html
 找到windows编译二进制： https://ffmpeg.zeranoe.com/builds/
 下载后，把二进制文件拷贝到 C:\Windows\System32
  这个就可以在命令行直接运行了
  有三个二进制文件：ffprobe, ffplay, ffmpeg 
  在 Git Bash下命令行下运行
  cd ~
  cd /Videos
  ls *.mp4
   video1.mp4  video2.mp4
  有两个例子视频文件
   $ ffprobe video1.mp4
   ffprobe version git-2020-04-03-52523b6 Copyright (c) 2007-2020 the FFmpeg developers
  built with gcc 9.3.1 (GCC) 20200328
  .....
 
 4 ） 播放本地视频：
  ffplay -vf scale=720:480  video1.mp4
效果OK
  四个方向键控制 快进快退
  播放音频时，一些操作：
w:绘制音频波形图
right:快进10s
left:快退10s
up:快进1min
down:快退1min
space:暂停/开始
esc:退出
播放视频时，一些操作：
s:步进模式，每按一次s，就播放下一帧图像 #这个好用。
每个都试试，不错！

 5.  播放 rtsp 流
 比如播放一个rtsp网络流（PS rtsp流可以用vlc推流 https://blog.csdn.net/gengxt2003/article/details/52811931）
 ffplay -vf scale=480:320 rtsp://192.168.1.19:8554/stream
 测试失败，语法正确，但是没有反应。

6. ffmpeg试一下转码之类的操作
 ffmpeg将视频码率设置为640kpbs
ffmpeg -i video1.mp4 -b:v 640k outsample.avi
转换成功，
看看能不能播放
ffplay -vf scale=720:480  outsample.avi
播放OK！

7. ffprobe则是用来发现资源的，比如发现可用的设备，如摄像头、录音设备等。
ffprobe -devices

8.  ffplay工具命令使用技巧浅析
 https://blog.csdn.net/dosthing/article/details/80140645

  ffplay的基本用法很简单，其一般形式如下：

    ffplay [option] file
    ffplay [option] URL

    总结起来ffplay的用法就是option项加上资源路径，option项是用来指定播放时的一些参数的，
    如指定连接的协议、视频画面的大小，音视频解码器选用、传输码率设定等，一般这些参数我们很少会设置，使用默认就OK，
    此时option项可以直接忽略，ffplay会帮我们选择，这也是它功能强大的体现，
    option的更多具体选项可以参考其官方文档；资源路径则包括文件资源路径和网络资源路径，
    文件资源路径是指定需要播放的音视频文件，如*.mp3、*.mp4、*,avi、*.mkv、*.rmvb等等类型的文件，
    网络资源路径根据协议可以分为RTSP、RTMP、HTTP流资源，心情好，来个直播，如：

    ffplay rtmp://live.hkstv.hk.lxdns.com/live/hks  #不能用
    ffplay http://live.hkstv.hk.lxdns.com/live/hks/playlist.m3u8 #不能用

     CCTV1高清：http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8

     
     #下面是一些热心网友提供的测试连接，感谢他们的分享，如有侵权，请联系删除。

RTMP协议直播源

大熊兔（点播）：rtsp://184.72.239.149/vod/mp4://BigBuckBunny_175k.mov

香港卫视：rtmp://live.hkstv.hk.lxdns.com/live/hks

RTSP协议直播源

珠海过澳门大厅摄像头监控：rtsp://218.204.223.237:554/live/1/66251FC11353191F/e7ooqwcfbqjoo80j.sdp

HTTP协议直播源

香港卫视：http://live.hkstv.hk.lxdns.com/live/hks/playlist.m3u8

CCTV1高清：http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8

CCTV3高清：http://ivi.bupt.edu.cn/hls/cctv3hd.m3u8

CCTV5高清：http://ivi.bupt.edu.cn/hls/cctv5hd.m3u8

CCTV5+高清：http://ivi.bupt.edu.cn/hls/cctv5phd.m3u8

CCTV6高清：http://ivi.bupt.edu.cn/hls/cctv6hd.m3u8

#------------------------------
 ffplay http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8 #效果好，满屏
 ffplay http://ivi.bupt.edu.cn/hls/cctv5phd.m3u8 #OK
 ffplay rtsp://218.204.223.237:554/live/1/66251FC11353191F/e7ooqwcfbqjoo80j.sdp #不通
 ffplay http://ivi.bupt.edu.cn/hls/cctv3hd.m3u8

 #---------------
 ffplay rtsp://admin:12345@192.168.1.1:554/h264/ch1/main/av_stream

 rtmp测试地址（可用）

香港卫视: rtmp://live.hkstv.hk.lxdns.com/live/hks1  #不能用
香港财经     rtmp://202.69.69.180:443/webcast/bshdlive-pc
韩国GoodTV,  rtmp://mobliestream.c3tv.com:554/live/goodtv.sdp
韩国朝鲜日报, rtmp://live.chosun.gscdn.com/live/tvchosun1.stream
美国1, rtmp://ns8.indexforce.com/home/mystream
美国2, rtmp://media3.scctv.net/live/scctv_800
美国中文电视,rtmp://media3.sinovision.net:1935/live/livestream #NO
湖南卫视 rtmp://58.200.131.2:1935/livetv/hunantv  #OK
#-------------------------------

