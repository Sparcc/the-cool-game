class CommandInterpreter():
    #commandLookup
    #def __init__(self):
    #  parse.
    def read(command,*arguments):
      print('command='+command)
      
class Game():
  isRunning = True
  com = None
  def __init__(self):
    self.com = CommandInterpreter()

  # Take input from user
  def acceptCommand(self,command):
      # Quit the game
      if command == 'exit' or command == 'quit' or command == 'end':
        self.endGame()

      # Continue the game
      elif self.isRunning:
        self.com

  def endGame():
    self.isRunning = False
  
  