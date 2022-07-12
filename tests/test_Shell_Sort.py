import pytest
from FoxDot import *
from stretch_beatz import *

'''
Shell_Sort and original tests written by Dillon-Dawson 
https://github.com/Dillon-Dawson/MelodyExtFD
Part of his A Level Computer Science Project
'''

class Test_Shell_Sort():
    
    def test__1(self):
        assert P[50,25,5,20,10].shell_sort() == P[50, 25, 5, 20, 10, 5, 25, 10, 20, 50, 5, 20, 10, 25, 50, 5, 10, 20, 25, 50]
    
    def test__2(self):
        assert P[50,25,5,20,10].shell_sort(swaps = True,debug = True) == P[50,25,5,20,10,5,25,50,20,10,5,25,10,20,50,5,20,10,25,50,5,10,20,25,50]
        
    
    def test__3(self):
        assert P[5,5,5,5,5].shell_sort(swaps = True) == P[5,5,5,5,5]
    
    def test__4(self):
        assert P([]).shell_sort(swaps= True) == P([])
    
    def test__5(self):
        assert P([]).shell_sort() == P([])
    
    def test__6(self):
        assert P[50,25,5,20,10].shell_sort(palindrome=True, debug = True) == P[50, 25, 5, 20, 10, 5, 25, 10, 20, 50, 5, 20, 10, 25, 50, 5, 10, 20, 25, 50,5, 10, 20, 25, 50,5, 20, 10, 25, 50,5, 25, 10, 20, 50,50, 25, 5, 20, 10]
   

if __name__ == "__main__":
    main()

    
