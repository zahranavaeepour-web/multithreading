from threading import Thread , Lock
import time
import random
def dining(i):
    rand = random.randint(3,7)
    time.sleep(rand)
    print(f"Philosopher {i + 1} is dining for {rand} second.")
def thinking(i):
    print(f"\t\t\t\t\t\tPhilosopher {i + 1} is thinking.")
    time.sleep(5)

def check(i,locks,n):
    while True :
        locks[i].acquire()
        if locks[(i+1)%n].acquire(blocking= False):
            dining(i)
            locks[(i+1)%n].release()
            locks[i].release()
            break
        else:
            locks[i].release()
            thinking(i)
        



if __name__ == "__main__":
    n=20
    thread_list = []
    locks =[Lock() for i in range(n)]
    for i in range(n):
        thread = Thread(target=check,args=(i,locks,n))
        thread.start()
        thread_list.append(thread)
    for th in thread_list:
        th.join()

    print("Philosophers dining finished.")
