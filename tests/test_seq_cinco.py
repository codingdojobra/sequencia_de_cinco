from unittest import TestCase, main
from src.seq_cinco import calcula_maior_produto

"""
2 1 1 1 1
1 2 1 1 1
1 1 2 1 1
1 1 1 2 1
1 1 1 1 2
"""


class TestSeqCinco(TestCase):
    def test_framework(self):
        self.assertTrue(True)

    def test_matriz1(self):
        matriz = [[2, 1, 1, 1, 1],
                  [1, 2, 1, 1, 1],
                  [1, 1, 2, 1, 1],
                  [1, 1, 1, 2, 1],
                  [1, 1, 1, 1, 2]]

        esperado = 32
        self.assertEqual(esperado, calcula_maior_produto(matriz))

    def test_matriz2(self):
        matriz = [[3, 1, 1, 1, 1],
                  [1, 3, 1, 1, 1],
                  [1, 1, 3, 1, 1],
                  [1, 1, 1, 3, 1],
                  [1, 1, 1, 1, 3]]

        esperado = 243
        self.assertEqual(esperado, calcula_maior_produto(matriz))


if __name__ == '__main__':
    main()
