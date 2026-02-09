import multiprocessing

def calc_square(numbers, queue):
    for n in numbers:
        queue.put(n * n) 

    
if __name__ == "__main__":
    arr = [2, 3, 4, 5]
    queue = multiprocessing.Queue()  # Create a Queue to share data between processes
    p1 = multiprocessing.Process(target=calc_square, args=(arr, queue))
    p1.start()
    p1.join()

    while not queue.empty():
        print("Square from queue:", queue.get())  