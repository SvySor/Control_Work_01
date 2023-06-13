from datetime import datetime
from note import Note

def read():
  notes = []
  with open('data.txt', 'r') as file:
    data = file.readlines()
    data = [elem.rstrip() for elem in data]
    data = [elem.split(';') for elem in data]
    for elem in data:
      id = int(elem[0])
      head = elem[1]
      body = elem[2]
      time_create = datetime.strptime(elem[3], '%m/%d/%Y %H:%M:%S')
      time_edit = datetime.strptime(elem[4], '%m/%d/%Y %H:%M:%S')
      note = Note(id, head, body, time_create, time_edit)
      notes.append(note)
  return notes


def write(notes):
  with open('data.txt', 'w') as file:
    string = ''
    for elem in notes:
      string += str(elem.get_id()) + ';' + \
                elem.get_head() + ';' + \
                elem.get_body() + ';' + \
                datetime.strftime(elem.get_time_create(), '%m/%d/%Y %H:%M:%S') + ';' + \
                datetime.strftime(elem.get_time_edit(), '%m/%d/%Y %H:%M:%S') + '\n'
    string = string[:-1]
    file.writelines(string)  
        