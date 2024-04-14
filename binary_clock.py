from datetime import datetime
from time import sleep
from subprocess import Popen

def tb(tl: list[tuple], d: str) -> str: return d.join([format(n, 'b').zfill(f).replace('0', '⚪ ').replace('1', '⚫ ') for n, f in tl])

def show(ts=False) -> str:
    n = datetime.now()
    if ts: return tb([(int(n.timestamp()), 38), (n.microsecond, 20)], '.')
    return tb([(n.year, 13), (n.month, 4), (n.day, 5), (n.hour, 5), (n.minute, 6), (n.second, 6), (n.microsecond, 20)], '\n')

def clock(ts=False):
    while True:
        print(show(ts))
        sleep(0.05)
        Popen('clear').wait()

if __name__ == '__main__': clock()