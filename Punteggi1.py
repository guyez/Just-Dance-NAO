# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:57:10 2019

@author: ramsi
"""
#LEGENDA: 0-NO ; 1-OK, 2-BENE ; 3-OTTIMO

# 1) Ho realizzato una matrice per i punteggi. Se pensate che è meglio avere un dataframe con i nomi a righe e colonne ditemelo.
import numpy as np

movements_arms=[1,2,3,4,5] #queste sono le mosse che coinvolgono solo le mani
movement_legs=[7,8,9,10,12,13] #queste sono le mosse che coinvolgono movimenti dei piedi e non sono di base
movement_base=[6,11,14,15,16,17]
 
# 2) La colonna 16sit e 17sitRelax sono dati da zeri perchè secondo me non ci stanno dopo nessun movimento e li farei
#   solo con le mosse obbligatorie.Se pensate che vanno inclusi ditemelo che ho i punteggi pronti per sostituirli.  
punteggi_base=np.array([[3,2,2,2,2,2,2,2,2,2,2,2,1,0,2,0,0],
                       [2,3,2,2,2,2,2,2,2,2,2,2,1,2,2,0,0],
                       [2,2,1,2,2,2,3,3,3,3,2,2,1,1,2,0,0],
                       [2,2,3,1,2,2,3,3,3,3,1,2,1,1,3,0,0],
                       [2,2,2,2,0,2,2,2,2,2,1,2,1,0,2,0,0],
                       [2,2,2,2,2,0,1,1,1,1,1,2,1,1,2,0,0],
                       [2,2,2,3,2,2,0,2,1,1,1,2,1,0,2,0,0],
                       [2,2,2,2,2,1,0,0,0,0,1,2,1,0,2,0,0],
                       [2,2,2,2,2,2,1,1,0,2,2,2,1,0,2,0,0],
                       [2,2,2,2,2,2,1,1,2,0,2,2,1,0,2,0,0],
                       [2,2,2,2,2,2,2,2,2,2,0,2,1,0,2,0,0],
                       [2,2,2,2,2,2,2,2,1,1,0,0,1,0,2,0,0],
                       [2,2,2,2,2,2,0,0,0,0,0,2,0,0,2,0,0],
                       [2,2,2,2,2,2,2,2,2,2,1,2,1,0,1,0,0],
                       [2,2,3,3,3,3,3,3,2,2,0,2,1,0,0,0,0],
                       [2,2,2,3,2,0,0,0,0,0,0,0,0,0,0,0,0],  #molti 0 perchè se si siede non ha senso rialzarsi subito
                       [2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0]   #molti 0 perchè se si siede non ha senso rialzarsi subito
                       ])

# 3)La colonna del 13RotationFootLleg è data tutta da 1 (o 0) perchè se il robot fa quel movimento si gira del tutto. Non so se ha senso
#  usare sta mossa se poi non abbiamo il modo di farlo ritornare a guardare in avanti. Come per il punto 2) ho
# i punteggi da usare se secondo vai vanno inclusi, fatemi sapere.
        
# 4) In realtà avevo creato anche una matrice che va a sostituire quella base, se:
#    - Si ripetono gli stessi movimenti di mano più di 2 volte (perchè alcuni ci stanno: tipo fare 1-1 nel NAO
#        assomiglia a fare "come on" con la mano, ma non si può fare all'eterno)
#    - il NAO fa movimenti diversi ma comunque sempre o delle braccia o delle gambe più di 2-3 volte. Ad esempio
#      se fa 11stand-3doublMovement-5unionArms-2rightArm-5unionArms oppure 7moveForward-8moveBackward-7moveForward-9diagonalLeft-7moveForward
 
#  Ma ora che ci penso magari ha più senso metterlo nei constrains. Ditemi voi se devo creare la matrice o no.
