from music21 import converter, instrument, note, chord, corpus
import json
import sys
import os.path as ospath
#from os.path import splitext, basename
#from os import *
from FoxDot import *

def extractNote(element):
    return int(element.pitch.ps)

def extractDuration(element):
    return element.duration.quarterLength

def extractAmplitude(element):
    if element.isRest:
        return 0
    else:
        return 1

def midi2note(n):
    return n - 60

def midiNotes2notes(notes):
    return [tuple(map(lambda x:midi2note(x),list(note))) for note in notes]

def get_notes(notes_to_parse):

    """ Get all the notes and chords from the midi files in the ./midi_songs directory """
    amps = []
    durations = []
    notes = []
    start = []

    for element in notes_to_parse:
        if isinstance(element, note.Note):
            start.append(element.offset)
            notes.append((extractNote(element),))
            durations.append(extractDuration(element))
            amps.append(extractAmplitude(element))
                
        elif isinstance(element, chord.Chord):
            start.append(element.offset)
            durations.append(extractDuration(element))
            amps.append(extractAmplitude(element))
            notes.append(tuple([extractNote(n) for n in element.notes]))

    return start, notes, durations, amps

def findFreeSpace(note_start,last_ends):
    #print(note_start, last_ends)
    for k, last_end in last_ends.items():
        if last_end <= note_start:
            return k
    return -1
    
def notesProcessing(values,notePerCompass, nCompass):
    length = notePerCompass*nCompass

    notes_info = list(zip(values[0],values[1],values[2],values[3]))
    #notes_info = sorted(notes_info, key=lambda x : x[0])
    notes_info = sorted(list(filter(lambda x : x[0] + 4 < length, notes_info)), key=lambda x : x[0])
    
    notes_per_beat = {str(k): [] for k in map(lambda x : x[0], notes_info)}

    for note in notes_info:
        notes_per_beat[str(note[0])].append(note)

    notes_at_the_same_time = max(map(len,notes_per_beat.values()))
    #print(notes_at_the_same_time)
    final_notes = []
    final_durs = []
    final_amps = []

    final_data = {str(i):([],[],[],[]) for i in range(notes_at_the_same_time)}
    last_ends = {str(i):0 for i in range(notes_at_the_same_time)}

    for _, notes_data in notes_per_beat.items():
        for note_data in notes_data:
            k = findFreeSpace(note_data[0],last_ends)
            if k != -1:
                start, notes, durations, amps = final_data[k]
                last_end = last_ends[k]
                if last_end < note_data[0]:
                    start.append(last_end)
                    notes.append((0,))
                    durations.append(note_data[0]-last_end)
                    #durations.append("rest("+str(note_data[0]-last_end)+")")
                    amps.append(0)

                start.append(note_data[0])
                notes.append(note_data[1])
                durations.append(note_data[2])
                amps.append(note_data[3])

                if note_data[0] + note_data[2] > last_end:
                    last_ends[k] = note_data[0] + note_data[2]

    for k,v in final_data.items():
        start, notes, durations, amps = v
        if sum(durations) < length:
            start.append(-1)
            notes.append((0,))
            durations.append(length - sum(durations))
            amps.append(0)
            
    return final_data

def intoCompasses(notes,dur,amps,notePerCompass, nCompass):
    notes_comp = []
    dur_comp = []
    amps_comp = []
    
    i = 0
    j = 0
    while j < len(dur):
        if sum(dur[i:j]) == notePerCompass:
            notes_comp.append(notes[i:j])
            dur_comp.append(dur[i:j])
            amps_comp.append(amps[i:j])
            i = j

        if sum(dur[i:j]) > notePerCompass:
            notes_comp.append(notes[i:j])
            dur_comp.append(dur[i:j-1] + [notePerCompass-sum(dur[i:j-1])])
            amps_comp.append(amps[i:j])
            
            notes = notes[:j] + [notes[j-1]] + notes[j:]
            amps = amps[:j] + [amps[j-1]] + amps[j:]
            dur = dur[:j] + [(sum(dur[i:j]) - notePerCompass)] + dur[j:]

            i = j
            
        j+=1
    #print(list(map(sum,dur_comp)))
    return notes_comp,dur_comp,amps_comp

def simplifyNote(n):
    if len(n)>1:
        return n
    elif len(n)==1:
        return n[0]

def simplifyNoteF(n):
    return n[0]

def simplifyNotes(notes):
    notes =  list(map(simplifyNoteF, notes))
    pure = list(filter(lambda n : n >- 60, notes))
    clean = []
    for i in range(len(notes)):
        if notes[i] > -60 :
            clean.append(notes[i])
        else:
            if len(clean) > 0:
                clean.append(clean[-1])
            elif notes[(i+1)%len(notes)] > -60:
                clean.append(notes[(i+1)%len(notes)])
            elif(len(pure) > 0):
                clean.append(pure[i%len(pure)])
        
    return clean

