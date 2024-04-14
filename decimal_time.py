from datetime import datetime
from time import sleep
from subprocess import Popen

def calculate_current_time() -> str:
    decimal = str((datetime.now().timestamp() % 86400) / 86400)
    return ':'.join([decimal[2:3], decimal[3:5], decimal[5:7], decimal[8:14]])

def show_clock():
    while True:
        print(calculate_current_time())
        sleep(0.01)
        Popen('clear').wait()

if __name__ == '__main__': show_clock()
