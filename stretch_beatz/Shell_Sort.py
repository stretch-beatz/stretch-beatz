from FoxDot import *
import math

'''
Shell_Sort and original tests written by Dillon Dawson 
https://github.com/Dillon-Dawson/MelodyExtFD
Part of his A Level Computer Science Project
'''

def makehalves(length):
    i = length
    list = []
    while i>2:
        i = math.floor(i/2)
        if(i>1):
            list.append(i)        
    return list



@PatternMethod
def shell_sort(self, swaps=False,debug = False, palindrome = False): #This defines the section of the code that does the
    ''' Returns the pattern and each stage of the pattern going through a shell sort
        e.g. `P[50,25,5,20,10].shell_sort()` will return `P[50, 25, 5, 20, 10, 5, 25, 10, 20, 50, 5, 20, 10, 25, 50, 5, 10, 20, 25, 50]`
        and  `P[50,25,5,20,10].shell_sort(swaps = True)` will add to the output for every number swap returning `P[50,25,5,20,10,5,25,50,20,10,5,25,10,20,50,5,20,10,25,50,5,10,20,25,50]`
        and  `P[50,25,5,20,10].shell_sort(palindrome=True)` will also undo the change to smoothly return to the orignal pattern P[50, 25, 5, 20, 10, 5, 25, 10, 20, 50, 5, 20, 10, 25, 50, 5, 10, 20, 25, 50,5, 10, 20, 25, 50,5, 20, 10, 25, 50,5, 25, 10, 20, 50,50, 25, 5, 20, 10]
    ''''
    items = self.data
    output = []
    output += items #output = output + items
    outputP = []
    outputP = items + outputP


 
    for i in makehalves(len(items)):
        for j in range(i):
            sortoutput, sortoutputP = inssort2(items, j, i)
            #print("after inssort2(items, "+str(j)+", "+str(i)+")", items)
            if swaps == False:
                output += items
                outputP = items + outputP
            if swaps == True:
                output += sortoutput
                outputP = sortoutputP + outputP
    sortoutput, sortoutputP = inssort2(items, 0, 1)
    #print("After pass at 1", items)
    if swaps == False:
        output += items
        outputP = items + outputP
    if swaps == True:
        output += sortoutput
        outputP = sortoutputP + outputP

    if palindrome:
        output += outputP
        
    if debug == True:
        print("Output",output)
        
    return self.__class__(output)


def inssort2(items, start, incr):
    output = []
    outputP = []

    
    for  i in range(start+incr, len(items), incr):
        j=i
        while (j>=incr) and (items[j] < items[j-incr]):
            items[j], items[j-incr] = items[j-incr], items[j]
            #print("Swapping", items)
            output += items
            outputP = items + outputP
            j-=incr

    return(output,outputP)

#assert shellsort([50,25,5,20,10]) == [ 5, 10, 20, 25, 50]

def printlist(list1, chunk_size = 5, ):
    chunked_list = [list1[i:i+chunk_size] for i in range(0, len(list1), chunk_size)]
    for j  in range(len(chunked_list)):
        chunk = chunked_list[j]
        print( str(chunk))
 

def printlist2(list1, chunk_size = 5, list2 = [] ):
    chunked_list = [list1[i:i+chunk_size] for i in range(0, len(list1), chunk_size)]
    chunked_list2 = [list2[i:i+chunk_size] for i in range(0, len(list2), chunk_size)]
    for j  in range(len(chunked_list)):
        chunk = chunked_list[j]
        chunk2 = chunked_list2[j]
        if (chunk != chunk2):
            print("Not Equal")
        print( str(chunk) +"\t"+str(chunk2))
 
