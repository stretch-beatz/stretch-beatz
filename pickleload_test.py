import json, pickle
import sys
import os.path as ospath
from FoxDot import *

def main(args):
    pickleFile = args.file
    print("Loading "+pickleFile)
    with open(pickleFile,'rb') as j:
        data = pickle.load( j)
        print(data)
        print(len(data["degree"]), "Compasses")
        


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process files into the data format for learning.')
    parser.add_argument('--file', help='file to learn from', default='output/bach.pickle')
    
    args = parser.parse_args()


    print("Scale.minor", Scale.minor)

    #main(args)