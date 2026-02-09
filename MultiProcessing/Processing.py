import multiprocessing

square_result = []

def calc_square(numbers):
    for n in numbers:
        square_result.append(n * n)
    print("Within the thread Square Result:", square_result)



if __name__ == "__main__":
    arr = [2, 3, 4, 5]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()
    p1.join()
    print("Outside the thread Square Result:", square_result)


# Outside the thread Square Result: [] because each process has its own memory space (address 0x7f8c2d3e4b80) and does not share global variables.