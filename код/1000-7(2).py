from re import S
import time
from tracemalloc import start
n = 1000
while n > -100000000:
    n -= 7
    time.sleep(0.10)
    print(n)
start(S)
