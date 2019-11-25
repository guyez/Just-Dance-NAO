## Importing Modules ##

from operator import ge
from operator import sub
from operator import add
from operator import le

from functools import partial

from py_search.uninformed import breadth_first_search
from py_search.uninformed import depth_first_search
from py_search.uninformed import tree_search
from py_search.uninformed import graph_search
from py_search.uninformed import choose_search
from py_search.uninformed import iterative_deepening_search
from py_search.uninformed import iterative_sampling

from py_plan.total_order import StateSpacePlanningProblem
from py_plan.base import Operator

class project:
	def __init__(self,constraint_moves,moves,time=180,search_type='breadth'):
		self.constraint_moves = constraint_moves
		self.moves = moves
		self.time = time
		self.search_type = search_type
		
	## Defining two types of Non-Informed Search Strategies ## 

	def breadth(self,x):
			return breadth_first_search(x, forward=True, backward=False)
		
	def depth(self,x):
			return depth_first_search(x, forward=True, backward=False)

	## Defining the algorithm A ##

	def A(self,result,constraint_move):
		final_move = constraint_move[0]
		cost_final_move = constraint_move[1]
		
		#################
		##  OPERATIONS ##
		#################

		#Applying an intermediate position: move
		move = Operator('mossa',
		[('Move','?m'),						#Preconditions: move: m,
		 ('Cost','?m','?c'),					#               cost of the move m (time required): c,
		 ('Time','?t'),						#               time when move m is performed: t,
		 ('StateCounter','?s'),					#               counter of the executed moves: s,
		 (ge,'?t','?c')						#               available time t must be greater than c.
		 ],
		[('not',('Time','?t')),				        #Postconditions: available time must be less than or equal to t,
		 ('Time',(sub,'?t','?c')),				        #                available time becomes t-c ,
		 ('not',('StateCounter','?s')),			        #                counter is no longer s,
		 ('StateCounter',(add,'?s',1))			        #                counter is updated to s+1.
		 ])
		 
		#Applying move to verify the successful conditions, i.e. a path given the problem description and satisfies all the constraints (It is not possible to do this operation directly from the Goal state since it is not possible to express conditions of >,<,>=,<= ): check
		check = Operator('check',
		[								#Preconditions: check
		('StateCounter','?s'),					#               counter of the executed moves: s,
		('Time','?t'),						#               time left: t,
		(le,'?t',0.2),						#               time left must be less than a given threshold,
		(ge,'?s',5)							#               counter of the executed moves must be greater than or equal to 5,
		],
		[('not',('Check','NO')),				        #Postconditions: moving from Check NO to Check SI
		('Check','SI')])
		 
		 

		period=round((self.time/7) - cost_final_move,2)
		move_cost_list = [[('Move',i[0]),('Cost',i[0],i[1])] for i in self.moves]
		start = [('Time',period),('StateCounter',0)]
		for k in move_cost_list:
			start += k
		goal = [('Check','SI')]

		p = StateSpacePlanningProblem(start, goal, [move,check])
		 
		temp_path=[]
		if self.search_type == 'breadth':
			for i in range(len(next(self.breadth(p)).path())-1):
				temp_path.append(((next(self.breadth(p)).path())[i][1]["?m"]))
			print(temp_path)
		elif self.search_type == 'depth':
			for i in range(len(next(self.depth(p)).path())-1):
				temp_path.append(((next(self.depth(p)).path())[i][1]["?m"]))
			print(temp_path)
		else:
			print(' the only possible values for the argument search_type are "depth", "breadth" ')

		result += temp_path
		result.append(final_move)
