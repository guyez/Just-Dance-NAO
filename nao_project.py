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



#################
##  OPERAZIONI ##
#################

#Applicare mossa non obbligatoria: mossa
mossa = Operator('mossa',
[('Move','?m'),						#Prerequisiti: mossa: m,
 ('Cost','?m','?c'),					#            costo della mossa m (tempo che ci impiega): c,
 ('Time','?t'),							#            tempo al momento in cui si fa la mossa: t,
 ('StateCounter','?s'),					#            contatore delle mosse eseguite: s,
 (ge,'?t','?c')							#            il tempo t disponibile deve essere maggiore di c,
 ],
[('not',('Time','?t')),				#Effetti: il tempo disponibile non è più t,
 ('Time',(sub,'?t','?c')),				#       il tempo disponbile diventa t-c ,
 ('not',('StateCounter','?s')),			#       il contatore non è più s,
 ('StateCounter',(add,'?s',1))			#       il contatore si aggiorna a s+1
 ])
 
#Applicare mossa per verificare le condizioni di successo (Non si può fare direttamente da 'goal' in quanto non si possono esprimere condizioni di >,<,>=,<= ): check
check = Operator('check',
[									#Prerequisiti: check
('StateCounter','?s'),					#            contatore delle mosse eseguite: s,
('Time','?t'),							#            tempo rimanente: t,
(le,'?t',0.5),							#            il tempo rimanente deve essere inferiore ad una soglia (in questo caso ho impostato 0.5),
(ge,'?s',5)								#            il contatore delle mosse eseguite deve essere maggiore o uguale a 5,
],
[('not',('Check','NO')),				#Effetti: passiamo da Check NO a Check SI
('Check','SI')])
 
 


start = [('Time',25),# T - T_mossa_finale (es. 25.71 - 3.40)
		 ('StateCounter',0),
		 ('Check','NO'),
		 ('Move','AirGuitar'),('Cost','AirGuitar',4),
		 ('Move','ArmDance'),('Cost','ArmDance',10),
		 ('Move','BlowKisses'),('Cost','BlowKisses',4.2),
		 ('Move','Bow'),('Cost','Bow',3),
		 ('Move','DanceMove'),('Cost','DanceMove',6),
		 ('Move','SprinklerL'),('Cost','SprinklerL',4),
		 ('Move','SprinklerR'),('Cost','SprinklerR',4),
		 ('Move','Dab'),('Cost','Dab',3),
		 ('Move','TheRobot'),('Cost','TheRobot',6)	 
		 ] #domain

goal = [('Check','SI')]


def progression(x):
    return breadth_first_search(x, forward=True, backward=False)


def regression(x):
    return breadth_first_search(x, forward=False, backward=True)


def bidirectional(x):
    return breadth_first_search(x, forward=True, backward=True)

'''
def progression(problem):
    return partial(depth_first_search, forward=True, backward=False)(problem)


def regression(problem):
    return partial(depth_first_search, forward=False, backward=True)(problem)

def bidirectional(problem):
    return partial(depth_first_search, forward=True, backward=True)(problem)
'''


p = StateSpacePlanningProblem(start, goal, [mossa,check])

compare_searches([p], [progression,  regression,
                       bidirectional])

print(next(progression(p)).path())
path = next(regression(p)).path()

print(path[0][0])
