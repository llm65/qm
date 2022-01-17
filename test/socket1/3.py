import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 6666))
server_socket.listen(5)

g_conn_pool = []
while True:
    s, addr = server_socket.accept()
    g_conn_pool.append(s)
    print(g_conn_pool)
    msg = s.recv(1024)
    print(msg.decode('utf-8'))
    s.close()
