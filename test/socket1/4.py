import socket


def send(m):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("localhost", 6666))
    c.send(m.encode('utf-8'))
    c.close()


while True:
    m1 = input()
    if m1:
        send(m1)


# while True:
#     c = socket1.socket1(socket1.AF_INET, socket1.SOCK_STREAM)
#     c.connect(("localhost", 6666))
#     msg = input()
#     c.send(msg.encode('utf-8'))
#     c.close()
