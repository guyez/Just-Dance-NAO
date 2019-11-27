# Import required libraries for the simulation:
import importlib
import os
import argparse
import time
from mutagen.mp3 import MP3
from pygame import mixer
from Utils import nao_project
from RobotPositions import *

# Arguments to be passed to the Command Prompt:
parser = argparse.ArgumentParser(description='Argument parser')
parser.add_argument('--port', dest='port', type=int, default=9559, help='number of the virtual robot port') 
parser.add_argument('--ip', dest='ip',type=str,default='127.0.0.1', help='ip number')
parser.add_argument('--song', dest='song', type=str, default='RockNRollRobot.mp3', help="Song's name")
parser.add_argument('--search', dest='search', type=str, default='breadth', 
help='Name of the search algorithm. The only possible values are depth, breadth, iterdeep')
parser.add_argument('--threshold', dest='threshold', type=float, default=0.5, help="Threshold")
args = parser.parse_args()

# Function that is executed: it searches and executes the optimal sequence of moves with respect to the song's duration 
def main(robotIP,port,song_name = 'RockNRollRobot_from_0.11.mp3',search_type = 'breadth',threshold = 0.5): #the parameters are passed through the cmd Prompt
	initial_move = ('StandInit',1.13)           # Name of the initial move and its duration
	time_initial_move = initial_move[1]
	
	moves = [('AirGuitar',5.24),                # List of the possible moves to be executed, expressed as a tuple containing the name of the move and its duration
	('ArmDance',11.34),                         
	('BlowKisses',4.64),
	('Bow',4.6),
	('DanceMove',6.04),
	('SprinklerL',4.04),
	('SprinklerR',4.04),
	('Dab',3.04),
	('TheRobot',6.04),
	('ComeOn',4.61),
	('StayingAlive',5.91),
	('Rhythm',3.96),
	('PulpFiction',5.56)]
	
	constr_moves = [('Stand',2.02),             # List of the mandatory positions, expressed as a tuple containing the name of the move and its duration
	('Sit',3.02),
	('Hello',4.02),
	('StandZero',2.02),
	('SitRelax',3.02),
	('WipeForehead',4.02),
	('Crouch',2.02)]
	
	result = [initial_move[0]]                  # List in which the sequence of moves to be executed is stored
	
	file_data = os.path.splitext(song_name)     # Assign to file_data the song name passed to the function as an argument
	if file_data[1] == '.mp3':                  # Recover the song length
		audio = MP3("./Songs/" + song_name)
		total_length = audio.info.length
	else:
		a = mixer.Sound("./Songs/" + song_name) 
		total_length = a.get_length()

	song_length = round(total_length,2)         # Round the song length
	# print(song_length)
	
    # Instantiate the variable our_project as instance of nao_project.project class with attributes: 
    # The mandatory positions, the list of possible moves, the available time, the type of search
	our_project = nao_project.project(constr_moves,moves,song_length - time_initial_move,search_type,threshold)   
	
    # For each of the mandatory positions run the method A in the class project with parameters the updated 
    # List of the moves to be executed and the next mandatory move
	start = time.time()
	for i in constr_moves:
		our_project.A(result,i)
	print('Computational time with searchtype = ' + search_type)
	print(round((time.time() - start),2))
	print(result)
	
	mixer.init()                                
	mixer.music.load("./Songs/" + song_name)        # Load the song
	mixer.music.play()                              # Play the song
	
	
	start = 0
	
	# for i,move in enumerate(result):
		# if i != 0:
			# print('{0:20}  {1}'.format(result[i-1], round((time.time() - start),2)))     # Print a table on the cmd with the move that is being executed and its cost
		# start = time.time()
		# importlib.import_module("." + move,"RobotPositions").main(robotIP,port)          # Import the movements
		# if i == 0:
			# print('\n{0:20}  {1}\n'.format('Move', 'Cost (in seconds)'))                 # Heading of the table
		
	# print('{0:20}  {1}'.format(result[-1], round((time.time() - start),2)))              # Print the last line of the table
	# time.sleep(2)
	# playing_time = round(mixer.music.get_pos()/1000.0,2)
	# while ((total_length - playing_time) > 0):
		# playing_time = round(mixer.music.get_pos()/1000.0,2)
	
	
if __name__ == "__main__":                                                               
	port = args.port
	robotIP = args.ip
	song_name = args.song
	search_type = args.search
	threshold = args.threshold
	if(search_type not in ['depth','breadth','iterdeep']):
		print('The only possible values for --search argument are depth, breadthand iterdeep')
		exit(1)
	main(robotIP, port, song_name, search_type,threshold)
	


	







