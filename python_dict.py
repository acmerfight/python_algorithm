#coding=utf-8

MIN_SIZE = 8


class Entry(object):
    __slots__ = ("key", "value", "hash")
    def __init__(self):
        self.key = None
        self.value = None
        self.hash = None

class Dict(object):
    def __init__(self):
        pass
    def clear():
        self.filled = 0
        self.used = 0
        self.mask = MIN_SIZE - 1
        self.table = []
        for i in xrange(MIN_SIZE):
            self.table.append(Entry())
