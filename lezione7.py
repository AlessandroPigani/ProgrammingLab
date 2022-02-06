import unittest
from lezione7estensione import somma

#testing

class TestSomma(unittest.Testcase):
    def test_somma():
        self.assertEqual(somma(1,1),2)
        self.assertEqual(somma(2.5,1.5),4)