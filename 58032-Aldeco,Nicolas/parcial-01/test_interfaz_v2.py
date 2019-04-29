import unittest
from interfaz_v2 import dec_hex_ch,hex_dec_ch

class TestDecimalToHexaMenu(unittest.TestCase):
    def test_inputVoid(self):
        res = dec_hex_ch(None)
        self.assertEqual(res,'ERROR - No ingreso nada')

    def test_inputLetterOrNumbers(self):
        res = dec_hex_ch('Hola Jorge')
        self.assertEqual(res,'ERROR - Debe ingresar solo numeros')

    def test_inputGoodJob(self):
        res = dec_hex_ch('5')
        dec = '5'
        resp = '5'
        self.assertEqual(res,f'El numero {dec} es {resp} en hexadecimal.')

    def test_inputGoodJob(self):
        res = dec_hex_ch('26')
        dec = '26'
        resp = '1A'
        self.assertEqual(res,f'El numero {dec} es {resp} en hexadecimal.')

class TestHexadecimalToDecimal(unittest.TestCase):
    def test_inputVoid(self):
        res = hex_dec_ch(None)
        self.assertEqual(res,'ERROR - No ingreso nada')
    
    def test_inputLetterOfNumbers(self):
        res = hex_dec_ch('4 F 2')
        self.assertEqual(res,'ERROR - No puede ingresar espacios')

    def test_inputCualquierCosa(self):
        res = hex_dec_ch('perro')
        self.assertEqual(res,'ERROR - El numero que ingreso no tiene las letras correctas')

    def test_inputCualquierCosa2(self):
        res = hex_dec_ch('ATR')
        self.assertEqual(res,'ERROR - El numero que ingreso no tiene las letras correctas')

    def test_inputGoodJob(self):
        res = hex_dec_ch('5')
        hexa = '5'
        resp = '5'
        self.assertEqual(res,f'El numero {hexa} es {resp} en decimal')

    def test_inputGoodJob2(self):
        res = hex_dec_ch('4F')
        hexa = '4F'
        resp = '79'
        self.assertEqual(res,f'El numero {hexa} es {resp} en decimal')

    def test_inputGoodJob3(self):
        res = hex_dec_ch('A2')
        hexa = 'A2'
        resp = '162'
        self.assertEqual(res,f'El numero {hexa} es {resp} en decimal')

if __name__ == "__main__":
    unittest.main()