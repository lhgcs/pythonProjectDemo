#!/usr/bin/python3

'''
@Description: 文本转语音
@Author: your name
@Date: 2019-10-26 15:52:29
@LastEditTime: 2019-10-26 17:14:00
@LastEditors: Please set LastEditors
'''

import pyttsx3

t1 ='I don’t know what to say. I didn’t know that there would be a podium with a microphone. I thought I would just be singing songs. Not to downplay that, but …'
t2 ='我不知说什么好了。我不知道这边有一个带麦克风的讲台。我还以为只要唱几首歌就好了。不是说那不重要。'
engine = pyttsx3.init()
engine.say(t2)
engine.runAndWait()
engine.endLoop()
