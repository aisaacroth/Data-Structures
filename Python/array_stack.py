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
        ''' Operates in O(1) time '''
        if i < 0 or i >= self.count:
            raise IndexError()
        return self.array[i]

    def set(self, i, new_value):
        ''' Operates in O(1) time '''
        if i < 0 or i >= self.count:
            raise IndexError()
        temp = self.array[i]
        self.array[i] = new_value
        return temp

    def add(self, i, new_value):
        ''' Operates in O(1 + n - i) time '''
        if self.count == len(self.array):
            self.resize()
        self.array[i + 1: self.count + 1] = self.array[i: self.count]
        self.array[i] = new_value
        self.count += 1

    def remove(self, i):
        ''' Operates in O(1 + n - i) time '''
        if i < 0 or i >= self.count:
            raise IndexError()
        temp = self.array[i]
        self.array[i: self.count - 1] = self.array[i + 1: self.count]
        self.count -= 1
        if len(self.array) >= 3 * self.count:
            self.resize()
        return temp

    def resize(self):
        new_array = [None] * (max(1, 2 * self.count))
        new_array[0: self.count] = self.array[0: self.count]
        self.array = new_array
