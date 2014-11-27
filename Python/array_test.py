#!/usr/bin/env python3
''' Test cases for testing the functionality of the array data structures

Author: Alexander Roth
Date:   2014-11-27
'''
import unittest
from array_stack import ArrayStack

class TestArrayStackFunctions(unittest.TestCase):

    def setUp(self):
        self.array_stack = ArrayStack()

    def testArrayStackInitialize(self):
        self.assertIsNotNone(self.array_stack)
        self.assertEqual(self.array_stack.count, 0)

    def testArrayStackGet(self):
        self.array_stack.add(0, 'a')
        value = self.array_stack.get(0)
        self.assertEqual('a', value)

    def testArrayStackSet(self):
        self.array_stack.add(0, 'a')
        value = self.array_stack.set(0, 1)
        self.assertEqual('a', value)
        self.assertIn(1, self.array_stack.array)
        self.assertEqual(1, self.array_stack.count)

    def testArrayStackAdd(self):
        self.array_stack.add(0, 'a')
        self.assertEqual(self.array_stack.count, 1)
        self.assertIn('a', self.array_stack.array)

    def testArrayStackRemove(self):
        self.array_stack.add(0, 'a')
        value = self.array_stack.remove(0)
        self.assertEqual('a', value)
        self.assertEqual(0, self.array_stack.count)


if __name__ == '__main__':
    unittest.main()
