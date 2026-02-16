# with open("data.txt", "w") as f:
#     f.write("Hello World")
# File is automatically closed here!




# Custom context manager using a class:
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"Time elapsed: {self.end - self.start:.4f} seconds")

with Timer():
    # Do some heavy work
    sum(i*i for i in range(1000000))