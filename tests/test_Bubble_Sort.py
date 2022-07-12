import pytest
from FoxDot import *
from stretch_beatz import *

'''
Bubble_Sort and original tests written by Dillon-Dawson 
https://github.com/Dillon-Dawson/MelodyExtFD
Part of his A Level Computer Science Project
'''

class Test_Bubble_Sort():
    
    def test__1(self):
        assert P[50,25,5,20,10].bubble_sort() == P[50,25,5,20,10,25,5,20,10,50,5,20,10,25,50,5,10,20,25,50]," Test 1 Fail "
    
    def test__2(self):
        assert P[50,25,5,20,10].bubble_sort(swaps = True) == P[50,25,5,20,10,25,50,5,20,10,25,5,50,20,10,25,5,20,50,10,25,5,20,10,50,5,25,20,10,50,5,20,25,10,50,5,20,10,25,50,5,10,20,25,50],"Test 2 Fail"
    
    def test__3(self):
        assert P[5,5,5,5,5].bubble_sort(swaps = True) == P[5,5,5,5,5],"Test 3 Fail"
    
    def test__4(self):
        assert P([]).bubble_sort(swaps= True) == P([]),"Test 4 Fail"
    
    def test__5(self):
        assert P([]).bubble_sort() == P([]),"Test 5 Fail" 
    
    def test__6(self):
        assert P[0.5 ,2.0 ,1 ,1.5].bubble_sort(palindrome=True) == P[0.5, 2.0, 1, 1.5, 0.5, 1, 1.5, 2.0, 0.5, 1, 1.5, 2.0, 0.5, 2.0, 1, 1.5], "Test 6 Fail"


    
