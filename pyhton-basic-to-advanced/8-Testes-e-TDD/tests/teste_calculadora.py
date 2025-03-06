"""Unittest #1
-https://docs.python.org/pt-br/3/library/unittest.html
"""
try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "../src",
            )))
except:
    raise

import unittest
from calculadora import soma

# começar com a palavra "test_ " para identificar o teste
# o nome do teste deve ser o nome da função


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 20, 30),
            (-10, 20, 10),
            (5.25, 5.25, 10.5),
            (100, 100, 200),
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retonar_assertion_error(self):
        with self.assertRaises(AssertionError):
            soma('10', 20)

    def test_soma_y_nao_e_int_ou_float_deve_retonar_assertion_error(self):
        with self.assertRaises(AssertionError):
            soma(10, '20')


if __name__ == '__main__':
    unittest.main(verbosity=2)
