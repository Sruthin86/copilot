import unittest
# import the function to be tested
from demo import area_of_triangle

# Create a test class to test the area of a triangle function
class TestAreaOfTriangle(unittest.TestCase):
    def test_area_of_triangle(self):
        # import the function to be tested
        from demo import area_of_triangle
        # test the function
        self.assertEqual(area_of_triangle(10, 5), 25)
        self.assertEqual(area_of_triangle(3, 4), 6)
        self.assertEqual(area_of_triangle(5, 5), 12.5)
    
    # Create a function to test the not equal assertion method of unittest
    def test_not_equal(self):
        # import the function to be tested
        from demo import area_of_triangle
        # test the function
        self.assertNotEqual(area_of_triangle(10, 5), 20)
        self.assertNotEqual(area_of_triangle(3, 4), 7)
        self.assertNotEqual(area_of_triangle(5, 5), 10)

# Create a test class to test the  better count larger numbers function
class TestBetterCountLargerNumbers(unittest.TestCase):
    def test_better_count_larger_numbers(self):
        # import the function to be tested
        from demo import better_count_larger_numbers
        # test the function
        self.assertEqual(better_count_larger_numbers([1, 2, 3, 4, 5]), 4)
        self.assertEqual(better_count_larger_numbers([1, 2, 3, 4, 5, 6, 7]), 6)
        self.assertEqual(better_count_larger_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), 8)
        self.assertEqual(better_count_larger_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 9)
        self.assertEqual(better_count_larger_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 10)
        
