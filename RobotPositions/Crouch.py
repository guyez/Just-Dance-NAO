import sys
from naoqi import ALProxy

def main(robotIP, port):

	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.2, 2])
	keys.append([[0.0924662, [3, -0.0666667, 0], [3, 0.6, 0]], [0.00217341, [3, -0.6, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([0.2, 2])
	keys.append([[-0.00843369, [3, -0.0666667, 0], [3, 0.6, 0]], [-0.00843369, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([0.2, 2])
	keys.append([[-1.17695, [3, -0.0666667, 0], [3, 0.6, 0]], [-0.350757, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([0.2, 2])
	keys.append([[0.0765027, [3, -0.0666667, 0], [3, 0.6, 0]], [7.02661e-05, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([0.2, 2])
	keys.append([[-1.06675, [3, -0.0666667, 0], [3, 0.6, 0]], [-1.00995, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([0.2, 2])
	keys.append([[-0.80083, [3, -0.0666667, 0], [3, 0.6, 0]], [-1.38235, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([0.2, 2])
	keys.append([[0.00435016, [3, -0.0666667, 0], [3, 0.6, 0]], [0.244566, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([0.2, 2])
	keys.append([[-0.698006, [3, -0.0666667, 0], [3, 0.6, 0]], [-0.455433, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([0.2, 2])
	keys.append([[-0.0736321, [3, -0.0666667, 0], [3, 0.6, 0]], [-0.00173872, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([0.2, 2])
	keys.append([[-0.241026, [3, -0.0666667, 0], [3, 0.6, 0]], [-0.00543351, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([0.2, 2])
	keys.append([[2.10473, [3, -0.0666667, 0], [3, 0.6, 0]], [0.701287, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([0.2, 2])
	keys.append([[1.40499, [3, -0.0666667, 0], [3, 0.6, 0]], [1.40787, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([0.2, 2])
	keys.append([[0.16502, [3, -0.0666667, 0], [3, 0.6, 0]], [0.297676, [3, -0.6, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([0.2, 2])
	keys.append([[0.145304, [3, -0.0666667, 0], [3, 0.6, 0]], [0.0095022, [3, -0.6, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([0.2, 2])
	keys.append([[-1.17695, [3, -0.0666667, 0], [3, 0.6, 0]], [-0.350757, [3, -0.6, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([0.2, 2])
	keys.append([[-0.0765259, [3, -0.0666667, 0], [3, 0.6, 0]], [-7.02661e-05, [3, -0.6, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([0.2, 2])
	keys.append([[1.06668, [3, -0.0666667, 0], [3, 0.6, 0]], [1.00995, [3, -0.6, 0], [3, 0, 0]]])


	names.append("RElbowYaw")
	times.append([0.2, 2])
	keys.append([[0.80098, [3, -0.0666667, 0], [3, 0.6, 0]], [1.38235, [3, -0.6, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([0.2, 2])
	keys.append([[0.00435016, [3, -0.0666667, 0], [3, 0.6, 0]], [0.244566, [3, -0.6, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([0.2, 2])
	keys.append([[-0.698006, [3, -0.0666667, 0], [3, 0.6, 0]], [-0.455433, [3, -0.6, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([0.2, 2])
	keys.append([[0.0736349, [3, -0.0666667, 0], [3, 0.6, 0]], [0.00173872, [3, -0.6, 0], [3, 0, 0]]])

	names.append("RHipYawPitch")
	times.append([0.2, 2])
	keys.append([[-0.241026, [3, -0.0666667, 0], [3, 0.6, 0]], [-0.00543351, [3, -0.6, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([0.2, 2])
	keys.append([[2.10471, [3, -0.0666667, 0], [3, 0.6, 0]], [0.701287, [3, -0.6, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([0.2, 2])
	keys.append([[1.40501, [3, -0.0666667, 0], [3, 0.6, 0]], [1.40787, [3, -0.6, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([0.2, 2])
	keys.append([[-0.165122, [3, -0.0666667, 0], [3, 0.6, 0]], [-0.297676, [3, -0.6, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([0.2, 2])
	keys.append([[-0.147125, [3, -0.0666667, 0], [3, 0.6, 0]], [-0.0095022, [3, -0.6, 0], [3, 0, 0]]])

	try:
	  motion = ALProxy("ALMotion",robotIP,port)
	  motion.angleInterpolationBezier(names, times, keys)
	except BaseException, err:
	  print err

  
if __name__ == "__main__":

    robotIP = "127.0.0.1"#"192.168.11.3"

    port = 55691 #9559 # Insert NAO port


    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)