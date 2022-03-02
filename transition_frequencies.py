import json, pickle
import sys
import os.path as ospath
from FoxDot import *

try :
    import sortedcontainers
except Exception as e:
    print("sortedcontainers import failed, probably not installed. The code will work but the output will be messy to read")
    print(e)
    pass

def main(args):
    pickleFile = args.file
    print("Loading "+pickleFile)
    with open(pickleFile,'rb') as j:
        data = pickle.load( j)
        #print(data['degree'])
        try:
            transitions= sortedcontainers.SortedDict()
            
        except Exception as e:
            print("sorteddict setup failed")
            print(e)
            transitions={}

        for notes in data['degree']:
            for i in range(len(notes)-1):
                A = notes[i]# % 12
                B = notes[i+1]# % 12
                C = B-A
                if not A in transitions:
                    transitions[A] =  {}
                if not B in transitions[A]:
                    transitions[A][B] = 0
                    #transitions[A][B] = C
                transitions[A][B] += 1
        
        print("transitions", transitions)
        #print("transitions", json.dumps(transitions))
        


                    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process files to analyse how often each note is followed by each other note in a body of work.')
    parser.add_argument('--file', help='file to learn from', default='output/bad_guy.pickle')
    
    args = parser.parse_args()

    main(args)