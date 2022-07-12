from FoxDot import *

'''
Recursive_Index written by Finn Brady  
https://github.com/Finn-T-Brady/FDMelExt
Part of his A Level Computer Science Project
'''

@PatternMethod
def recursive_index(self,append=1, Length=None,stall=2,start=0, debug=0):
    if self.data==[]:
        print("Warning: .recursive_index recieved an empty pattern")
        return self.new([])
    if Length==None:
        Length=len(self.data)
    new = []
    new = [RecurStall_0,RecurStall_1,RecurStall_2][stall](self.data,Length,start)
    if debug==1:
        print(new)
    if(append==1):
        new=self.data+new
    return self.new(new)

def RecurStall_0(pattern,i=None,start=0):
    new = []
    curr=pattern[start]
    new+=[curr]
    for x in range(0,i-1):
        curr=pattern[curr%len(pattern)]
        new+=[curr]
    return new
def RecurStall_1(pattern,i=None,start=0):
    new = []
    curr=pattern[start]
    old=-1
    new+=[curr]
    x=0
    for x in range(0,i-1):
        if(curr==old):
            break
        old=curr
        curr=pattern[curr%len(pattern)]
        new+=[curr]
    return new
def RecurStall_2(pattern,i=None,start=0):
    new = []
    curr=pattern[start]
    old=-1
    new+=[curr]
    for x in range(0,i-1):
        if(curr!=old):
            curr=pattern[curr%len(pattern)]
        if(curr==old):
            curr=pattern[(curr+1)%len(pattern)]
        new+=[curr]
        old=curr
    return new
