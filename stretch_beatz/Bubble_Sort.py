from FoxDot import *

'''
Bubble_Sort and original tests written by Dillon Dawson 
https://github.com/Dillon-Dawson/MelodyExtFD
Part of his A Level Computer Science Project
'''

@PatternMethod
def bubble_sort(self, swaps=False, debug = False, palindrome = False): #This defines the section of the code that does the
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
