import unittest
from your_module import calculate_amortization

class TestAmortization(unittest.TestCase):
    def test_amortization_case1(self):
        self.assertAlmostEqual(calculate_amortization(100000, 5, 30), 536.82, places=2)

    def test_amortization_case2(self):
        self.assertAlmostEqual(calculate_amortization(200000, 3.92, 15), 1475.61, places=2)

    def test_amortization_case3(self):
        self.assertAlmostEqual(calculate_amortization(350000, 4.5, 30), 1773.37, places=2)

    def test_amortization_case4(self):
        self.assertAlmostEqual(calculate_amortization(500000, 2.67, 10), 4746.10, places=2)

    def test_amortization_case5(self):
        self.assertAlmostEqual(calculate_amortization(0, 5, 30), 0, places=2)

    def test_amortization_case6(self):
        self.assertAlmostEqual(calculate_amortization(100000, 0, 30), 277.78, places=2)

    def test_amortization_case7(self):
        self.assertRaises(ValueError, calculate_amortization, -100000, 5, 30)

    def test_amortization_case8(self):
        self.assertRaises(ValueError, calculate_amortization, 100000, -5, 30)

    def test_amortization_case9(self):
        self.assertRaises(ValueError, calculate_amortization, 100000, 5, -30)

if __name__ == '__main__':
    unittest.main()