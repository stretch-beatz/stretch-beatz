from FoxDot import *

'''
Cocktail_Sort written by Finn Brady  
https://github.com/Finn-T-Brady/FDMelExt
Part of his A Level Computer Science Project
'''

@PatternMethod
def cocktail_sort(self,append=1,Length=None,step=0, Backwards=0,debug=False):
    #check for empty pattern
    if self.data==[]:
        print("Warning: .cocktail_sort recieved an empty pattern")
        return self.new([])
    #if no length given it takes the square of 
    if(Length==None):
        Length=len(self.data)
        if(step==1):
            Length=Length*Length
    new=[]
    if(append==1):
        new=self.data
    #selecting from an array of functions instead of using if statements
    new+=[CTailFwdStp,CTailFwdPass,CTailBkwdStp,CTailBkwdPass][2*Backwards+step](self.data,Length)
    if(debug):
        print(new)
    return self.new(new)

#The function for cocktail_sort in step mode moving forwards first
def CTailFwdStp(data,i):
    new=[]
    swapped = True
    start=0
    end = len(data)-1
    while (swapped and i>=0):
        for i in range(start, end):
            if(data[i]>data[i+1]):
                data[i], data[i+1] = data[i+1],data[i]
                swapped = True
            new+=data
        if(swapped == False):
            break
        end = end - 1
        for i in range(end-1,start-1,-1):
            if(data[i] > data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
            new+=data
        start = start +1
        i-=1
    return new
#The function for cocktail_sort in pass mode moving forwards first
def CTailFwdPass(data,i):
    new=[]
    swapped = True
    start=0
    end = len(data)-1
    
    while (swapped and i>=0):
        for i in range(start, end):
            if(data[i]>data[i+1]):
                data[i], data[i+1] = data[i+1],data[i]
                swapped = True
        if(swapped == False):
            break
        end = end - 1
        for i in range(end-1,start-1,-1):
            if(data[i] > data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
        start = start +1
        new+=data
        i-=1
    return new
#The function for cocktail_sort in step mode moving backwards first
def CTailBkwdStp(data,i):
    new=[]
    swapped = True
    start=0
    end = len(data)-1
    
    while (swapped and i>=0):
        for i in range(end-1,start-1,-1):
            if(data[i] > data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
            new+=data
        if(swapped == False):
            break
        start = start +1
        for i in range(start, end):
            if(data[i]>data[i+1]):
                data[i], data[i+1] = data[i+1],data[i]
                swapped = True
            new+=data
        end = end - 1
        i-=1
    return new
#The function for cocktail_sort in pass mode moving backwards first
def CTailBkwdPass(data,i):
    new=[]
    swapped = True
    start=0
    end = len(data)-1
    
    while (swapped and i>=0):
        for i in range(end-1,start-1,-1):
            if(data[i] > data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
        if(swapped == False):
            break
        start = start +1
        for i in range(start, end):
            if(data[i]>data[i+1]):
                data[i], data[i+1] = data[i+1],data[i]
                swapped = True
        end = end - 1
        new+=data
        i-=1
    return new

