
def searchnote (notes, id):
  for i in notes:
    if i.get_id() == id:
      return i
      
