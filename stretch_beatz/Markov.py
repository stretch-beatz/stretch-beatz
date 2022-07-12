from FoxDot import *
#Libraries to randomly seed Markov Chain class
from random import Random
from time import time_ns as timeStamp

'''
Markov written by Finn Brady  
https://github.com/Finn-T-Brady/FDMelExt
Part of his A Level Computer Science Project
'''

class MrkvChain:
    #Nodes are formated as {nodeValue:[links, numbers are repeated to add weight]} e.g.{4:[1,3,3,5,2]}
    Nodes = {}

    #The crrent node selected by the chain
    currVal = None

    #Preparing the Random Class
    rng = Random(None)

    #weights for value n infront, formatted [n, weight]
    dWeights = [[1,4],[2,2],[3,1],[-1,1]]

    #the Next() Method returns the current value and selects the next value for the chain
    def Next(self):
        val=self.currVal
        links=self.Nodes[val]
        self.currVal=links[self.rng.randint(0,len(links)-1)]
        return val

    #the ArrayDecomp() method takes an array, loops through it, and for each note calculates the probalities for the next possible nots
    def ArrayDecomp(self,Arr):
        t=len(Arr)
        #initialising dict
        for x in Arr:
            self.Nodes[x]=[]
        #adding notes to arrays
        for x in range(0,t):
            for n in self.dWeights:
                self.Nodes[Arr[x]]+=n[1]*[Arr[(x+n[0])%t]]

    #the Initialisation function which is calles
    def __init__(self,Arr=None,Seed=None,Weights=None):
        #if a seed is not given
        if Seed==None:
            #checks the timestamp and modulos if by 0xFFFFFFFF (2^24-1)
            tempSeed=timeStamp()%0xFFFFFFFF
            #Printing seed in hex so it can be reused if it sounded good, it is in hex to make it more readable
            print("MrkvChain seed:"+hex(tempSeed))
            #initialising the random class
            self.rng.seed(tempSeed)

        #initialises the random class if a seed is provided
        if Seed!=None:
            self.rng.seed(Seed)
        #replaces the default dWeights values
        if Weights!=None:
            self.dWeights=Weights
        #if an array is provided it will decompose it to the probabilities
        if Arr!=None:
            self.ArrayDecomp(Arr)
            self.currVal=Arr[0]


#functions to be inserted into FoxDot as a Pattern Method
#via the @PatternMethod function decorator

#This is the function to decompose a FoxDot Pattern into a Markov Chain and them recompose a pattern
@PatternMethod
def markov(self,Length=None,append=1,Seed=None, Weights=None,debug=0):
    #check for empty pattern
    if(self.data==[]):
        print("Warning: .Markov recieved an empty pattern")
        return self.new([])
    #initialises markov chain with given pattern, seed, and weights
    Mrkv=MrkvChain(self.data,Seed,Weights)
    new=[]
    #if no lenght is given, takes length of given data
    if Length==None:
        Length=len(self.data)
    #gets new value from markov chain class for specified length
    for x in range(0,Length):
        new+=[Mrkv.Next()]
    del Mrkv
    #debug argument at request of client
    if debug==1:
        print(new)
    #if the append argument is set to 1 it appends the generate pattern to the end of the original one
    if append==1:
        new=self.data+new
    return self.new(new)
