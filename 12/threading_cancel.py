import threading
import itertools
from time import sleep
import sys


class Signal:
    # 通过对象的go属性控制线程的结束
    go = True


def spin(msg, signal):
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        sys.stdout.write(status)
        sys.stdout.flush()
        sys.stdout.write('\x08'*len(status))
        sleep(.5)
        if not signal.go:
            break
    sys.stdout.write(' '*len(status))
    sys.stdout.write('\x08'*len(status))


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('waiting...', signal))
    spinner.start()
    sleep(3)
    signal.go = False
    spinner.join()


def main():
    supervisor()
    print('Finish!')


if __name__ == "__main__":
    main()