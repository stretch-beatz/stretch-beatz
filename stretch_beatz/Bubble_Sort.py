from FoxDot import *

'''
Bubble_Sort and original tests written by Dillon Dawson 
https://github.com/Dillon-Dawson/MelodyExtFD
Part of his A Level Computer Science Project
'''

@PatternMethod
def bubble_sort(self, swaps=False, debug = False, palindrome = False): #This defines the section of the code that does the
    ''' Returns the pattern and each stage of the pattern going through a bubble sort
        e.g. `P[50,25,5,20,10].bubble_sort()` will return `P[50,25,5,20,10,25,5,20,10,50,5,20,10,25,50,5,10,20,25,50]`
        and  `P[50,25,5,20,10].bubble_sort(swaps = True)` will add to the output for every number swap returning `P[50,25,5,20,10,25,50,5,20,10,25,5,50,20,10,25,5,20,50,10,25,5,20,10,50,5,25,20,10,50,5,20,25,10,50,5,20,10,25,50,5,10,20,25,50]`
        and  `P[0.5 ,2.0 ,1 ,1.5].bubble_sort(palindrome=True)` will also undo the change to smoothly return to the orignal pattern P[0.5, 2.0, 1, 1.5, 0.5, 1, 1.5, 2.0, 0.5, 1, 1.5, 2.0, 0.5, 2.0, 1, 1.5]
    ''''

    items = self.data
    changes = passes = 0 # This sets the changes and passes to 0 every time this section is ran.
    last = len(items) #lens is a method that returns the length of a list.
    swapped = True
    output = []
    output += items #output = output + items
    outputP = []
    outputP = items + outputP


    while swapped:
        swapped = False
        passes += 1
        for j in range(1, last):
            if items[j - 1] > items[j]:
                items[j], items[j - 1] = items[j - 1], items[j]  # Swap
                if swaps == True:
                    output += items
                changes += 1
                swapped = True
                last = j
        if changes == 0:
            #raise Warning("Data Presorted")
            print("Data Presorted", self.data)
        if swapped == True and swaps == False:
            output += items
            outputP = items + outputP

    if palindrome:
        output += outputP
    if debug == True:
        print(output)
    return self.__class__(output)
