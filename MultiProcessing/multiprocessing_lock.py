import time
import multiprocessing

def deposit(balance,lock):
    for _ in range(10):
        time.sleep(0.01)
        lock.acquire()
        balance.value += 1
        lock.release()

def withdraw(balance,lock):
    for _ in range(10):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= 1
        lock.release()



if __name__ == "__main__":
    balance = multiprocessing.Value('i', 100)
    lock = multiprocessing.Lock()

    t1 = multiprocessing.Process(target=deposit, args=(balance,lock))
    t2 = multiprocessing.Process(target=withdraw, args=(balance,lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final balance:", balance.value)  