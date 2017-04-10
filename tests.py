#source_github_Wojtasny
import unittest
import kol1 as k

class TestStringMethods(unittest.TestCase):

    def test_get_correction(self):
#	self.assertEqual(k.get_new_angle(1), 2)
	self.assertEqual(k.get_correction(-1), 1)
	self.assertEqual(k.get_correction(10), -10)
	self.assertEqual(k.get_correction(1), -1)

    def test_get_new_angle(self):
	self.assertTrue(k.get_new_angle(1))
	self.assertTrue(k.get_new_angle(1))
	self.assertTrue(k.get_new_angle(1))
"""
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
"""

if __name__ == '__main__':
    unittest.main()

