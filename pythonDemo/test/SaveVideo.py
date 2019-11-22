'''
@Description: 保存视频
@Version: 1.0
@Autor: lhgcs
@Date: 2019-11-22 15:51:55
@LastEditors: lhgcs
@LastEditTime: 2019-11-22 15:59:23
'''

import cv2
import base64
import numpy as np
import time

vw = cv2.VideoWriter()


t1 = time.time()
frameNumber = 0
latestFps = 0

# 计算fps:1秒内获取到的帧数
def getFPS():
    global t1, frameNumber, latestFps
    frameNumber += 1
    t2 = time.time()
    if (t2 - t1 >= 1):
        latestFps = frameNumber
        t1 = time.time()
        frameNumber = 0
    return latestFps

# cv2.namedWindow("frame", 0)
# cv2.resizeWindow("frame", 800, 600)

def saveVideo(imgStr, trackerStr = ""):
    if len(imgStr) > 100:
        img_data = base64.b64decode(imgStr)
        # 转换为np数组
        img_array = np.fromstring(img_data, np.uint8)
        # 转换成opencv可用格式
        img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
        vw.write(img)
        if (cv2.waitKey(80) == ord('s')):
            # 初始化视频写入器
            vw.open("debug.mp4", cv2.VideoWriter_fourcc("M", "P", "4", "V"), 2, (img.shape[1], img.shape[0]))
            print("capture start", flush = True)
            vw.release()
            