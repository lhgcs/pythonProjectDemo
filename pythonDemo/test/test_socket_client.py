#!/usr/bin/env python3

'''
@Description: socket客户端
@Version: 1.0
@Autor: lhgcs
@Date: 2019-06-10 14:41:21
@LastEditors: lhgcs
@LastEditTime: 2019-11-22 15:50:50
'''

import socket

if __name__ == "__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(("192.168.0.105", 8888))

    while True:
        try:
            msg = sk.recv(1024)
            # if b'' != msg:
            print(msg)
            if msg == bytes("close", encoding="utf-8"):
                print("close")
            sk.send(bytes("123", encoding="utf-8"))
        except Exception as e:
            sk.close()
            sk = None
            print(e)
            break

    if sk is not None:
        sk.close()
        