import time

def calc_square(numbers):
    print("Calculating squares...")
    for n in numbers:
        time.sleep(0.2)
        print('Square of :', n*n)


def calc_cube(numbers):
    print("Calculating cubes...")
    for n in numbers:
        time.sleep(0.2)
        print('Cube of :', n*n*n)


arr = [2, 3, 4, 5]

t = time.time()
calc_square(arr)
calc_cube(arr)


print("Total time taken:", time.time() - t)  #1.6074023246765137