import unittest

def is_prime(value):
    if value < 2:
        return False
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_with_1(self):
        result = is_prime(1)
        self.assertFalse(result)  # Cambiado a assertFalse
    
    def test_with_2(self):
        result = is_prime(2)
        self.assertTrue(result)
    
    def test_with_3(self):
        result = is_prime(3)
        self.assertTrue(result)
    
    def test_with_4(self):
        result = is_prime(4)
        self.assertFalse(result)
    
    def test_with_5(self):
        result = is_prime(5)
        self.assertTrue(result)

unittest.main()
