import socket

HOST = "127.0.0.1"
PORT = 4000
Stop = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Receive the first one manually because it doesn't contain 'continue'
    data = s.recv(1024)
    data = data.decode("utf-8")

    # Get the word sent
    to_reverse = data.split(" ")[-1]
    to_reverse = to_reverse[: len(to_reverse) - 1]
    print(to_reverse)

    # Reverse it and add '\n' so it's read by the server
    to_send = "".join(reversed(to_reverse))
    to_send += "\n"
    s.sendall(to_send.encode())

    while not Stop:
        data = s.recv(1024)
        data = data.decode("utf-8")
        
        # If we receive to continue we continue, else we stop and print the data (the flag)
        if "continue" in data:
            to_reverse = data.split(" ")[-1]
            to_reverse = to_reverse[: len(to_reverse) - 1]
            print(to_reverse)

            to_send = "".join(reversed(to_reverse))
            to_send += "\n"
            s.sendall(to_send.encode())
        
        else:
            print(data)
            Stop = True
