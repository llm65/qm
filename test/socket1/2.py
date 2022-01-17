import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 6669))
server_socket.listen(5)


def send():
    while True:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect(("localhost", 6666))
        msg = input()
        c.send(msg.encode('utf-8'))
        c.close()


def recv():
    while True:
        s, addr = server_socket.accept()
        msg = s.recv(1024)
        print(msg.decode('utf-8'))
        s.close()


if __name__ == '__main__':
    t1 = threading.Thread(target=send, args=())
    t2 = threading.Thread(target=recv, args=())
    t1.start()
    t2.start()


# 读取消息 打印 关闭连接
# msg = c.recv(1024)
# print(msg.decode('utf-8'))
# c.close()