def main(args):
    filename = ""
    ext = ""

    output_data = {
        "degree":[],
        "dur":[]
    }

    print("args", args)   
    if (args.midi != None):
        mid = converter.parse(args.midi)
        filename, ext = ospath.splitext(ospath.basename(args.midi))
        process_midi(mid, filename)
    elif (args.composer != None):
        #http://web.mit.edu/music21/doc/about/referenceCorpus.html
        composer = corpus.getComposer(args.composer)
        for filecorp in composer: 
            mid = corpus.parse(filecorp)
            basenamef = ospath.basename(filecorp)
            #print("basenamef",basenamef)
            filename, ext = ospath.splitext(basenamef)
            
            newdata = {
                "degree":[],
                "dur":[]
            }
            
            jsonFile = ospath.join("output",filename + ".json")
            if(ospath.isfile(jsonFile)):
                print("loading "+jsonFile)
                with open(jsonFile,'r') as j:
                    newdata = json.load(j)
                    print(newdata)
            else:
                newdata = process_midi(mid, filename)
            
            output_data["degree"] += newdata["degree"]
            output_data["dur"] += newdata["dur"]
        
        jsonFile = ospath.join("output",args.composer + ".json")
        print("Saving "+jsonFile)
        with open(jsonFile,'w') as j:
            json.dump(output_data, j)
    
    elif (args.corpus != None):
        #http://web.mit.edu/music21/doc/about/referenceCorpus.html
        mid = corpus.parse(args.corpus)
        basenamef = ospath.basename(args.corpus)
        #print("basenamef",basenamef)
        filename, ext = ospath.splitext(basenamef)
        process_midi(mid, filename)


def process_midi(mid, filename):
    output_data = {
        "degree":[],
        "dur":[]
    }

    data = {}
    i = 0

    instruments = instrument.partitionByInstrument(mid)
    if(instruments == None or len(instruments) == 0):
        data["instrument_0"] = get_notes(mid)
        
    else:
        for instrument_i in instruments.parts:
            notes_to_parse = instrument_i.recurse()

            if instrument_i.partName is None:
                data["instrument_{}".format(i)] = get_notes(notes_to_parse)
                i+=1
            else:
                data[instrument_i.partName] = get_notes(notes_to_parse)


    with open('base_file.py','r') as f:
        text = f.read()

    notePerCompass = 16
    nCompass = 30
    i = 0
    u = 0
    final_compas = [[] for _ in range(nCompass)]
    for k, v in data.items():
        if len(v[0]) > 0 and len(v[1]) > 0:
            values = list(data.values())
            values_i = values[i]
            final_data = notesProcessing(values_i,notePerCompass,nCompass)
            for final_v in final_data.values():
                notes = midiNotes2notes(final_v[1])
                dur = final_v[2]
                amps = final_v[3]
                notes_comp, dur_comp, amps_comp = intoCompasses(notes,dur,amps,notePerCompass,nCompass)
                for j in range(len(notes_comp)):
                    dur_export = []
                    dur_strings = []
                    for k in range(len(dur_comp[j])):
                        if amps_comp[j][k] > 0:
                            dur_strings.append(str(dur_comp[j][k]))
                            dur_export.append(float(dur_comp[j][k]))
                        else:
                            dur_strings.append("rest("+str(dur_comp[j][k])+")")
                            dur_export.append(-1*float(dur_comp[j][k]))

                    dur_string = " ,".join(dur_strings)
                    simple_notes = list(map(simplifyNote, notes_comp[j]))

                    output_data["degree"].append(simplifyNotes(notes_comp[j]))
                    output_data["dur"].append(dur_export)

                    final_compas[j].append("\td{} >> pluck({},dur=[{}])\n".format(u,simple_notes,dur_string))
                    #final_compas[j].append("\td{} >> pluck({},dur={},amp={})\n".format(u,notes_comp[j],dur_comp[j],amps_comp[j]))
                u += 1
        i+=1

    final_compas = list(filter(lambda x : len(x) > 0, final_compas))
    i = 0
    for compass in final_compas:
            text += "@structure\n"
            text += "def a{}():\n".format(i)
            i+=1
            for instrument_i in compass:
                text += instrument_i
    text += "Clock.clear()\n"
    text += "\nstart = Clock.mod({}) - 0.1\n".format(notePerCompass)
    for i in range(len(final_compas)):
            text += "Clock.schedule(a{}, start + {})\n".format(i,notePerCompass*i)

    text += "Clock.schedule(lambda : Clock.clear(), start + {})\n".format(notePerCompass*(i+1))

    if(len(output_data["degree"])):
        outputFile =  ospath.join("output",filename + ".py")
        print("Saving "+outputFile)
        with open(outputFile,'w') as f:
            f.write(text)

        jsonFile = ospath.join("output",filename + ".json")
        print("Saving "+jsonFile)
        with open(jsonFile,'w') as j:
            json.dump(output_data, j)
    else:
        print("No Data to save for " + filename)

    return output_data


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process files into the data format for learning.')
    parser.add_argument('--midi', help='file to convert')#, default="midis/bad_guy.mid")
    parser.add_argument('--corpus', help='file from corpus http://web.mit.edu/music21/doc/about/referenceCorpus.html', default='bach/bwv108.6.xml')
    parser.add_argument('--composer', help='Music21 Compsoer info to learn from')#, default="midis/bad_guy.mid")
    '''parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    '''

    args = parser.parse_args()

    main(args)