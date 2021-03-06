def matrix_script(n, m, matrix):
    
    """
    These are regex expressions I use later
    """
    
    regex_char = r"[A-Z, a-z, 0-9]"
    regex_char_end = r"([A-Z, a-z, 0-9]+)*$"
    regex_nonchar = r"([^A-Z, a-z, 0-9]+|\s+)*"
    regex_nonchar_end = r"([^A-Z, a-z, 0-9]+|\s+)*$"
    
    import re
    
    i = 0
    matrix_unwrap = ""
    
    """
    This unravels the matrix input and returns it in a simple string
    """
    
    while i < m:
        for each in matrix:
            matrix_unwrap += each[i]
        i += 1
    i = 0
    
    while i < len(matrix_unwrap):
        
        """
        This is an initial test for cases where the string starts with a non-letter/number
        """
        
        while not matrix_unwrap[i].isalnum() and not re.match(regex_nonchar_end, matrix_unwrap[i:]):
            i += len(re.match(regex_nonchar, matrix_unwrap[i:]).group())
            
        """
        This passes consecutive letters/numbers
        """
        while matrix_unwrap[i].isalnum():
            i += len(re.match(regex_char, matrix_unwrap[i:]).group())
            
        """
        This replaces groups of non-letter/number between letter/numbers with a space character
        """
        
        while not re.match(regex_nonchar_end, matrix_unwrap[i:]):
            matrix_unwrap = matrix_unwrap.replace(re.match(regex_nonchar, matrix_unwrap[i:]).group(), " ", 1)
            break
        
        """
        This checks if the cursor has approached the final group of characters and if so, ends the function
        """
        
        while re.match(regex_nonchar_end, matrix_unwrap[i:]) or re.match(regex_char_end, matrix_unwrap[i:]):
            return (matrix_unwrap)
        i += 1

import unittest

class TestMatrix(unittest.TestCase):
    def test_0(self):
        n = 7
        m = 3
        matrix = ["Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"]
        result = matrix_script(n, m, matrix)
        self.assertEqual(result, "This is Matrix#  %!")

    def test_1(self):
        n = 4
        m = 6
        matrix = ["T%Mic&", "h%axr%", "iit#p!", "ssrst&"]
        result = matrix_script(n, m, matrix)
        self.assertEqual(result, "This isMatrix scrpt&%!&")

    def test_2(self):
        n = 4
        m = 6
        matrix = ["T%$r%r", "h%Mi$i", "iiaxsp", "sst%ct"]
        result = matrix_script(n, m, matrix)
        self.assertEqual(result, "This is Matrix script")
    
    def test_6(self):
        n = 2
        m = 2
        matrix = ["# ", " @"]
        result = matrix_script(n, m, matrix)
        self.assertEqual(result, "#  @")
        
    def test_7(self):
        n = 2
        m = 4
        matrix = ["# i#", " @#U"]
        result = matrix_script(n, m, matrix)
        self.assertEqual(result, "#  @i U")

if __name__ == '__main__':
    unittest.main()
