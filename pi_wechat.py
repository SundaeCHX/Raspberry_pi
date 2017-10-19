#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 19:44:28
# @Author  : Sundae Chen (sundaechn@gmail.com)
# @Link    : http://sundae.applinzi.com/home

import itchat
import urllib
import urllib2
import re
import base64
import pygame
import sys
import time
import subprocess
import os
import commands


@itchat.msg_register(itchat.content.TEXT)
def text(msg):
    global child
    if msg['ToUserName'] != 'filehelper':
        return
    content = msg['Text']
    if content == u'启动树莓派':
        itchat.send(u'----Raspberry---已启动----'+'\n'+u'''播放自定义内容命令格式为:
“pi 内容”
与语音机器人对话命令格式为:
“robot 内容”
查看音乐列表请输入:
“pi 音乐列表”
查看设备信息请输入:
 "pi 设备信息"''', 'filehelper')
        speech(u'树莓派已启动')
    if content[0:5] == 'robot':
        txt = content[6:-1]+content[-1]
        word = Robot(txt, 'Sundae')
        speech(word)
        return
    if content[0:2] == 'pi':
        txt = content[3:-1]+content[-1]
        if txt == u'设备信息':
            check()
            return
        if txt == u'监控':
            subprocess.call(['fswebcam', '--no-banner', '-r',
                             '640x480', 'image.jpg'], shell=False)
            itchat.send('@img@%s' % 'image.jpg', 'filehelper')
            return
        if txt == u'音乐列表':
            itchat.send(u'----Raspberry---音乐列表----'+'\n' +
                        u'''1.我好喜欢你你喜不喜欢我
2.童话镇
3.七色シンフォニー
4.那就这样吧
5.Say You Will
6.追梦赤子心
7.光るなら
8.Beautiful In White
9.キラメキ
10.致姗姗来迟的你
11.鲁莽灰飞烟灭前
12.奇妙能力歌
13.不说再见
14.最后一个夏天
15.热河
16.背影
17.自然醒
18.七月上
19.北京东路的日子
20.阴天
21.回忆
22.耿耿于怀
23.你离开了宝鸡中学，从此没有人和我说话
24.单车带我去西藏
25.眉间雪
26.成都
27.说谎
28.我已经敢想你
29.热血无赖
30.白昼之月
31.残酷月光
32.浪费
33.神秘嘉宾
34.想自由
35.生活不止眼前的苟且
36.崇拜 (Live)
37.江南
38.修炼爱情
39.爱的就是你 (浪漫版)
40.大城小爱
41.你不知道的事
42.唯一 
43.我们的歌
44.依然爱你
45.半岛铁盒
46.彩虹
47.东风破
48.发如雪
49.告白气球
50.给我一首歌的时间
51.简单爱
52.龙卷风
53.七里香
54.晴天
55.手写的从前
56.说好的幸福呢
57.听妈妈的话
58.星晴
59.烟花易冷
60.一路向北
61.梵高先生
62.山阴路的夏天
63.天空之城
64.和你在一起2013版[Live]
65.忽然（2012 Live）
66.热河 2015现场版
67.寻找

播放命令为：
music 序号
music 随机播放
music 停止播放
music 下一首

李志歌单:
music 李志''', 'filehelper')
            return
        else:
            speech(txt)
            return
    if content[0:5] == 'music':
        txt = content[6:-1]+content[-1]
        if txt == u'随机播放':
            itchat.send('----Raspberry----'+'\n'+u'正在播放', 'filehelper')
            child = subprocess.Popen(
                ['mplayer', '-shuffle', '-playlist', 'music/playlist.txt'], shell=False)
            return
        elif txt == u'停止播放':
            child.terminate()
            itchat.send('----Raspberry----'+'\n'+u'播放停止', 'filehelper')
            return
        elif txt == u'下一首':
            child.terminate()
            child = subprocess.Popen(
                ['mplayer', '-shuffle', '-playlist', 'music/playlist.txt'], shell=False)
            return
        elif txt == u'李志':
            itchat.send('----Raspberry----'+'\n'+u'正在播放', 'filehelper')
            child = subprocess.Popen(
                ['mplayer', '-shuffle', '-playlist', 'music/playlist_lz.txt'], shell=False)
        else:
            music = 'music/'+txt+'.mp3'
            if os.path.exists(music):
                itchat.send('----Raspberry----'+'\n'+u'正在播放', 'filehelper')
                child = subprocess.Popen(
                    ['mplayer', '-loop', '0', music], shell=False)
                return
            else:
                itchat.send('----Raspberry----'+'\n'+u'该文件不存在', 'filehelper')
                return


