#!/usr/bin/env python

# TCP
# 2015-07-20 17:14:25

# 导入socket库
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
s.connect(('www.baidu.com', 80))

# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')



