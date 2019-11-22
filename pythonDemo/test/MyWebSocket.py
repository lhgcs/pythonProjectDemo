#!/usr/bin/env python3

'''
@Description: websocket
@Version: 1.0
@Autor: lhgcs
@Date: 2019-11-15 15:11:23
@LastEditors: lhgcs
@LastEditTime: 2019-11-15 15:24:39
'''

# pip install websocket --user
# pip install websocket-client --user

import websocket

'''
@description: 连接成功
@param {type} 
@return: 
'''
def on_open(ws):
   req = '{"type":"getDebugFrame"}'
   ws.send(req)

'''
@description: 收到数据
@param {type} 
@return: 
'''
def on_message(ws, message):
    print(message)

'''
@description: 异常
@param {type} 
@return: 
'''
def on_error(ws, error):
   print(error)

'''
@description: 关闭
@param {type} 
@return: 
'''
def on_close(ws):
   print("Connection closed")
   ws.close()


if __name__ == "__main__":
   websocket.enableTrace(True)
   ws = websocket.WebSocketApp("ws://localhost:6040",
                               on_message=on_message,
                               on_error=on_error,
                               on_close=on_close)
   ws.on_open = on_open
   ws.run_forever(ping_timeout=5)
