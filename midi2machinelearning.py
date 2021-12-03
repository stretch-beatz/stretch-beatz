from copy import Error
from enum import unique
from inspect import trace
from os import linesep
from music21 import converter, duration, instrument, note, chord, corpus, analysis, pitch, scale
import json, pickle
import sys, numbers
import os.path as ospath
#from os.path import splitext, basename
#from os import *
from FoxDot import *
from music21.environment import envSingleton
WINDOW_SIZE = 4

def extractDuration(element):
    return element.duration.quarterLength

def getFoxDotFromPitch(ps, pitchesToFoxDot):
    if(ps == -1):
        return 0
    try :
        return int(pitchesToFoxDot[ps])
    except KeyError:
        print("KeyError ps", ps )
        return getFoxDotFromPitch(ps - 1, pitchesToFoxDot)

def get_notes(notes_to_parse, pitchesToFoxDot):
    """ Get all the notes and chords from the midi files in the ./midi_songs directory """
    durations = []
    notes = []
    
    for element in notes_to_parse:
        if element.isRest:
            restinst = rest(extractDuration(element))
            notes.append(restinst)
            durations.append(restinst)
        elif isinstance(element, note.Note):
            notes.append(getFoxDotFromPitch(element.pitch.ps,pitchesToFoxDot))
            durations.append(extractDuration(element))
        elif isinstance(element, chord.Chord):
            durations.append(extractDuration(element))
            notes.append(tuple([getFoxDotFromPitch(n.pitch.ps,pitchesToFoxDot) for n in element.notes]))
        else:
            print("No action for element", element)

    #print("notes", notes)
    fd_notes = get_degrees_training_data(notes)
    fd_durations = get_durations_training_data(durations)
                
    return notes, durations, fd_notes, fd_durations

def main(args):
    filename = ""
    ext = ""

    output_data = {
        "degree":[],
        "dur":[],
        "dur_json":[]
    }

    #print("args", args)   
    if (args.midi != None):
        try:
            mid = converter.parse(args.midi)
            filename, ext = ospath.splitext(ospath.basename(args.midi))
            degrees, durations = process_midi(mid, filename, args.chords)
        except Exception as e:
            print("Can't parse "+str(args.midi))
            trace(e)
        
    elif (args.composer != None):
        #http://web.mit.edu/music21/doc/about/referenceCorpus.html
        composer = corpus.getComposer(args.composer)
        degrees = []#loadTraining(composer, "degrees")
        
        if (len(degrees) == 0 ):
            durations = []#loadTraining(composer, "durations")
            
            for filecorp in composer: 
                try:
                    mid = corpus.parse(filecorp)
                except Exception as e:
                    print("Can't parse "+str(filecorp))
                    trace(e)
                    continue    #
                
                basenamefile = ospath.basename(filecorp)
                #print("basenamefile",basenamefile)
                filename, ext = ospath.splitext(basenamefile)

                if(args.force == False ):
                    newdegrees = loadTraining(filename, "degrees")
                    newdurations = loadTraining(filename, "durations")
                
                if(args.force == True or len(newdegrees) == 0):
                    newdegrees, newdurations = process_midi(mid, filename, args.chords)
                
                degrees.extend(newdegrees)
                durations.extend(newdurations)
                        
            saveTraining(degrees, args.composer, "degrees")
            saveTraining(durations, args.composer, "durations")

    elif (args.corpus != None):
        #http://web.mit.edu/music21/doc/about/referenceCorpus.html
        try:
            mid = corpus.parse(args.corpus)
            basenamefile = ospath.basename(args.corpus)
            
            #print("basenamef",basenamef)
            filename, ext = ospath.splitext(basenamefile)
            process_midi(mid, filename, args.chords)
        except Exception as e:
            print("Can't parse "+str(args.corpus))
            trace(e)
        

        
def get_unique_numbers(number_list):
    unique = []

    for num in number_list:
        if num in unique:
            continue
        else:
            unique.append(num)
    return unique

def get_degrees_training_data(degree_inputs):
    degrees = list(filter(lambda x: isinstance(x, numbers.Number) , degree_inputs))
    training = []
    for i in range(0, max(0,len(degrees)-( WINDOW_SIZE + 1))):
        training.append(degrees[i:(i+WINDOW_SIZE+1)])
    #print("training", training)
    return training

def loadTraining( modelname, modeltype):
    import csv
    training = []
    csvFilePath = ospath.join("output", modelname + "_" + modeltype + ".csv")
    print("Loading", csvFilePath)
    if(ospath.isfile(csvFilePath)):
        with open(csvFilePath, 'r', newline= "\n") as csvfile:
            spamreader= csv.reader(csvfile, quoting = csv.QUOTE_NONNUMERIC)
            for count, row in enumerate(spamreader):
                if len(row) and (count > 0):
                    training.append(row)

    return training

