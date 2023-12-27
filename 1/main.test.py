import unittest

class Day1Tests(unittest.TestCase):
    def test_day1(self):
        print('testing')
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()