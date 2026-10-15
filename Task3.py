import os
import time
from multiprocessing import Process
def child_process(number):
    print(
        f"Child {number} running... PID: {os.getpid()}",
        flush=True
    )
    time.sleep(2)

    print(
        f"Child {number} finished. PID: {os.getpid()}",
        flush=True
    )

if __name__ == "__main__":
    children = []

    for i in range(2):
        p = Process(target=child_process, args=(i + 1,))
        p.start()
        children.append(p)

    print("Parent waiting for both children...", flush=True)
    for p in children:
        p.join()
    print("Parent resumes after both children terminate.")
