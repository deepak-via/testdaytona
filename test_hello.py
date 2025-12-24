import unittest
from hello import hello_world


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        """Test that hello_world returns the expected message."""
        result = hello_world()
        self.assertEqual(result, 'Hello from E2E Test 1766585237!')


if __name__ == '__main__':
    unittest.main()
