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
    locks[i].acquire()
    if i + 1 < n :
        m = i + 1
    else:
        m = 0
    if locks[m].acquire(blocking= False):
        dining(i)
        locks[m].release()
        locks[i].release()
        
    else:
        locks[i].release()
        thinking(i)
        check(i,locks,n)



if __name__ == "__main__":
    n=50
    thread_list = []
    locks =[Lock() for i in range(n)]
    for i in range(n):
        thread = Thread(target=check,args=(i,locks,n))
        thread.start()
        thread_list.append(thread)
    for th in thread_list:
        th.join()

    print("Philosophers dining finished.")
