import unittest
import re
import validate.sample.sample as e

class testsample_fun(unittest.TestCase):
    def test_email(self):
        result = e.filter_mail(('brian-23@hackerrank.com','britts_54@hackerrank.com','lara@hackerrank.com'))
        self.assertEqual(result,['brian-23@hackerrank.com','britts_54@hackerrank.com','lara@hackerrank.com'])


if __name__=='__main__':
    unittest.main()