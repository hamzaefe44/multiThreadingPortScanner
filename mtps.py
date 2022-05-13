import socket
import threading
import queue




IP_ADDRESS = '192.168.43.60'#YOUR TARGET IP ADDRESS
q = queue.Queue()

# Storing port numbers in our query
for i in range(130, 1000):
    q.put(i)


def scan():
    while not q.empty():
        port=q.get()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((IP_ADDRESS, port))
                print("[+]port:{}".format(port))
            except:
                pass
        q.task_done()

thred_l=[]
# Thread numbers 
for i in range(30):
    t = threading.Thread(target=scan, daemon=True)
    thred_l.append(t)
for i in thred_l:
    i.start()
q.join()
print("Finished")
