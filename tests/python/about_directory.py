import unittest


class DirectoryTest(unittest.TestCase):

    def test_direct(self):
        dic = {'Leon': 28, 'Ada': 32}
        self.assertEqual(dic['Leon'], 28)
