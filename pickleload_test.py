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

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process files into the data format for learning.')
    parser.add_argument('--file', help='file to learn from', default='output/bad_guy.pickle')
    
    args = parser.parse_args()

    main(args)