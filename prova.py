from RobotPositions import Rotation_handgun_object_1,Right_arm_2,Double_movement_3,Arms_opening_4,Union_arms_5
from RobotPositions import Crouch_6,Move_forward_7,Move_backward_8,Diagonal_left_9,Diagonal_right_10
from RobotPositions import Stand_11,Rotation_foot_RLeg_12,Rotation_foot_LLeg_13,StandInit_14,StandZero_15
from RobotPositions import Sit_16,SitRelax_17

listaMosse = [Rotation_handgun_object_1,Right_arm_2,Double_movement_3,Arms_opening_4,Union_arms_5,
Crouch_6,Move_forward_7,Move_backward_8,Diagonal_left_9,Diagonal_right_10,
Stand_11,Rotation_foot_RLeg_12,Rotation_foot_LLeg_13,StandInit_14,StandZero_15,
Sit_16,SitRelax_17]

for i in listaMosse:
	print(i)
	for j in listaMosse:
		i.main("127.0.0.1",51616)
		j.main("127.0.0.1",51616)
		print(j)
	
	
