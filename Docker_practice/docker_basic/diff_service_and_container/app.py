import time

i = 20

while True:
    result = 100/i
    i -= 1
    print(i, flush=True)
    time.sleep(1)

