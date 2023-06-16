from newnote import newnote
from datetime import datetime
from checkindex import checkindex
from searchnote import searchnote
from deletenote import deleteNote
from data import write

def menu(notes):
  while True:
    print()
    print ('Select function:')
    print ('1 - list all notes')
    print ('2 - add new notes')
    print ('3 - read note')
    print ('4 - edit note')
    print ('5 - delete note')
    print ('0 - exit program')
    print ('Select option: ')
    opnumber = int(input())
    print()
    while opnumber < 0 or opnumber > 6 :
      print('Input correct number')
      opnumber = int(input())
    if opnumber == 1:
      listAllNotesMenu(notes)
    elif opnumber == 2:
      addNewNoteMenu(notes)
    elif opnumber == 3:
      readNoteMenu(notes)
    elif opnumber == 4:
      editNoteMenu(notes)
    elif opnumber == 5:
      deleteNoteMenu(notes)
    elif opnumber == 0:
      break
  print('Buy!')

# 1 - List all notes
def listAllNotesMenu(notes):
  print('All notes:')
  if len(notes) == 0 :
    print('There are no notes in notebook')
  else:
    for i in notes:
      print(repr(i))

# 2 - add new note
def addNewNoteMenu(notes):  
  print('Input new note')
  print('Input note head:')
  head = input()
  print('Input note body')
  body = input()
  notes = newnote(notes, head, body, datetime.now(), datetime.now())
  print('New note added')
  print(repr(notes[-1]))
  return notes

# 3 - read note
def readNoteMenu(notes):
  if len(notes) == 0 :
    print('There are no notes in notebook')
  else:
    print('Input note index')
    id = int(input())
    while not (checkindex(notes, id)):
      print('Input correct id')
      id = int(input())
    note = searchnote(notes, id)
    print(repr(note))
    
# 4 - edit note
def editNoteMenu(notes):
  if len(notes) == 0 :
    print('There are no notes in notebook')
  else:
    print('Input note index to edit')
    id = int(input())
    while not (checkindex(notes, id)):
      print('Input correct id')
      id = int(input())
    note = searchnote(notes, id)
    print(repr(note))
    print('Edit this note')
    print('Input new note head:')
    head = input()
    print('Input new note body')
    body = input()
    print('Rewrite this note with new data?')
    check = input()
    if check :
      note.set_head(head)
      note.set_body(body)
      note.set_time_edit(datetime.now())
      notes = deleteNote(notes, id)
      notes.append(note)
      write(notes)
    else:
      print('Nothing was edited')
  return notes
  
# 5 - delete note
def deleteNoteMenu(notes):
  if len(notes) == 0 :
    print('There are no notes in notebook')
  else:
    print('Input note index to delete')
    id = int(input())
    while not (checkindex(notes, id)):
      print('Input correct id')
      id = int(input())
    note = searchnote(notes, id)
    print(repr(note))
    print('Delete this note?')
    check = input()
    if check :
      notes = deleteNote(notes, id)
    else:
      print('Nothing was deleted')
  return notes
