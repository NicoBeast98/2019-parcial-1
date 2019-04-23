import unittest
from dec_to_hex import decimal_to_hexa

class TestDecToHex(unittest.TestCase):
    def test_5_to_hex_5(self):
        hexa_num = decimal_to_hexa(5)
        self.assertEqual(hexa_num,'5')
    def test_10_to_hex_A(self):
        hexa_num = decimal_to_hexa(10)
        self.assertEqual(hexa_num,'A')
    def test_17_to_hex_11(self):
        hexa_num = decimal_to_hexa(17)
        self.assertEqual(hexa_num,'11')
    def test_16_to_hex_10(self):
        hexa_num = decimal_to_hexa(16)
        self.assertEqual(hexa_num,'10')
    def test_4095_to_hex_FFF(self):
        hexa_num = decimal_to_hexa(4095)
        self.assertEqual(hexa_num,'FFF')
    def test_1234_to_hex_4D2(self):
        hexa_num = decimal_to_hexa(1234)
        self.assertEqual(hexa_num,'4D2')
    def test_234_to_hex_EA(self):
        hexa_num = decimal_to_hexa(234)
        self.assertEqual(hexa_num,'EA')
    def test_921_to_hex_(self):
        hexa_num = decimal_to_hexa(921)
        self.assertEqual(hexa_num,'399')


if __name__ == "__main__":
    unittest.main()