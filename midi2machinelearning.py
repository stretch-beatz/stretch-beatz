from copy import Error
from enum import unique
from music21 import converter, instrument, note, chord, corpus, analysis, pitch, scale
import json, pickle
import sys
import os.path as ospath
#from os.path import splitext, basename
#from os import *
from FoxDot import *


def extractDuration(element):
    return element.duration.quarterLength



def getFoxDotFromPitch(ps, pitchesToFoxDot):
        if(ps == -1):
            return 0
        try :
            return pitchesToFoxDot[ps]
        except KeyError:
            print("KeyError ps", ps )
            return getFoxDotFromPitch(ps - 1, pitchesToFoxDot)

def get_notes(notes_to_parse, pitchesToFoxDot):
    """ Get all the notes and chords from the midi files in the ./midi_songs directory """
    amps = []
    durations = []
    notes = []
    start = []

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
    return start, notes, durations, amps


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
            process_midi(mid, filename, args.chords)
        except Exception as e:
            print("Can't parse "+str(args.midi))
            print(e)
        
    elif (args.composer != None):
        #http://web.mit.edu/music21/doc/about/referenceCorpus.html
        composer = corpus.getComposer(args.composer)
        for filecorp in composer: 
            try:
                mid = corpus.parse(filecorp)
            except Exception as e:
                print("Can't parse "+str(filecorp))
                print(e)
                continue    
            
            basenamef = ospath.basename(filecorp)
            #print("basenamef",basenamef)
            filename, ext = ospath.splitext(basenamef)
            
            newdata = {
                "degree":[],
                "dur":[],
                "dur_json":[]
            }
            
            pickleFile = ospath.join("output",filename + ".pickle")
            if(ospath.isfile(pickleFile) and not args.force):
                print("loading "+pickleFile)
                with open(pickleFile,'rb') as j:
                    newdata = pickle.load(j)
            else:
                newdata = process_midi(mid, filename, args.chords)
            
            output_data["degree"] += newdata["degree"]
            output_data["dur"] += newdata["dur"]
            output_data["dur_json"] += newdata["dur_json"]
        
        jsonFile = ospath.join("output",args.composer + ".json")
        out_json =  {
            "degree":output_data["degree"],
            "dur":output_data["dur_json"]
        }
        print("Saving "+jsonFile)
        with open(jsonFile,'w') as j:
            json.dump(out_json, j)

        pickleFile = ospath.join("output",args.composer + ".pickle")
        print("Saving "+pickleFile)
        with open(pickleFile,'wb') as k:
            pickle.dump(output_data, k)
    
    elif (args.corpus != None):
        #http://web.mit.edu/music21/doc/about/referenceCorpus.html
        try:
            mid = corpus.parse(args.corpus)
            basenamef = ospath.basename(args.corpus)
            #print("basenamef",basenamef)
            filename, ext = ospath.splitext(basenamef)
            process_midi(mid, filename, args.chords)
        except Exception as e:
            print("Can't parse "+str(args.corpus))
            print(e)
        
def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


def process_midi(mid, filename, chords=False):
    output_data = {
        "degree":[],
        "dur":[],
        "dur_json":[]
    }

    data = {}
    i = 0

    allinstruments=[]
    instruments = instrument.partitionByInstrument(mid)
    if (len(instruments) == 0):
        instruments = [instruments]

    for instr in instruments:
        ##newinstrs = instrument.unbundleInstruments(instr)
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
                rootPos = scalepitches.index(rootPitch)
                pitchesToFoxDot = {scalepitches[i].ps:(i-rootPos) for i in range(len(scalepitches))}
                fd_notes = get_notes(instr[note.Note], pitchesToFoxDot)
                

                allinstruments.append( {"part":instr, "root":rootPitch.name ,"octave":minoctave, "scale":analyzedKey.mode, "pitchesToFoxDot":pitchesToFoxDot, "fd_notes":fd_notes })


    for instr in allinstruments: 
        print(instr['part'].partName,":\t", instr["root"], "octave", instr["octave"],  instr["scale"])#, instr["pitchesToFoxDot"], pitchesToFoxDot)

'''    

                    dur_export = []
                    dur_json = []
                    dur_strings = []
                    for k in range(len(dur_comp[j])):
                        if amps_comp[j][k] > 0:
                            dur_strings.append(str(dur_comp[j][k]))
                            dur_json.append(float(dur_comp[j][k]))
                            dur_export.append(float(dur_comp[j][k]))
                        else:
                            dur_strings.append("rest("+str(dur_comp[j][k])+")")
                            dur_json.append(-1*float(dur_comp[j][k]))
                            dur_export.append(rest(float(dur_comp[j][k])))
                            

                    dur_string = " ,".join(dur_strings)
                    simple_notes = list(map(simplifyNote, notes_comp[j]))

                    output_data["degree"].append(simplifyNotes(notes_comp[j],chords))
                    output_data["dur"].append(dur_export)
                    output_data["dur_json"].append(dur_json)


                    final_compas[j].append("\td{} >> pluck({},dur=[{}])\n".format(u,simple_notes,dur_string))
                    #final_compas[j].append("\td{} >> pluck({},dur={},amp={})\n".format(u,notes_comp[j],dur_comp[j],amps_comp[j]))
                u += 1
        i+=1

    final_compas = list(filter(lambda x : len(x) > 0, final_compas))
    i = 0
'''

'''
    if(len(output_data["degree"])):
        outputFile =  ospath.join("output",filename + ".py")
        print("Saving "+outputFile)

        jsonFile = ospath.join("output",filename + ".json")
        out_json =  {
            "degree":output_data["degree"],
            "dur":output_data["dur_json"]
        }
        print("Saving "+jsonFile)
        with open(jsonFile,'w') as j:
            json.dump(out_json, j)
        
        pickleFile = ospath.join("output",filename + ".pickle")
        print("Saving "+pickleFile)
        with open(pickleFile,'wb') as k:
            pickle.dump(output_data, k)
    else:
        print("No Data to save for " + filename)

    return output_data
'''

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