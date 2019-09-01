import unittest     
# Import the Python unit testing framework
import maths        
# Our code to test
class MathsTest(unittest.TestCase):    
    ''' Unit tests for our maths functions. '''    
    def test_add(self):
        sum = maths.add(1,2) #Arrange and Act
        self.assertEqual(sum, '3') #assert
        
        '''additional test'''
        r1 = maths.add(11,11) #Arrange and Act
        self.assertEqual(r1,'22') #assert
        
        r2 = maths.add(11,11,16) #Arrange and Act
        self.assertEqual(r2,'16') #assert
        
        r3 = maths.add(11,11,5) #Arrange and Act
        self.assertEqual(r3,'42') #assert
        
        r4 = maths.add(60,22,10) #Arrange and Act
        self.assertEqual(r4,'82') #assert
        
        r5 = maths.add(23,44,4.5) #Arrange and Act
        self.assertEqual(r5,'Failed') #assert
        
        
    # TODO    
    def test_fibonacci(self):        
        ''' Tests the fibonacci function. '''        
        fib = maths.fibonacci(5) #Arrange and Act
        self.assertEqual(fib, 5) #assert
    # TODO
    # This allows running the unit tests from the command line (python test_maths.py)
    
    def test_convert_base(self):
        result1 = maths.convert_base(11,16) #Arrange and Act
        result2 = maths.convert_base(11,2) #Arrange and Act
        self.assertEqual(result1,'B') #assert
        self.assertEqual(result2,'1011') #assert
    
    def test_factorial(self):
        fac = maths.factorial(2)
        self.assertEqual(fac,None)
        
if __name__ == '__main__':    
    unittest.main()