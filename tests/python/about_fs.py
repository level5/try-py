import unittest


class AboutFs(unittest.TestCase):

    def test_read_of_file(self):
        f = open(__file__, 'r')
        
        self.assertTrue(f.read().startswith('import unittest'))
        f.close()

    def test_read_line_of_file(self):
        f = open(__file__, 'r')
        self.assertEqual(f.readline(), 'import unittest\n')
        f.close()