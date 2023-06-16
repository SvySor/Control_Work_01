from data import read
from menu import menu

if __name__ == '__main__':
  notes = read()
  menu(notes)