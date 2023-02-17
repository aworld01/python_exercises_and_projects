import socket

def net():
    try:
        socket.create_connection(("google.com",80))
        return True
    except OSError:
        return False

if net():
    print("Internet is connected...")
else:
    print("Computer not connected")
    print("Make sure your computer has an active Internet connection")