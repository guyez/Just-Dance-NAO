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

def breadth(x):
        return breadth_first_search(x, forward=True, backward=False)
    
def depth(x):
        return depth_first_search(x, forward=True, backward=False)


def A(constraint_move,result,time=180,search_type='breadth'):
    final_move = constraint_move[0]
    cost_final_move = constraint_move[1]
    
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
    [('not',('Time','?t')),				#Effetti: il tempo disponibile is no more t,
     ('Time',(sub,'?t','?c')),				#       il tempo disponbile diventa t-c ,
     ('not',('StateCounter','?s')),			#       il contatore is no more  s,
     ('StateCounter',(add,'?s',1))			#       il contatore si aggiorna a s+1
     ])
     
    #Applicare mossa per verificare le condizioni di successo (Non si puo fare direttamente da 'goal' in quanto non si possono esprimere condizioni di >,<,>=,<= ): check
    check = Operator('check',
    [									#Prerequisiti: check
    ('StateCounter','?s'),					#            contatore delle mosse eseguite: s,
    ('Time','?t'),							#            tempo rimanente: t,
    (le,'?t',1.3),							#            il tempo rimanente deve essere inferiore ad una soglia,
    (ge,'?s',5)								#            il contatore delle mosse eseguite deve essere maggiore o uguale a 5,
    ],
    [('not',('Check','NO')),				#Effetti: passiamo da Check NO a Check SI
    ('Check','SI')])
     
     

    period=round((time/7) - cost_final_move,2)
    start = [('Time',period),
                     ('StateCounter',0),
                     ('Check','NO'),
                     ('Move','AirGuitar'),('Cost','AirGuitar',5),
                     ('Move','ArmDance'),('Cost','ArmDance',11),
                     ('Move','BlowKisses'),('Cost','BlowKisses',5),
                     ('Move','Bow'),('Cost','Bow',4),
                     ('Move','DanceMove'),('Cost','DanceMove',6),
                     ('Move','SprinklerL'),('Cost','SprinklerL',4),
                     ('Move','SprinklerR'),('Cost','SprinklerR',4),
                     ('Move','Dab'),('Cost','Dab',3),
                     ('Move','TheRobot'),('Cost','TheRobot',6)	 
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
