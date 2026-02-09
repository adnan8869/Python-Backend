from multiprocessing import Pool
import time


def fun(n):
    sum = 0
    for i in range(n):
        sum += i * i
    return sum

if __name__ == "__main__":
    t1 = time.time()
    p=Pool()  # Can use processes=n to specify number of worker processes
    result = p.map(fun, range(10000))  # Distribute the tasks among the worker processes
    p.close() 
    p.join() 
    print("Time taken in multiprocessing pool:", time.time() - t1) 


    # To see the result of computations
    t2 = time.time()
    result = []
    for x in range(10000):
        result.append(fun(x))
    print("Time taken in sequential execution:", time.time() - t2)