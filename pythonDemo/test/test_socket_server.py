#!/usr/bin/env python3

'''
@Description: socket服务端
@Version: 1.0
@Autor: lhgcs
@Date: 2019-06-10 14:41:21
@LastEditors: lhgcs
@LastEditTime: 2019-11-22 15:51:11
'''

import socket
import time

if __name__ == "__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(("192.168.0.110", 4800))
    sk.listen(25)
    while True:
        client,addr = sk.accept()
        while True:
            try:
                msg = client.recv(1024)
                # if b'' != msg:
                print(msg)
                if msg == bytes("close", encoding="utf-8"):
                    print("close")
                client.send(bytes("123", encoding="utf-8"))
                time.sleep(2)
            except Exception as e:
                client.close()
                client = None
                print(e)
                break
   
    if sk is not None:
        sk.close()
