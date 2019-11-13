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

#################
##  OPERAZIONI ##
#################

#Applicare mossa non obbligatoria: mossa
mossa = Operator('mossa', 
[('Move','?m'),                       #Prerequisiti: mossa: m,
 ('Cost','?m','?c'),                    #            costo della mossa m (tempo che ci impiega): c,
 ('Time','?t'),                         #            tempo al momento in cui si fa la mossa: t,
 ('StateCounter','?s'),                 #            contatore delle mosse eseguite: s,
 (ge,'?t','?c'),                        #            il tempo t disponibile deve essere maggiore di c,
 (lt,'?s',5)],                          #            il contatore s deve essere minore di 5 (altrimenti si dovrebbe fare una mossa obbligatoria (quella detta in goal)
[('not',('Time','?t')),               #Effetti: il tempo disponibile non è più t,
 ('Time',(sub,'?t','?c')),              #       il tempo disponbile diventa t-c ,            
 ('not',('StateCounter','?s')),         #       il contatore non è più s,
 ('StateCounter',(add,'?s',1))          #       il contatore si aggiorna a s+1
 ])
 
#Applicare mossa obbligatoria: mossaObb
mossaObb = Operator('mossaObb',
[('MoveC','?m'),                      #Come prima in mossa
 ('Cost','?m','?c'),
 ('Time','?t'),
 ('StateCounter','?s'),
 (ge,'?t','?c'),
 (eq,'?s',5)],                       #il contatore s deve essere uguale a 5 (facciamo le mosse obbligatorie solo quando è necessario)
[('not',('Time','?t')),
 ('Time',(sub,'?t','?c')),
 ('not',('StateCounter','?s')),
 ('StateCounter',(add,'?s',1))
 ])
 
####################
## STATO INIZIALE ##
####################
start = [('MoveC','StandInit'),                                     #Stato iniziale: Trovarsi in standInit
         ('Time',25),                                                      #         Tempo disponibile = 25
		 ('StateCounter',0),                                               #         contatore = 0
		 ('MoveC','Sit'),('Cost','Sit',5),                          #Dominio: Sit:mossa obbligatoria; Costo di sit=5;
		 ('MoveC','StandInit'),('Cost','StandInit',3),                 #      StandInit: ...
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


########################
##  STATO FINALE/GOAL ##
########################

goal = [('MoveC','StandZero'),                            #Goal: posizione standzero e counter = 6
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
