def topten():
    n = 1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1


# values=topten()
# for i in values:
for i in topten():
    print(i)

'''generaters accupy less space'''
'''Generator in python let us write fast and compact code. This is an advantage over Python iterators. They are also simpler to code than do custom iterator.'''
'''Python iterator is more memory-efficient'''


def func():
    i = 1
    while i > 0:
        yield i
        i -= 1


for i in func():
    print(i)
1

func().__sizeof__()
32
Here, we
got
32.
But
for a python iterator, we get 16.

'''Generator in python is a subclass of Iterator. To prove this, we use the issubclass() function'''.

import collections, types

issubclass(types.GeneratorType, collections.Iterator)
True

issubclass(collections.Generator, collections.Iterator)
True

issubclass(collections.Iterator, types.GeneratorType)
False

Python
iterator is an
iterable
Iterator in python is a
subclass
of
Iterable.

issubclass(collections.Iterator, collections.Iterable)