import sqlite3
class DatabaseHelper():
  con = None
  def __init__(self, table):
    self.con = sqlite3.connect('sql-data.db')
    self.table = table
    self.cur = self.con.cursor()
  def find(self, field, value):
    return self.cur.execute("SELECT * FROM "+self.table+" WHERE "+field+" = '"+value+"'")