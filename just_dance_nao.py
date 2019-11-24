import importlib
import os
import argparse
import time
from mutagen.mp3 import MP3
from pygame import mixer
from Utils import nao_project
from RobotPositions import *


parser = argparse.ArgumentParser(description='Argument parser')
parser.add_argument('--port', dest='port', type=int, default=9559, help='number of the virtual robot port')
parser.add_argument('--ip', dest='ip',type=str,default='127.0.0.1', help='ip number')
parser.add_argument('--song', dest='song', type=str, default='RockNRollRobot.mp3', help="Song's name")
parser.add_argument('--search', dest='search', type=str, default='breadth', help='Name of the search algorithm. The only possible values are depth and breadth')
args = parser.parse_args()

def main(robotIP,port,song_name = 'RockNRollRobot.mp3',search_type = 'breadth'):
	initial_move = ('StandInit',1.13)
	time_initial_move = initial_move[1]
	constr_moves = [('Stand',2.02),('Sit',3.02),('Hello',4.02),('StandZero',2.02),('SitRelax',3.02),('WipeForehead',4.02),('Crouch',2.02)]
	result = [initial_move[0]]
	
	file_data = os.path.splitext(song_name)
	if file_data[1] == '.mp3':
		audio = MP3("./Songs/" + song_name)
		total_length = audio.info.length
	else:
		a = mixer.Sound("./Songs/" + song_name)
		total_length = a.get_length()

	song_length = round(total_length,2)
	#print(song_length)
	for i in constr_moves:
		nao_project.A(i,result,song_length - time_initial_move,search_type)
	print(result)
	
	mixer.init()
	mixer.music.load("./Songs/" + song_name)
	mixer.music.play()
	
	
	start = 0
	
	for i,move in enumerate(result):
		if i != 0:
			print('{0:20}  {1}'.format(result[i-1], round((time.time() - start),2)))
		start = time.time()
		importlib.import_module("." + move,"RobotPositions").main(robotIP,port)
		if i == 0:
			print('\n{0:20}  {1}\n'.format('Move', 'Cost(in seconds)'))
		
	print('{0:20}  {1}'.format(result[-1], round((time.time() - start),2)))
	time.sleep(2)
	# playing_time = round(mixer.music.get_pos()/1000.0,2)
	# while ((total_length - playing_time) > 0):
		# playing_time = round(mixer.music.get_pos()/1000.0,2)
	
	
if __name__ == "__main__":
	port = args.port
	robotIP = args.ip
	song_name = args.song
	search_type = args.search
	if(search_type != 'depth' and search_type != 'breadth'):
		print('The only possible values for --search argument are depth and breadth')
		exit(1)
	main(robotIP, port, song_name, search_type)
	


	







