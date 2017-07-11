import unittest
import re


class RegexTest(unittest.TestCase):

    def test_match(self):
        p = re.compile('[a-z]+')

        # 是否匹配string的开始位置
        m = p.match('abc123')
        # .group 返回匹配的string
        self.assertEqual('abc', m.group())
        # .start 返回匹配开始的index，因为match是从字符串开始的位置匹配，所以.start总是返回0
        self.assertEqual(0, m.start())
        # .end 返回匹配结束的位置
        self.assertEqual(3, m.end())
        # .span 返回一个元组(start, end)
        self.assertEqual((0, 3), m.span())

        m2 = p.match('123abc')
        # 不匹配的时候返回的是None
        self.assertIsNone(m2)

    def test_search(self):
        p = re.compile("[a-z]+")

        m = p.search('123abc')

        self.assertIsNotNone(m)

        self.assertEqual('abc', m.group())
        self.assertEqual(3, m.start())
        self.assertEqual(6, m.end())
        self.assertEqual((3, 6), m.span())

    def test_findall(self):
        p = re.compile("[a-z]+")
        match_strings = p.findall("123abc123abc")
        self.assertEqual(['abc', 'abc'], match_strings)

    def test_finditer(self):
        p = re.compile("[a-z]+")
        matches = p.finditer('123abc123abc')
        self.assertEqual([(3, 6), (9, 12)], [m.span() for m in matches])

    def test_r_string(self):
        """使用r开头的string，可以不需要对\做转移"""
        p = re.compile(r"\d+")
        p2 = re.compile("\\d+")
        self.assertEqual(p, p2)

    print(2**32 / 1024 / 1024/1024)