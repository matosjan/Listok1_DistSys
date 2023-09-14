import socket

HOST, PORT = "127.0.0.1", 12345 
data = b''
data_size = 0

def GET(conn):
    try:
        if data_size != 0:
            conn.sendall(bytes(str(data_size), encoding='utf-8'))
            conn.sendall(data)
        else:
            conn.sendall(bytes("0\n", encoding='utf-8'))
    except:
        return


def PUT(request, conn):
    global data
    global data_size
    content_len = request[3]
    if (len(request) > 5 + content_len and request[content_len + 4] != ord('\n')) or len(request) < 5 + content_len:
        try:
            conn.sendall('1\n'.encode("utf-8"))
        except:
            return
        return
    data = request[4:content_len + 5]
    data_size = content_len
    try:
        conn.sendall('0\n'.encode('utf8'))
    except:
        return
        

def start_server():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.bind((HOST, PORT)) 
    serv_sock.listen(10)

    while True:
        connection, addr = serv_sock.accept()
        request = connection.recv(260)
        if request is None or len(request) < 4:
            connection.close()
            continue

        procedure = request[:3].decode("utf-8")
        if procedure == "GET":
            GET(connection)
        elif procedure == "PUT":
            PUT(request, connection)
            
        connection.close()

    
start_server()
