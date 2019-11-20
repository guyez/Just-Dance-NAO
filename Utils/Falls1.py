# -*- coding: cp1252 -*-
from RobotPositions import Rotation_handgun_object_1,Right_arm_2,Double_movement_3,Arms_opening_4,Union_arms_5
from RobotPositions import Crouch_6,Move_forward_7,Move_backward_8,Diagonal_left_9,Diagonal_right_10
from RobotPositions import Stand_11,Rotation_foot_RLeg_12,Rotation_foot_LLeg_13,StandInit_14,StandZero_15
from RobotPositions import Sit_16,SitRelax_17,Hello_18,Wipe_Forehead_19

listaMosse = [Rotation_handgun_object_1,Right_arm_2,Double_movement_3,Arms_opening_4,Union_arms_5,
Crouch_6,Move_forward_7,Move_backward_8,Diagonal_left_9,Diagonal_right_10,
Stand_11,Rotation_foot_RLeg_12,Rotation_foot_LLeg_13,StandInit_14,StandZero_15,
Sit_16,SitRelax_17,Hello_18,Wipe_Forehead_19]

Fall_A = [Crouch_6,Move_forward_7,Move_backward_8,Diagonal_left_9,Diagonal_right_10,
                   Stand_11,Rotation_foot_RLeg_12,Rotation_foot_LLeg_13,StandInit_14,StandZero_15,
                   Sit_16,SitRelax_17]

Fall_B = [Crouch_6,Stand_11,Rotation_foot_RLeg_12,Rotation_foot_LLeg_13,StandInit_14,StandZero_15,
                   Sit_16,SitRelax_17]

#Fall_B è un sottoinsieme di Fall_A



#I movimenti in Fall_A cadono durante:
# (k denota un elemento in Fall_B)
#  k-SitRelax_17-Move_forward_7- CADE - k
#  k-SitRelax_17-Move_backward_8- CADE - k
#  k-SitRelax_17-Diagonal_left_9- CADE - k
#  k-SitRelax_17-Diagonal_right_10- CADE - k

for k in range(0,len(Fall_A)):
    print("Inizio a provare le possibili mosse sucessive alla posizione: " + str(17) + "\n")
    for j in [6,7,8,9]:
            Fall_A[k].main("127.0.0.1",54233)
            listaMosse[16].main("127.0.0.1",54233)
            listaMosse[j].main("127.0.0.1",54233)
            print("Mossa: "+ str(j+1) + "\n")
    Fall_A[k].main("127.0.0.1",54233)

#I movimenti in Fall_B cadono durante i movimenti precedenti (quelli di Fall_A) e durante:
# (k denota un elemento in Fall_B)
#  k -Stand_11-Double_movement_3- CADE - k
#  k -StandZero_15-Double_movement_3- CADE - k

for k in range(0,len(Fall_B)):
    for i in [10,14]:
            print("Inizio a provare le possibili mosse sucessive alla posizione: " + str(i+1) + "\n")
            Fall_B[k].main("127.0.0.1",54233)
            listaMosse[i].main("127.0.0.1",54233)
            listaMosse[2].main("127.0.0.1",54233)
            print("Mossa: "+ str(2+1) + "\n")
Fall_B[k].main("127.0.0.1",54233)





