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
        soup = BeautifulSoup('<b>b1</b><b>b1</b>', "html5lib")
        tag = soup.b
        self.assertEqual(type(tag), bs4.element.Tag)

        # 每使用一次.<tag-name>,就会一个tag，下次在调用的时候，会获取下一个tag
        self.assertEqual(str(tag), '<b>b1</b>')
        self.assertEqual(str(soup.b), '<b>b2</b>')

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
