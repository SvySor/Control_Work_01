def checkindex(notes, id):
  for i in notes:
    if i.get_id() == id:
      return True
  return False
