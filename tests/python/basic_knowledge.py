import unittest


class BasicKnowledgeTest(unittest.TestCase):

    def test__name__(self):
        """如果是顶级执行上下文,__name__等于__main__"""
        self.assertEqual(__name__, 'tests.python.basic_knowledge')

    def test_built_in_type_func(self):
        a = 42
        self.assertEqual(type(a), int)

    def test_int_could_be_any(self):
        """int可以是任意大的数"""
        number = 10**90
        self.assertEqual(str(number),
                         '1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

    def test_is(self):
        """is 判断的是两个变量是否指向一个对象，==是判断两个对象是否相等，和class的__eq__方法的实现有关"""
        class Word:
            def __init__(self, text):
                self.text = text

            def __eq__(self, other):
                return self.text.lower() == other.text.lower()

        a_ha = Word('ha')
        another_ha = Word('HA')

        self.assertTrue(a_ha == another_ha)
        self.assertFalse(a_ha is another_ha)

    def test_return_value(self):
        """三个方法的返回值都是None，只是方法的语义不同"""
        def method1():
            return None

        def method2():
            pass

        def method3():
            return

        self.assertIsNone(method1())
        self.assertIsNone(method2())
        self.assertIsNone(method3())

    def test_for_in_list(self):
        self.assertEqual([number*number for number in range(1, 6)], [1, 4, 9, 16, 25])

    def test_for_in_list2(self):
        self.assertEqual([number for number in range(1, 6) if number % 2 == 0], [2, 4])

    def test_for_in_list3(self):
        self.assertEqual([(row, col) for row in range(1, 3) for col in range(1, 3)], [(1, 1), (1, 2), (2, 1), (2, 2)])

    def test_if_else(self):
        """空值被判定为False，但是他们并不等于False"""
        def test(v):
            if v:
                return True
            else:
                return False

        self.assertFalse(test(None))
        self.assertFalse(test(0))
        self.assertFalse(test(0.0))
        self.assertFalse(test(False))
        self.assertFalse(test([]))
        self.assertFalse(test({}))
        self.assertFalse(test(set()))

        self.assertFalse(None == False)
        self.assertTrue(0 == False)
        self.assertTrue(0.0 == False)
        self.assertFalse("" == False)
        self.assertFalse([] == False)
        self.assertFalse({} == False)
        self.assertFalse(set() == False)

    def test_generator(self):
        """怎么定义generator的例子"""
        def my_range(first=0, last=10, step=1):
            number = first
            while number < last:
                yield number
                number += step
        self.assertEqual([1, 2, 3, 4, 5], [number for number in my_range(1, 6)])

    def test_decorator(self):
        """其实就相当于是把@后面的函数执行一下,下面的函数会被当做参数传入,然后返回一个新的函数来赋给下面这个函数名.当有多个注解时,靠近函数的先执行"""
        def print_func_name(pre):
            def print_func_name_in(fn):
                def new_func():
                    return pre + '_' +fn.__name__
                return new_func
            return print_func_name_in

        @print_func_name('prefix')
        def test():
            pass

        self.assertEqual('prefix_test', test())
