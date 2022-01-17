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
