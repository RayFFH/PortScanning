import socket
import threading
from queue import Queue

q = Queue()
ip = '127.0.0.1'
print_l = threading.Lock()

def port_scanning(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = s.connect_ex((ip, port))
    print_l.acquire()
    try:
        print("port",port, "is open")
    finally:
        print_l.release()

    s.close()


def thread_maker():
    while True:
        worker = q.get()
        port_scanning(worker)
        q.task_done()


for x in range(30):
    t= threading.Thread(target = thread_maker)
    t.daemon = True
    t.start()

for worker in range (1,23):
    q.put(worker)

q.join()