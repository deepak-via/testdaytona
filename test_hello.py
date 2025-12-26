import unittest
import math
from hello import hello_world, pentagon_area


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        """Test that hello_world returns the expected message."""
        result = hello_world()
        self.assertEqual(result, 'Hello from E2E Test 1766585237!')


class TestPentagonArea(unittest.TestCase):
    def test_pentagon_area_basic(self):
        """Test pentagon area calculation with side length 1."""
        result = pentagon_area(1)
        expected = (1/4) * math.sqrt(25 + 10 * math.sqrt(5))
        self.assertAlmostEqual(result, expected, places=10)

    def test_pentagon_area_with_side_5(self):
        """Test pentagon area calculation with side length 5."""
        result = pentagon_area(5)
        expected = (1/4) * math.sqrt(25 + 10 * math.sqrt(5)) * 25
        self.assertAlmostEqual(result, expected, places=10)

    def test_pentagon_area_with_side_10(self):
        """Test pentagon area calculation with side length 10."""
        result = pentagon_area(10)
        expected = (1/4) * math.sqrt(25 + 10 * math.sqrt(5)) * 100
        self.assertAlmostEqual(result, expected, places=10)

    def test_pentagon_area_zero(self):
        """Test pentagon area calculation with side length 0."""
        result = pentagon_area(0)
        self.assertEqual(result, 0)

    def test_pentagon_area_negative(self):
        """Test that negative side length raises ValueError."""
        with self.assertRaises(ValueError):
            pentagon_area(-1)


if __name__ == '__main__':
    unittest.main()
