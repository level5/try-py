import unittest

module_global = 42


class NameSpaceTest(unittest.TestCase):
    """
    当前的namespace是使用python dictionaries来实现的
    例如：1. built-in name的集合
         2. module的global names
         3. 函数调用的local names
    """

    def setUp(self):
        global module_global
        module_global = 42

    def test_writable_attr_could_be_reassign(self):
        self.fail('TBD')

    def test_writable_attr_could_be_del(self):
        """
        writable attr可以被 del删除
        """
        self.fail('TBD')

    def test_scope(self):
        """
        scope
        1. 最里层的scope， 包含了local name
        2. 。。。包围的function的scopes，从最靠近过的scope开始
        3. 倒数第二层scope，包含当前模块的global names
        4. 最外层的scope，包含built-in names
        """
        self.fail('TBD')

    def test_read_global_variable(self):
        """对全局的变量只能只读"""
        self.assertEqual(module_global, 42)

    def test_write_variable_without_global(self):
        """不使用global的话，赋值时生成一个local的变量"""
        def change():
            module_global = 44
        change()
        self.assertEqual(module_global, 42)

    def test_keyword_global(self):
        def change():
            global module_global
            module_global = 44
        change()
        self.assertEqual(module_global, 44)

    def test_keyword_global2(self):
        """global关键字会将变量直接绑定到module的全局变量上，会跳过外层scope的变量"""
        module_global = 42
        def change():
            global module_global
            module_global = 44

        change()
        self.assertEqual(module_global, 42)

    def test_keyword_nonlocal(self):
        """nonlocal关键字可以将变量绑定到当前scope的外层scope的变量上"""
        module_global = 41
        def change():
            nonlocal module_global
            module_global = 44
        change()
        self.assertEqual(module_global, 44)

    def test_class_def(self):
        class MyClass:
            i = 42

            def f(self):
                return 43

        self.assertEqual(MyClass.i, 42)
        self.assertEqual(MyClass.f(None), 43)

    def test_class_instance(self):
        class MyClass:
            i = 42

            def f(self):
                return 43

        x = MyClass()

        self.assertIsNotNone(x.f)

    def test_keyword_super(self):
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        class Employee(Person):
            def __init__(self, name, age, salary):
                super().__init__(name, age)
                self.salary = salary

        code_monkey = Employee('h', 33, 12000)
        self.assertEqual(code_monkey.name, 'h')
        self.assertEqual(code_monkey.salary, 12000)

    def test_property(self):
        class Person:
            def __init__(self, name):
                self.hidden_name = name

            def get_name(self):
                return self.hidden_name

            def set_name(self, name):
                self.hidden_name = name

            name = property(get_name, set_name)

        kain = Person('kain')
        self.assertEqual(kain.name, 'kain')
        kain.name = 'KAIN'
        self.assertEqual(kain.name, 'KAIN')

    def test_property_decorator(self):
        class Person:
            def __init__(self, input_name):
                self.hidden_name = input_name

            # 这个函数的名字就是属性名
            @property
            def name(self):
                return self.hidden_name

            # 这函数的名字也必须是name
            @name.setter
            def name(self, input_name):
                self.hidden_name = input_name

        kain = Person('kain')
        self.assertEqual(kain.name, 'kain')
        kain.name = 'KAIN'
        self.assertEqual(kain.name, 'KAIN')

    def test_keep_name_hidden(self):
        "使用__xxx,可以隐藏属性名，属性名被转移到_Duck__xxx??? 这个测试下来怎么是错误的？"
        class Person:
            def __init__(self, name):
                self.__name = name

        kain = Person('kain')
        try:
            kain.__name
        except AttributeError as err:
            pass
        else:
            self.fail("should throw exception")

    def test_class_method(self):
        class Person:
            count = 0

            def __init__(self, name):
                self.__name = name
                Person.count += 1

            @classmethod
            def total_person(cls):
                return cls.count

        kain = Person('kain')
        leon = Person('leon')

        self.assertEqual(Person.total_person(), 2)

    def test_static_method(self):
        class Util:
            @staticmethod
            def add(a, b):
                return a + b

        self.assertEqual(Util.add(1, 2), 3)

    def test_special_method(self):
        class Word:
            def __init__(self, text):
                self.text = text

            # 特殊方法以__开头和结束
            def __eq__(self, a_word):
                return self.text.lower() == a_word.text.lower()

        first = Word('ha')
        second = Word('HA')
        third = Word('eh')

        self.assertTrue(first == second)
        self.assertFalse(first == third)

    def test_iterator(self):
        class Reverse:

            def __init__(self, data):
                self.data = data
                self.index = len(data)

            # 我觉得这里应该生成一个新的对象比较好一点，这样每次的调用就不会相互干扰
            def __iter__(self):
                return self

            def __next__(self):
                if self.index == 0:
                    raise StopIteration
                self.index -= 1
                return self.data[self.index]

