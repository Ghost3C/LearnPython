import socket
UDP_IP = '127.0.0.1'
UDP_PORT = 10080

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))
print('准备接收内容')
while 1:
    data,addr = sock.recvfrom(1024) # 设置接收数据包的缓存区为1024byte，如果数据包大于这个值，则数据包不会接收大于缓冲区设定值的数据包。
    print('从{ip}:{port},接收到内容:{data}'.format(ip=addr[0],port=addr[1],data=data.decode('utf-8')))
    
