import unittest
import bs4
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


class BeautifulSoupTest(unittest.TestCase):
    """
    运行case需要安装的两个包：
    pip3 install beautifulsoup4
    pip3 install html5lib==1.0b8
    """
    def test_example(self):
        soup = BeautifulSoup(html_doc, "html5lib")

        self.assertEqual(soup.title.name, "title")
        self.assertEqual(soup.title.get_text(), "The Dormouse's story")

    def test_tag(self):
        soup = BeautifulSoup('<b>b2</b><b>b1</b>', "html5lib")
        tag = soup.b
        self.assertEqual(type(tag), bs4.element.Tag)

        # 每使用一次.<tag-name>,就会一个tag，下次在调用的时候，会获取下一个tag
        # ???? 这个为什么昨天运行不是这样的结果！！！！
        # 看起来是取得第一个满足条件的tag
        self.assertEqual('<b>b2</b>', str(tag))
        self.assertEqual('<b>b2</b>', str(soup.b))
        # self.assertEqual('<b>b2</b>', str(soup.b))

        # 整个BeautifulSoup对象可以当做一个Tag来使用

    def test_tag_name(self):
        soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "html5lib")
        tag = soup.b
        # tag的名字可以通过name属性获得
        self.assertEqual(tag.name, 'b')

        # 改变tag的名字，对应的文档也会发生变化
        tag.name = 'h1'
        self.assertEqual(str(soup),
                         '<html><head></head><body><h1 class="boldest">Extremely bold</h1></body></html>')

    def test_tag_attribute(self):
        soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "html5lib")
        tag = soup.b

        # 属性
        self.assertEqual(tag['class'], ['boldest'])
        self.assertEqual(tag.attrs, {'class': ['boldest']})

        # 同样可以通过赋值的方式来修改属性
        pass

    def test_tag_string(self):
        soup = BeautifulSoup('<b>b2</b>', "html5lib")
        tag = soup.b
        self.assertEqual(type(tag.string), bs4.element.NavigableString)
        # 可以通过unicode方法直接将tag.string转换成unicode string
        # python3中unicode() 在哪里？
        # unicode(tag.string)

        # 同样可以通过赋值的方式来修改属性

        # 如果想在Beautiful Soup之外使用 NavigableString 对象,
        # 需要调用 unicode() 方法,将该对象转换成普通的Unicode字符串,
        # 否则就算Beautiful Soup已方法已经执行结束,
        # 该对象的输出也会带有对象的引用地址.这样会浪费内存.