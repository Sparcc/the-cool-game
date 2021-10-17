from helpers import *

class Settings(DatabaseHelper):
  def __init__(self):
    super().__init__("settings")

  def getValue(self, field, value):
    self.cur.execute("SELECT * FROM "+self.table+" WHERE "+field+" = '"+value+"'")
    #print(self.cur.fetchone()[1])
    return self.cur.fetchone()[1]
