import sys
import importlib
from Utils import nao_project
from RobotPositions import *

# from RobotPositions import AirGuitar
# from RobotPositions import ArmDance
# from RobotPositions import BlowKisses
# from RobotPositions import Bow
# from RobotPositions import Crouch
# from RobotPositions import Dab
# from RobotPositions import DanceMove
# from RobotPositions import Hello
# from RobotPositions import Sit
# from RobotPositions import SitRelax
# from RobotPositions import SprinklerL
# from RobotPositions import SprinklerR
# from RobotPositions import Stand
# from RobotPositions import StandInit
# from RobotPositions import StandZero
# from RobotPositions import TheRobot
# from RobotPositions import WipeForehead



def main(robotIP,port,song_name='RockNRollRobot.mp3',search_type='breadth'):
	initial_move = ('StandInit',1)
	constr_moves = [('Stand',2),('Sit',3),('Hello',4),('StandZero',2),('SitRelax',3),('WipeForehead',4),('Crouch',2)]
	result = [initial_move[0]]
	for i in constr_moves:
		nao_project.A(i,result)
	print(result)
	
	for move in result:
		importlib.import_module("."+move,"RobotPositions").main(robotIP,port)
		
if __name__ == "__main__":

    port = int(sys.argv[2])
    robotIP = sys.argv[1]

    main(robotIP, port)