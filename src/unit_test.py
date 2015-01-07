import random
import sys
import unittest

class TestSequenceFunctions(unittest.TestCase):
    #Class init method
    @classmethod
    def setUpClass(cls):
        print 'In setUpClass'
        
    #Class cleanup method
    @classmethod
    def tearDownClass(cls):
        print 'in tearDownClass'
    
    #Test init method 
    def setUp(self):
        print 'In setUp'
        self.seq = range(10)
        
    #Test cleanup method 
    def tearDown(self):
        print 'In tearDown'
        self.seq = None

    #Test method, need start with "test_*"
    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    #Test method
    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    #Test method, will skip this test
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    #Test method, will only run on windows platform
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        print 'In skip unless test method'
        pass
    
    #Test method, expect an exception is thrown
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
    
    #Test method, passed if KeyError exception is threw
    def test_assertRaised(self):
        with self.assertRaises(KeyError):
            raise KeyError
    
if __name__ == '__main__':
    unittest.main()