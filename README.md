# midi2foxdot

Small script to convert midi files (and the music21 corpus files into FoxDot code (A python live coding framework) and foxdot compatible arrays for machine learning experiments for FoxDot.

## Requirements

- python
- music21 python library (Try something like: `pip install music21`)

## Usage
It is used running the main script `midi2code.py` it takes an input midi file and converts that into a text file that can be used inside FoxDot the python live coding framework.

### Usage example

```
python midi2code.py --midi INPUT_MIDI

python midi2code.py --midi midis/bad_guy.mid
```

The generated code divides the song into pieces with a duration of 8 beats in order to make it easier to modify and read the code. You can change the variables `notePerCompass` and `nCompass` at `midi2code.py` to change the duration of each part (16 beats by default) and the number of parts extracted from the song (30 by default).
