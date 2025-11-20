import time
from threading import Thread
class Task1(Thread):
    def run(self):
        for i in range(1,100+1):
            if i%2 !=0:
                print(i)
                time.sleep(1)
class Task2(Thread):
    def run(self):
        for i in range(1,100+1):
            if i%2 ==0:
                print(i)
                time.sleep(1)
t1 = Task1()
t2 = Task2()
t1.start()
time.sleep(0.5)
t2.start()
            