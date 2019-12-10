from threading import *
from time import *


def wish(name):
    for i in range(10):
        print('good evening:', end='')
        sleep(0.2)
        print(name)


t1 = Thread(target=wish, args=('yuvraj',))
t2 = Thread(target=wish, args=('dhoni,'))

t2.start()
t1.start()

'=============================='


def topten():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6


values = topten()

# print(values.__next__())
# print(values.__next__())


for i in values:
    print(i)