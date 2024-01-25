import pytest


def test_triangle(triangle):
    assert triangle == 2.205

# Create a function to test the area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height

# Create a fixture to test the area of a triangle
@pytest.fixture
def triangle():
    return area_triangle(2.1, 2.1)

# Create a test class to test the area of the triange
class TestTriangle:
    def test_area_triangle(self):
        assert area_triangle(2.1, 2.1) == 2.205
        assert area_triangle(0, 0) == 0
        assert area_triangle(3, 4) == 6
    
    
    # Create a test using assert not equal
    def test_area_triangle_not_equal(self):
        assert area_triangle(2.1, 2.1) != 2.206
        assert area_triangle(0, 0) != 1
        assert area_triangle(3, 4) != 6.1

    



