import unittest


class WithTest(unittest.TestCase):

    def test_how_to_use_with(self):
        """with expression as v [, expression as v]"""
        with open(__file__, 'r') as f:
            self.assertEqual(f.readline(), 'import unittest\n')

    def test_object_in_with_statement(self):
        """
        expression生成一个context manager对象，这个对象有两个
        方法：
            __enter__   返回结果会被赋值给as后面的v
            __exit__    如果with的body有异常，异常的相关参数会被传入这个函数，
                        返回结果如果是True，继续执行，False的话，异常会被继续抛出
                        如果这个方法抛出异常，此异常会代替之前的异常被抛出
        """
        f = open(__file__, 'r')
        self.assertTrue(hasattr(f, '__enter__'))
        self.assertTrue(hasattr(f, '__exit__'))
        f.close()

    def test_enter_of_context_manager(self):
        obj = []

        class ctx:
            def __enter__(self):
                return obj

            def __exit__(self, exc_type, exc_val, exc_tb):
                del exc_type, exc_val, exc_tb
                return True

        with ctx() as o:
            self.assertTrue(o is obj)

