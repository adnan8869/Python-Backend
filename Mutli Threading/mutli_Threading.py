import time
import threading

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
# Creating threads
t1 = threading.Thread(target=calc_square, args=(arr,))  # Here arg is a tuple
t2 = threading.Thread(target=calc_cube, args=(arr,))
# Starting threads
t1.start()
t2.start()
# Waiting for both threads to complete
t1.join()
t2.join()

print("Total time taken:", time.time() - t)  # Time 0.8080644607543945