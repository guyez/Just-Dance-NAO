## Importing Modules ##

from operator import ge
from operator import gt
from operator import eq
from operator import sub
from operator import add
from operator import lt
from operator import le

from functools import partial

from py_search.utils import compare_searches
from py_search.uninformed import breadth_first_search
from py_search.uninformed import depth_first_search
from py_search.uninformed import tree_search
from py_search.uninformed import graph_search
from py_search.uninformed import choose_search
from py_search.uninformed import iterative_deepening_search
from py_search.uninformed import iterative_sampling

from py_plan.total_order import StateSpacePlanningProblem
from py_plan.base import Operator

## Defining two types of Non-Informed Search Strategies ## 

def breadth(x):
        return breadth_first_search(x, forward=True, backward=False)
    
def depth(x):
        return depth_first_search(x, forward=True, backward=False)

## Defining the algorithm A ##

def A(constraint_move,result,time=180,search_type='breadth'):
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
     
     

    period=round((time/7) - cost_final_move,2)
    start = [('Time',period),
                     ('StateCounter',0),
                     ('Check','NO'),
                     ('Move','AirGuitar'),('Cost','AirGuitar',5.24),
                     ('Move','ArmDance'),('Cost','ArmDance',11.34),
                     ('Move','BlowKisses'),('Cost','BlowKisses',4.64),
                     ('Move','Bow'),('Cost','Bow',4.6),
                     ('Move','DanceMove'),('Cost','DanceMove',6.04),
                     ('Move','SprinklerL'),('Cost','SprinklerL',4.04),
                     ('Move','SprinklerR'),('Cost','SprinklerR',4.04),
                     ('Move','Dab'),('Cost','Dab',3.04),
                     ('Move','TheRobot'),('Cost','TheRobot',6.04)	 
                     ] #domain

    goal = [('Check','SI')]

    
    



    p = StateSpacePlanningProblem(start, goal, [mossa,check])
     
    ups=[]
    if search_type == 'breadth':
        for i in range(len(next(breadth(p)).path())-1):
            ups.append(((next(breadth(p)).path())[i][1]["?m"]))
        print(ups)
    elif search_type == 'depth':
        for i in range(len(next(depth(p)).path())-1):
            ups.append(((next(depth(p)).path())[i][1]["?m"]))
        print(ups)
    else:
        print(' the only possible values for the argument search_type are "depth", "breadth" ')

    result += ups
    result.append(final_move)
