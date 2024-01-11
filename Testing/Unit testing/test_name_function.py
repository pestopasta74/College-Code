# save this file as test_name_function.py
import unittest
from name_function import formatted_name
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        result = formatted_name("pete", "seeger")
        self.assertEqual(result, "Pete Seeger")
    def test_first_middle_last_name(self):
        result = formatted_name("john", "hooker", "lee")
        self.assertEqual(result, "John Lee Hooker")
    def test_prestons_name(self):
        result = formatted_name("preston", "Whiteman", "Leighton Tony Shaun")
        self.assertEqual(result, "Preston Leighton Tony Shaun Whiteman")

if __name__== '__main__':
    unittest.main()