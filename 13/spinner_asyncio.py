import asyncio
import itertools
import sys


@asyncio.coroutine
def spin(msg):
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        print(status, end='')
        sys.stdout.flush()
        print('\x08'*len(status), end='')
        try:
            yield from asyncio.sleep(.5)
        except asyncio.CancelledError:
            break
    sys.stdout.write(' '*len(status))
    sys.stdout.write('\x08'*len(status))


@asyncio.coroutine
def supervisor():
    spinner = asyncio.async(spin('waiting...'))
    yield from asyncio.sleep(3)
    spinner.cancel()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(supervisor())
    loop.close()
    print('Finish!')


if __name__ == "__main__":
    main()
