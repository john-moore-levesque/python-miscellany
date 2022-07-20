import datetime
import time
import numpy
import json


def chime():
    notefreqs = {}
    with open('notes-frequencies.json') as jsonfile:
        notefreqs = json.load(jsonfile)

    frequencies = [notefreqs['A4'], notefreqs['C#5'], notefreqs['E5']]
    notes = []
    sample_rate = 44100
    T = 0.25
    t = numpy.linspace(0, T, T * sample_rate, False)

    for frequency in frequencies:
        note = numpy.sin(frequency * t * 2 * numpy.pi)
        notes.append(note)

    audio = numpy.hstack(tuple(notes))
    audio *= 32767 / numpy.max(numpy.abs(audio))
    audio = audio.astype(numpy.int16)


def timer(duration):
    countdown = []
    totalseconds = 0
    for t in duration.split(':'):
        try:
            countdown.append(int(t))
        except AssertionError:
            pass

    if len(countdown) > 3:
        return False
    elif len(countdown) == 3:
        hours, minutes, seconds = countdown
        totalseconds = (hours * 3600) + (minutes * 60) + seconds
    elif len(countdown) == 2:
        minutes, seconds = countdown
        totalseconds = (minutes * 60) + seconds
    else:
        seconds = countdown[0]
        totalseconds = seconds

    starttime = datetime.datetime.now().strftime('%H:%M:%S')
    for remaining in range(totalseconds, 0, -1):
        print("Timer started at %s" %(starttime))
        hours = remaining // 3600
        minutes = (remaining % 3600) // 60
        seconds = remaining % 60
        print("%d hours, %d minutes, %d seconds remaining" %(hours, minutes, seconds))
        time.sleep(1)

    print("Time's up! Finished at %s" %(datetime.datetime.now().strftime('%H:%M:%S')))
    chime()
