import unittest

class FunctionTest(unittest.TestCase):

    def test_function(self):

        def test():
            """this is doc of test function"""
            pass

        self.assertEqual(test.__name__, 'test')
        self.assertEqual(test.__doc__, 'this is doc of test function')

    def test_assign_method(self):
        """通过对象引用的方法,已经绑定好了self"""
        class MyClass:

            def __init__(self):
                self.foo = 'foo'
                self.bar = 'bar'

            def method(self):
                return self.foo

        method = MyClass().method

        self.assertEqual(method(), 'foo')
