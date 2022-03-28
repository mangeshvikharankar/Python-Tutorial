
# Multithreading is used to run thread(process) parallely.
from threading import Thread
from time import sleep


class Hi(Thread):
    def run(self):
        for i in range(3):
            print("Hiii")
            sleep(1)

class Hello(Thread):
    def run(self):
        for i in range(3):
            print("Hello")
            sleep(1)

t1 = Hi()
t2 = Hello()

t1.start()    # for run thread we use start() method
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("end") # after t1 and t2 join this will run


