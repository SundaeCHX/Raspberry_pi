# Raspberry_pi

利用微信充当树莓派控制客户端，可实现音乐播放、语音机器人、视频监控等功能。

运行 python pi_wechat.py ，扫描二维码登录，通过“文件传输助手”发送命令“启动树莓派”。

将音乐文件拷贝至 Raspberry_pi/music/ 目录下，修改 pi_wechat.py 代码可构建自己的音乐列表。

如果你的树莓派有一块LCD屏幕，你可以运行 python Raspberry_pi/pi_desktop/desktop.py 来拥有一个时间桌面。



Use WeChat as a Raspberry_pi control client, can achieve music player, voice robot, video monitoring and other functions.

Run python pi_wechat.py , scan the two-dimensional code login, through the "file transfer assistant" to send the command "启动树莓派".

Copy the music files to the Raspberry_pi / music / directory and modify the pi_wechat.py code to build your own music list.

If your Raspberry_pi has an LCD screen, you can run the python Raspberry_pi / pi_desktop / desktop.py to have a time desktop.

    播放自定义内容命令格式为:
     “pi 内容”
    与语音机器人对话命令格式为:
     “robot 内容”
    查看音乐列表请输入:
     “pi 音乐列表”
    查看设备信息请输入:
     "pi 设备信息"
    查看视频监控请输入:
     "pi 监控"
