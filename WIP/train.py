import json, pickle
import sys
import os.path as ospath
from FoxDot import *
import pykov

def main(args):
    pickleFile = args.file
    print("Loading "+pickleFile)
    with open(pickleFile,'rb') as j:
        data = pickle.load( j)
        #print(data)
        matr = pykov.Matrix()
        T = pykov.Chain()
        transitions= {}

        for notes in data['degree']:
            for i in range(len(notes)-1):
                A = notes[i]# % 12
                B = notes[i+1]# % 12
                if not A in transitions:
                    transitions[A] =  pykov.Vector()
                if not B in transitions[A]:
                    transitions[A][B] = 0
                transitions[A][B] += 1
            
        for k in transitions.keys():
            transitions[k].normalize()
            T[k] = transitions[k]

                #matr[(A,B)] += 1
                #T[(A,B)] += 1
        
        #matr.normalize()

        print (T.steady())



                    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process files into the data format for learning.')
    parser.add_argument('--file', help='file to learn from', default='output/bad_guy.pickle')
    
    args = parser.parse_args()

    main(args)