# 15.1
import multiprocessing
import time

def wait_n_time(wait):
    time.sleep(wait)

    now = time.time()
    print(time.ctime(now))

if __name__ == "__main__":
    for i in range(3):
        p = multiprocessing.Process(target= wait_n_time, args= (2*i + 1,))

        p.start()