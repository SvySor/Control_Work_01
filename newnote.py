from note import Note
from data import write

def newnote (notes, head, body, time_created, time_edited):
  note = Note(idgenerator(notes), head, body, time_created, time_edited)
  notes.append(note)
  write(notes)
  return notes

def idgenerator(notes):
  idx = 0
  for i in notes:
    idx = max(idx, i.get_id())
  return idx + 1