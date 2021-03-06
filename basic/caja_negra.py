import unittest


def suma(num_1,num_2):
    result = num_1 + num_2
    return result

class cajaNegraTest(unittest.TestCase):
    
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5 

        result = suma(num_1,num_2)

        self.assertEqual(result,15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -5 

        result = suma(num_1,num_2)

        self.assertEqual(result,-15)    


if __name__ == '__main__':
    unittest.main()
