import unittest
from Examen2 import MiClase


class MyTestCase(unittest.TestCase):
    ###Jose###
    def test_ObtieneValencia1(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.ObtieneValencia(45786312), 5)  # add assertion here

    def test_ObtieneValencia2(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.ObtieneValencia(215496), 3)  # add assertion here

    def test_DivisibleTempo1(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.DivisibleTempo(8), [1, 2, 4, 8])  # add assertion here

    def test_DivisibleTempo2(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.DivisibleTempo(12), [1, 2, 3, 4, 6, 12])  # add assertion here

    ###YERIK###
    def test_ObtieneMasBailable1(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.ObtieneMasBailable([0.8, 0.9, 0.7]), 0.9)  # add assertion here

    def test_ObtieneMasBailable2(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.ObtieneMasBailable([1, 2, 4, 5, 10, 20]), 20)  # add assertion here

    def test_VerificaListaCanciones1(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]), True)

    def test_VerificaListaCanciones2(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.VerificaListaCanciones([1, 2, 4, 5, 10, 20]), True)

    def test_Encuentra(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.Encuentra([1, 2, 3, 4, 5], 4), True)

if __name__ == '__main__':
    unittest.main()
