from data import write

def deleteNote (notes, id):
  for i in notes:
    if i.get_id() == id:
      notes.remove(i)
      break
  write(notes)
  return notes
  