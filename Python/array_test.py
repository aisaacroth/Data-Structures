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
        pass

    def testArrayStackSet(self):
        pass

    def testArrayStackAdd(self):
        pass

    def testArrayStackRemove(self):
        pass


if __name__ == '__main__':
    unittest.main()
