import unittest


class AboutString(unittest.TestCase):

    def test_string_format(self):
        self.assertEqual('{}'.format(42), '42')
        self.assertEqual('{b} {a}'.format(a=1, b=2), '2 1')