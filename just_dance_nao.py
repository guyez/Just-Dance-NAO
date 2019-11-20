import sys
from Utils import nao_project

from RobotPositions import AirGuitar
from RobotPositions import ArmDance
from RobotPositions import BlowKisses
from RobotPositions import Bow
from RobotPositions import Crouch
from RobotPositions import Dab
from RobotPositions import DanceMove
from RobotPositions import Hello
from RobotPositions import Sit
from RobotPositions import SitRelax
from RobotPositions import SprinklerL
from RobotPositions import SprinklerR
from RobotPositions import Stand
from RobotPositions import StandInit
from RobotPositions import StandZero
from RobotPositions import TheRobot
from RobotPositions import WipeForehead


def main(robotIP,port,song_name='RockNRollRobot.mp3',search_type='breadth'):
    initial_move = ('StandInit.py',1)
    constr_moves = [('Stand.py',2),('Sit.py',3),('Hello.py',4),('StandZero.py',2),('SitRelax.py',3),('WipeForehead.py',4),('Crouch',2)]
    result = [initial_move[0]]
    for i in costr_moves:
        nao_project.A(i,result,time - initial_move[1],search_type)
    for move in result:
        __import__('RobotPositions/' + move).main(robotIP,port)
