import unittest
from Examen2 import MiClase


class MyTestCase(unittest.TestCase):
    ###Jose###
    def test_ObtieneValencia1(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.ObtieneValencia(45786312), 4)  # add assertion here

    def test_ObtieneValencia2(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.ObtieneValencia(215496), 3)  # add assertion here

    def test_DivisibleTempo1(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.DivisibleTempo(8), [1, 2, 4, 8])  # add assertion here

    def test_DivisibleTempo2(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.DivisibleTempo(12), [1, 2, 3, 4, 6, 12])  # add assertion here


if __name__ == '__main__':
    unittest.main()
