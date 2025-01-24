# Basic Note Generator by [Voidpiercer]
# Adding quarter notes sequentially ...

import flpianoroll as flp

notes = [48,52,55,60] # C4, E4, G4, C5
vel = [0.7, 0.8, 0.9, 1.0] # Increasing velocity
color = [0,3,6,9] # Green, Blue, Purple, Pink
start = [0,96,192,288] # Quarter Notes / 1 Bar
length = 96 # PPQ (ticks)
test = "test"

# Interate 4 times, Generating Notes of varying color ...

for index, i in enumerate(notes):
    note = flp.Note()
    note.number = notes[index]
    note.velocity = vel[index]
    note.time = start[index]
    note.length = length
    note.color = color[index]
    note.selected = False
    flp.score.addNote(note)

# Iterate 4 times, adding the associated note markers ...

mark_name = ["C4", "E4", "G4", "C5"]

for index, i in enumerate(mark_name):
    Mark = flp.Marker()
    Mark.name = mark_name[index]
    Mark.time = start[index]
    flp.score.addMarker(Mark)

















