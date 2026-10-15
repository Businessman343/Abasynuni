import os
import time
for i in range(5):
    print("Iteration:", i + 1)
    print("Current PID:", os.getpid())
    print("Parent PID:", os.getppid())
    print("--------------------")
    time.sleep(1)