def saveTraining(training, modelname, modeltype):
    import csv
    if (len(training) == 0):
        return False
    print("modelname", modelname , "modeltype", modeltype)
    csvFilePath = ospath.join("output", (modelname + "_" + modeltype + ".csv"))
    print("Saving", csvFilePath)
    #print("training[0]", training[0])
    with open(csvFilePath, 'w', newline= "\n") as csvfile:
        spamwriter = csv.writer(csvfile, quoting = csv.QUOTE_NONNUMERIC)        
        data_len = len(training[0]) - 1
        header = ['i'+str(i+1) for i in range(data_len)]
        header.append("target")
        #print("header", header)
        spamwriter.writerow(header)
        for arr in training:
            if(not all([i==arr[0] for i in arr])):
                spamwriter.writerow(arr)

def get_fd_dur_data(dur):
    if isinstance(dur, rest):
        return float(-1 * rest.dur)
    else:
        return float(dur)

def get_durations_training_data(durations_inputs):
    durations = list(map(get_fd_dur_data , durations_inputs))
    training = []
    for i in range(0, max(0,len(durations)-( WINDOW_SIZE + 1))):
        training.append(durations[i:(i+WINDOW_SIZE+1)])
    print("durations training", durations)
    
    return training

def process_midi(mid, filename, chords=False):
    allinstruments=[]
    instruments = instrument.partitionByInstrument(mid)
    if (instruments == None or len(instruments) == 0):
        instruments = [mid]

    for instr in instruments:
        #newinstrs = instrument.unbundleInstruments(instr)
        minoctave = None
        maxoctave = None
        
        #print(instr.parts.keys())
        
        try :
            minoctave = min(instr[note.Note]).octave
            maxoctave = max(instr[note.Note]).octave
        except Exception:
            pass
            #print("No minOctave")
        
        analyzedKey = None
        try :
            analyzedKey = instr.analyze('key')
            
        except Exception:
            pass
            #print("No analyzedKey")

        if (minoctave and analyzedKey):
            #analyzedKey.mode
            #analyzedKey.tonic
            uniquepitches = get_unique_numbers([n.pitch for n in instr[note.Note]])
            lowest = min(uniquepitches)
            highest = max(uniquepitches)
            uniquecount = len(uniquepitches)
            sc = None
            rootPitch =  pitch.Pitch(analyzedKey.tonic, octave=minoctave)
            if (analyzedKey.mode == "major"):
                sc = scale.MajorScale(rootPitch)
            elif (analyzedKey.mode == "minor"):
                sc = scale.MinorScale(rootPitch)
            elif (analyzedKey.mode == "chromatic"):
                sc = scale.ChromaticScale(rootPitch)

            if(uniquecount >= 8 and sc != None):
                scalepitches = sc.getPitches(lowest, highest)
                
                try:
                    rootPos = scalepitches.index(rootPitch)
                    pitchesToFoxDot = {scalepitches[i].ps:(i-rootPos) for i in range(len(scalepitches))}

                    notes, durations, fd_notes, fd_durations = get_notes(instr[note.Note], pitchesToFoxDot)
                    allinstruments.append( {
                        "part":instr, 
                        "root":rootPitch.name,
                        "octave":minoctave, 
                        "scale":analyzedKey.mode, 
                        "pitchesToFoxDot":pitchesToFoxDot, 
                        "degree":fd_notes, 
                        "dur":fd_durations 
                    })

                except ValueError:
                    print("rootPitch", rootPitch, "not in scalepitches", scalepitches)


    degrees = []
    durations = []
    
    for instr in allinstruments: 
        #print(instr['part'].partName,":\t", instr["root"], "octave", instr["octave"],  instr["scale"])
        degrees.extend(instr['degree'])
        durations.extend(instr['dur'])

    saveTraining(degrees, filename, "degrees")
    saveTraining(durations, filename, "durations")

    return degrees, durations

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process files into the data format for learning.')
    parser.add_argument('--midi', help='file to convert')
    parser.add_argument('--corpus', help='file from corpus \nhttp://web.mit.edu/music21/doc/about/referenceCorpus.html', default='bach/bwv108.6.xml')
    parser.add_argument('--composer', help='Music21 Composer info to learn from')
    parser.add_argument('--chords', action='store_true', help='keep chords')
    parser.add_argument('--force', action='store_true', help='Force')

    args = parser.parse_args()

    main(args)