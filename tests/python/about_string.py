import unittest


class AboutString(unittest.TestCase):

    def test_string_format(self):
        self.assertEqual('{}'.format(42), '42')
        self.assertEqual('{b} {a}'.format(a=1, b=2), '2 1')

    def test_define_string(self):
        txt1 = 'txt1'
        txt2 = "txt2"
        txt3 = '''txt
3'''
        self.assertEqual(txt1, "txt1")
        self.assertEqual(txt2, "txt2")
        self.assertEqual(txt3, "txt\n3")

    def test_slice(self):
        txt = 'this is the first example abot slice in python'

        self.assertEqual(txt[0:4], 'this')
        self.assertEqual(txt[0:4:2], 'ti')