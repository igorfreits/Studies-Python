"""aula-112-Unittest#2

1-Receber um numero inteiro
2-Saber se o número é multiplico de 3 e 5
    Bacon com ovos
3 - Saber o numero NÂO é múltiplo de 3 e 5
    Passar fome
4 - Saber se o numero é múltiplo somente de 5
    Ovos
5 - Passar fomeSaber se um numero é múltiplo somente de 3
    Bacon
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
from baconcomovos import bacon_com_ovos


class test_BaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_receber_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'"{entrada}" não retornou "{saida}"'
                                 )

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'"{entrada}" não retornou "{saida}"'
                                 )

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'Bacon'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'"{entrada}" não retornou "{saida}"')

    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_for_multiplo_de_5(self):
        entradas = (5, 10, 20, 25)
        saida = 'Ovos'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'"{entrada}" não retornou "{saida}"'
                                 )


if __name__ == '__main__':
    unittest.main(verbosity=2)
