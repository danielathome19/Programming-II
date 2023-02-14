import time
import threading as th

def print_nums(start, end, delay):
  for i in range(start, end):
    time.sleep(delay)
    print(i, " ")

def print_lets(delay):
  for letter in "abcdefghi":
    time.sleep(delay)
    print(letter)

t1 = th.Thread(target=print_nums, args=(1, 10, 0.5)).start()
# t2 = th.Thread(target=print_nums, args=(11, 20, 0.5)).start()
t2 = th.Thread(target=print_lets, args=(0.5,)).start()
# Wait for threads to complete before exiting
t1.join()
t2.join()