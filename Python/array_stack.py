#!/usr/bin/env python3
''' ArrayStack Data Structure implemented in Python.

Author: Alexander Roth
Date:   2014-11-26
'''

class ArrayStack:

    def __init__(self):
        self.array = []
        self.count = 0

    def get(self,i):
        return self.array[i]

    def set(self, i, new_value):
        temp = self.array[i]
        self.array[i] = new_value
        return temp

    def add(self, i, new_value):
        if self.count == len(self.array):
            self.resize()
        j = i
        for j in range(self.count):
            self.array[j + 1] = self.array[j]
        self.array[i] = new_value
        self.count += 1

    def remove(self, i):
        temp = self.array[i]
        j = i
        for j in xrange(self.count):
            self.array[j] = self.array[j + 1]
        self.count -= 1
        if len(self.array) >= 3 * self.count:
            self.resize()
        return temp
