from datetime import datetime

class Note():
  def __init__(self, id, head, body, time_create, time_edit):
    self.id = id
    self.head = head
    self.body = body
    self.time_create = time_create
    self.time_edit = time_edit

  def get_id(self):
    return self.id

  def set_id(self, id):
    self.id = id

  def get_head(self):
    return self.head

  def set_head(self, head):
    self.head = head

  def get_body(self):
    return self.body

  def set_body(self, body):
    self.body = body

  def get_time_create(self):
    return self.time_create

  def set_time_create(self, time_create):
    self.time_create = time_create

  def get_time_edit(self):
    return self.time_edit

  def set_time_edit(self, time_edit):
    self.time_edit = time_edit

  def __repr__(self):
    return f"id = {self.id}, head = {self.head}, body = {self.body}, create time = {self.time_create}, edit time = {self.time_edit}"

note1 = Note(1, 'Заголовок', 'Что-то', datetime.now(), datetime.now())
