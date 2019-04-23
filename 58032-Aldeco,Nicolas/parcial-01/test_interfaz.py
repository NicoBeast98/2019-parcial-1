import unittest
from interfaz import check

class ErrorFromInput(unittest.TestCase):
    def test_GOOD_JOB(self):
        ans = check('5')
        self.assertEqual(ans,'5')
    def test_InputVoid(self):
        ans = check(None)
        self.assertEqual(ans,'ERROR -- Ingreso vacio')
    def test_InputLetters(self):
        ans = check('Hola Mabel')
        self.assertEqual(ans,'ERROR -- No puede ingresar palabras')

if __name__ == "__main__":
    unittest.main()