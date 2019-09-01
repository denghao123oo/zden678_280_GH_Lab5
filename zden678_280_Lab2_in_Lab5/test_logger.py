from logger import Logger
import unittest


class Target:   
    def get_text(self):
        return self.text
    
    def set_text(self, text):
        self.text = text
        
class LoggerTest(unittest.TestCase):
    def test_info(self):
        t1 = Target() #arrange
        log = Logger(target=t1.set_text) #arrange
        log.info('say something') #act
        self.assertEqual('[INFO] say something',t1.get_text()) #assert
        
    def test_error(self):
        t2 = Target()  #arrange
        log = Logger(target=t2.set_text) #arrange
        log.error('Errors found') #act
        self.assertEqual('[WARNING] ' +'Errors found',t2.get_text()) #assert

if __name__ == '__main__':    
    unittest.main()