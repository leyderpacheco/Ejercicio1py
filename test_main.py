import unittest
import main



class Test(unittest.TestCase):
    def test_calculo_edad(self):
        self.assertEqual(70,main.calculo_edad(),"No CUmple los requisitos para aprobar el test") #edad esperada 69 años

if __name__=="__main__":
    unittest.main()