def speech(txt):
    itchat.send('----Raspberry----'+'\n'+u'准备播放', 'filehelper')
    api = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=m2IC97MaSDKd8P1RTCCjieE5&client_secret=39db1835eb14f86b9327aa2738f567d1'
    request = urllib2.Request(api)
    response = urllib2.urlopen(request)
    content = response.read()
    result = re.findall(r'{"access_token":"(.*?)"', content, re.S)
    access_token = result[0]
    url = 'http://tsn.baidu.com/text2audio'
    txt = txt.encode('utf-8')
    data = urllib.urlencode({'tex': txt, 'lan': 'zh', 'cuid': 'Sundae',
                             'tok': access_token, 'ctp': 1, 'vol': 9, 'per': 0, 'pit': 7, 'spd': 5})
    req = urllib2.Request(url)
    res = urllib2.urlopen(req, data)
    answer = res.read()
    with open('speech.mp3', 'wb') as f:
        f.write(answer)
    subprocess.call(['mplayer', 'water.mp3'], shell=False)
    subprocess.call(['mplayer', 'speech.mp3'], shell=False)
    itchat.send('----Raspberry----'+'\n'+u'播放完毕', 'filehelper')
    return


def Robot(content, toUser):
    api = 'http://www.tuling123.com/openapi/api'
    apikey = 'db33db678c254e33abc877db64548fb6'
    content = content.encode('utf-8')
    toUser = toUser.encode('utf-8')
    data = urllib.urlencode({'key': apikey, 'info': content, 'userid': toUser})
    request = urllib2.Request(api, data)
    response = urllib2.urlopen(request)
    answer = response.read()
    results = re.findall('"text":"(.*?)"', answer)
    for result in results:
        return result.decode('utf-8')


def check():
    cpu_tempFile = open('/sys/class/thermal/thermal_zone0/temp')
    cpu_temp = cpu_tempFile.readline()
    cpu_tempFile.close()
    cpu_temp = round(float(cpu_temp)/1000, 1)
    cpu_use = os.popen(
        "top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()
    gpu_temp = commands.getoutput(
        '/opt/vc/bin/vcgencmd measure_temp').replace('temp=', '').replace('\'C', '')
    gpu_temp = float(gpu_temp)
    RAM_stats = getRAMinfo()
    RAM_total = round((int(RAM_stats[0])+int(RAM_stats[1]))/1024, 1)
    RAM_used = round(int(RAM_stats[0])/1024, 1)
    RAM_free = round(int(RAM_stats[1])/1024, 1)
    DISK_stats = getDiskSpace()
    DISK_total = DISK_stats[0]
    DISK_used = DISK_stats[1]
    DISK_free = DISK_stats[2]
    DISK_perc = DISK_stats[3]
    itchat.send('----Raspberry---Infomation----'+'\n'+'CPU Temperature = '+str(cpu_temp)+'\n' +
                'CPU Use = '+str(cpu_use)+'%'+'\n' +
                'GPU Temperature = '+str(gpu_temp)+'\n\n' +
                'RAM Total = '+str(RAM_total)+' MB'+'\n' +
                'RAM Used = '+str(RAM_used)+' MB'+'\n' +
                'RAM Free = '+str(RAM_free)+' MB'+'\n\n' +
                'DISK Total Space = '+str(DISK_total)+'B'+'\n' +
                'DISK Used Space = '+str(DISK_used)+'B'+'\n' +
                'DISK Free Space = '+str(DISK_free)+'B'+'\n' +
                'DISK Used Percentage = '+str(DISK_perc)+'\n\n' +
                'External Temperature = '+str(getTemperature())+u'℃', 'filehelper')
    return


def getRAMinfo():
    p = os.popen('free')
    i = 0
    while True:
        i = i+1
        line = p.readline()
        if i == 3:
            return (line.split()[2:4])


def getDiskSpace():
    p = os.popen('df -h /')
    i = 0
    while True:
        i = i+1
        line = p.readline()
        if i == 2:
            return(line.split()[1:5])


def getTemperature():
    temfile = open('/sys/bus/w1/devices/28-0516a2855eff/w1_slave')
    text = temfile.read()
    temfile.close()
    line = text.split('\n')[1]
    data = line.split(' ')[9]
    tem = float(data[2:])
    tem = tem/1000
    return tem


itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run()
