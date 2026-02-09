import multiprocessing

def calc_square(numbers, square_result , v):
    v.value = 5
    for i, n in enumerate(numbers):
        square_result[i] = n * n
    print("Within the process Square Result:", list(square_result))

if __name__ == "__main__":
    numbers = [2, 3, 4, 5]
    # Using multiprocessing.Array to share data between processes( data type, size)
    square_result = multiprocessing.Array('i', len(numbers)) 
     # Value can be used to share a single value between processes
    v= multiprocessing.Value('i', 0)  

    p1 = multiprocessing.Process(target=calc_square, args=(numbers, square_result, v))
    p1.start()
    p1.join()
    print("Outside the process Square Result:", square_result[:]) 
    print("Outside the process Square Result:", v.value) 