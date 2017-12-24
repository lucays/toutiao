from concurrent import futures
import itertools
from time import sleep
import sys


class Signal:
    go = True


def spin(msg, signal):
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        # sys.stdout.write(status)
        print(status, end='')
        sys.stdout.flush()
        # sys.stdout.write('\x08'*len(status))
        print('\x08'*len(status), end='')
        sleep(.5)
        if not signal.go:
            break
    sys.stdout.write(' '*len(status))
    sys.stdout.write('\x08'*len(status))


def supervisor():
    signal = Signal
    with futures.ThreadPoolExecutor() as e:
        e.submit(spin, 'waiting...', signal)
        sleep(3)
        signal.go = False


def main():
    supervisor()
    print('Finish!')


if __name__ == "__main__":
    main()
