from operator import ge
from operator import eq
from operator import sub
from operator import add
from operator import lt

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

#Mosse non obbigatorie
mossa = Operator('mossa',
[('Move','?m'),
 ('Cost','?m','?c'), #Mosse
 ('Time','?t'),
 ('StateCounter','?s'),
 (ge,'?t','?c'),
 (lt,'?s',5)],
[('not',('Time','?t')),
 ('Time',(sub,'?t','?c')),
 ('not',('StateCounter','?s')),
 ('StateCounter',(add,'?s',1))
 ])
 
 
 #Mosse obligatorie
mossaObb = Operator('mossaObb',
[('MoveC','?m'),
 ('Cost','?m','?c'),
 ('Time','?t'),
 ('StateCounter','?s'),
 (ge,'?t','?c'),
 (eq,'?s',5)],
[('not',('Time','?t')),
 ('Time',(sub,'?t','?c')),
 ('not',('StateCounter','?s')),
 ('StateCounter',(add,'?s',1))
 ])





start = [('MoveC','StandInit'), 
         ('Time',25),
		 ('StateCounter',0),
		 ('MoveC','Sit'),('Cost','Sit',5),
		 ('MoveC','StandInit'),('Cost','StandInit',3),
		 ('MoveC','SitRelax'),('Cost','SitRelax',4),
		 ('MoveC','WipeForehead'),('Cost','WipeForehead',2),
		 ('MoveC','Hello'),('Cost','Hello',3),
		 ('MoveC','Stand'),('Cost','Stand',4),
		 ('MoveC','StandZero'),('Cost','StandZero',5),
		 ('MoveC','Crouch'),('Cost','Crouch',3),
		 ('Move','ArmDance'),('Cost','ArmDance',5),
		 ('Move','Dab'),('Cost','Dab',5),
		 ('Move','BlowKiss'),('Cost','BlowKiss',5),
		 ('Move','Bow'),('Cost','Bow',5)      
		 ] #domain

goal = [('MoveC','StandZero'),
         ('StateCounter',6)
		]

'''
def progression(x):
    return breadth_first_search(x, forward=True, backward=False)


def regression(x):
    return breadth_first_search(x, forward=False, backward=True)


def bidirectional(x):
    return breadth_first_search(x, forward=True, backward=True)
'''
'''
def progression(problem):
    return partial(depth_first_search, forward=True, backward=False)(problem)


def regression(problem):
    return partial(depth_first_search, forward=False, backward=True)(problem)

def bidirectional(problem):
    return partial(depth_first_search, forward=True, backward=True)(problem)
'''

def progression(x):
    return tree_search(x)


def regression(x):
    return tree_search(x)


def bidirectional(x):
    return tree_search(x)

p = StateSpacePlanningProblem(start, goal, [mossa, mossaObb])

compare_searches([p], [progression,  regression,
                       bidirectional])

print(next(progression(p)).path())
path = next(regression(p)).path()

print(path[0][0])
