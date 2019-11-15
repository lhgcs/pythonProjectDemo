#!/usr/bin/python

'''
@Description: 语音转文本
@Author: your name
@Date: 2019-10-26 17:18:41
@LastEditTime: 2019-10-26 17:34:10
@LastEditors: Please set LastEditors
'''

# https://www.i5seo.com/python-simple-realize-speech-recognition.html
# https://github.com/realpython/python-speech-recognition/blob/master/audio_files/harvard.wav


'''
# 使用麦克风
sudo apt-get install python-pyaudio python3-pyaudio
pip3 install pyaudio
# 语音识别
pip3 install SpeechRecognition
'''

import speech_recognition as sr
print(sr.__version__)

#获取文件数据
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
	#去除噪声
	r.adjust_for_ambient_noise(source, duration=0.5)
	#audio = r.record(source)
	#offset偏移,durration停止
	audio = r.record(source, offset=4.7, duration=2.8)

#识别器
r.recognize_google(audio，show_all=True)

# import speech_recognition as sr
# r = sr.Recognizer()

# mic = sr.Microphone()
# sr.Microphone.list_microphone_names()

# mic = sr.Microphone(device_index=3)
# with mic as source:
# 	audio = r.listen(source)
