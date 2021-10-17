
from utils import Settings
from core_components import Game

settings = Settings()
game = Game()

while(game.isRunning):
    print('game.isRunning='+str(game.isRunning))
    command = input()
    game.acceptCommand(command)