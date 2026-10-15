import os
from multiprocessing import Process
def child_process(number):
    print(
        f"Child {number} → PID: {os.getpid()}, "
        f"PPID: {os.getppid()}",
        flush=True
    )
if __name__ == "__main__":
    children = []

    for i in range(2):
        p = Process(target=child_process, args=(i + 1,))
        p.start()
        children.append(p)
    print("Parent PID:", os.getpid())
    for i, p in enumerate(children, start=1):
        print(f"Child {i} PID:", p.pid)
    for p in children:
        p.join()
    print("Parent: Both children have finished.")
