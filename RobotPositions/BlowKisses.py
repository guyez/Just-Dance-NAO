import sys
import time
from naoqi import ALProxy


def main(robotIP, port):
	names = list()
	times = list()
	keys = list()
	
	

	try:
		ttsProxy = ALProxy("ALTextToSpeech",robotIP,port)
	except Exception,e:
		print("Could not create a proxy to ALTextToSpeech")
	
		ttsProxy.say("Blow kisses!")

	names.append("HeadPitch")
	times.append([0.2, 0.6, 1.4, 2.04, 2.4, 3.2, 3.84, 4.2])
	keys.append([[-0.0046272, [3, -0.0666667, 0], [3, 0.133333, 0]], [-0.01078, [3, -0.133333, 0], [3, 0.266667, 0]], [-0.01078, [3, -0.266667, 0], [3, 0.213333, 0]], [-0.112024, [3, -0.213333, 0], [3, 0.12, 0]], [-0.01078, [3, -0.12, 0], [3, 0.266667, 0]], [-0.01078, [3, -0.266667, 0], [3, 0.213333, 0]], [-0.112024, [3, -0.213333, 0], [3, 0.12, 0]], [-0.00409839, [3, -0.12, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([0.2, 0.6, 1.4, 2.04, 2.4, 3.2, 3.84, 4.2])
	keys.append([[0.00648624, [3, -0.0666667, 0], [3, 0.133333, 0]], [0.010696, [3, -0.133333, 0], [3, 0.266667, 0]], [0.010696, [3, -0.266667, 0], [3, 0.213333, 0]], [0.338973, [3, -0.213333, 0], [3, 0.12, 0]], [0.010696, [3, -0.12, 0], [3, 0.266667, 0]], [0.010696, [3, -0.266667, 0], [3, 0.213333, 0]], [0.338973, [3, -0.213333, 0], [3, 0.12, 0]], [0.00919698, [3, -0.12, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([0.2, 0.72, 2.52, 4.2])
	keys.append([[-0.35, [3, -0.0666667, 0], [3, 0.173333, 0]], [-0.359129, [3, -0.173333, 0], [3, 0.6, 0]], [-0.359129, [3, -0.6, 0], [3, 0.56, 0]], [-0.35, [3, -0.56, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([0.2, 0.72, 2.52, 4.2])
	keys.append([[-0.00902358, [3, -0.0666667, 0], [3, 0.173333, 0]], [-0.0797476, [3, -0.173333, 0], [3, 0.6, 0]], [-0.0797476, [3, -0.6, 0], [3, 0.56, 0]], [0, [3, -0.56, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([0.2, 0.6, 1, 1.4, 1.72, 2.04, 2.4, 2.8, 3.2, 3.52, 3.84, 4.2])
	keys.append([[-1.01789, [3, -0.0666667, 0], [3, 0.133333, 0]], [-1.56617, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.658043, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.56617, [3, -0.133333, 0], [3, 0.106667, 0]], [-0.658043, [3, -0.106667, -0.210158], [3, 0.106667, 0.210158]], [-0.305225, [3, -0.106667, 0], [3, 0.12, 0]], [-1.56617, [3, -0.12, 0], [3, 0.133333, 0]], [-0.658043, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.56617, [3, -0.133333, 0], [3, 0.106667, 0]], [-0.658043, [3, -0.106667, -0.210158], [3, 0.106667, 0.210158]], [-0.305225, [3, -0.106667, 0], [3, 0.12, 0]], [-1.00727, [3, -0.12, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([0.2, 0.6, 1, 1.4, 1.72, 2.04, 2.4, 2.8, 3.2, 3.52, 3.84, 4.2])
	keys.append([[-1.38905, [3, -0.0666667, 0], [3, 0.133333, 0]], [-0.624379, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.26866, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.624379, [3, -0.133333, 0], [3, 0.106667, 0]], [-1.26866, [3, -0.106667, 0.242373], [3, 0.106667, -0.242373]], [-2.07862, [3, -0.106667, 0], [3, 0.12, 0]], [-0.624379, [3, -0.12, 0], [3, 0.133333, 0]], [-1.26866, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.624379, [3, -0.133333, 0], [3, 0.106667, 0]], [-1.26866, [3, -0.106667, 0.242373], [3, 0.106667, -0.242373]], [-2.07862, [3, -0.106667, 0], [3, 0.12, 0]], [-1.3896, [3, -0.12, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([0.2, 0.6, 1, 1.4, 1.72, 2.04, 2.4, 2.8, 3.2, 3.52, 3.84, 4.2])
	keys.append([[0.252174, [3, -0.0666667, 0], [3, 0.133333, 0]], [0.917114, [3, -0.133333, -0.082886], [3, 0.133333, 0.082886]], [1, [3, -0.133333, 0], [3, 0.133333, 0]], [0.917114, [3, -0.133333, 0], [3, 0.106667, 0]], [1, [3, -0.106667, 0], [3, 0.106667, 0]], [0.997478, [3, -0.106667, 0.00252199], [3, 0.12, -0.00283724]], [0.917114, [3, -0.12, 0], [3, 0.133333, 0]], [1, [3, -0.133333, 0], [3, 0.133333, 0]], [0.917114, [3, -0.133333, 0], [3, 0.106667, 0]], [1, [3, -0.106667, 0], [3, 0.106667, 0]], [0.997478, [3, -0.106667, 0.00252199], [3, 0.12, -0.00283724]], [0.25, [3, -0.12, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([0.2, 0.72, 2.52, 4.2])
	keys.append([[-0.45, [3, -0.0666667, 0], [3, 0.173333, 0]], [-0.27941, [3, -0.173333, 0], [3, 0.6, 0]], [-0.27941, [3, -0.6, 0], [3, 0.56, 0]], [-0.45, [3, -0.56, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([0.2, 0.72, 2.52, 4.2])
	keys.append([[0.00159365, [3, -0.0666667, 0], [3, 0.173333, 0]], [0.168548, [3, -0.173333, 0], [3, 0.6, 0]], [0.168548, [3, -0.6, 0], [3, 0.56, 0]], [0.00837686, [3, -0.56, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([0.2, 0.72, 2.52, 4.2])
	keys.append([[-0.00420801, [3, -0.0666667, 0], [3, 0.173333, 0]], [-0.170318, [3, -0.173333, 0], [3, 0.6, 0]], [-0.170318, [3, -0.6, 0], [3, 0.56, 0]], [-0.00409839, [3, -0.56, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([0.2, 0.72, 2.52, 4.2])
	keys.append([[0.699999, [3, -0.0666667, 0], [3, 0.173333, 0]], [0.680776, [3, -0.173333, 0], [3, 0.6, 0]], [0.680776, [3, -0.6, 0], [3, 0.56, 0]], [0.7, [3, -0.56, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([0.2, 0.6, 1, 1.4, 1.72, 2.04, 2.4, 2.8, 3.2, 3.52, 3.84, 4.2])
	keys.append([[1.39733, [3, -0.0666667, 0], [3, 0.133333, 0]], [0.496974, [3, -0.133333, 0.195313], [3, 0.133333, -0.195313]], [0.225456, [3, -0.133333, 0], [3, 0.133333, 0]], [0.496974, [3, -0.133333, 0], [3, 0.106667, 0]], [0.225456, [3, -0.106667, 0], [3, 0.106667, 0]], [0.4034, [3, -0.106667, -0.042591], [3, 0.12, 0.0479148]], [0.496974, [3, -0.12, 0], [3, 0.133333, 0]], [0.225456, [3, -0.133333, 0], [3, 0.133333, 0]], [0.496974, [3, -0.133333, 0], [3, 0.106667, 0]], [0.225456, [3, -0.106667, 0], [3, 0.106667, 0]], [0.4034, [3, -0.106667, -0.177943], [3, 0.12, 0.200186]], [1.40275, [3, -0.12, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([0.2, 0.6, 1, 1.4, 1.72, 2.04, 2.4, 2.8, 3.2, 3.52, 3.84, 4.2])
	keys.append([[0.297991, [3, -0.0666667, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.133333, 0]], [0.05058, [3, -0.133333, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.106667, 0]], [0.05058, [3, -0.106667, -0.05058], [3, 0.106667, 0.05058]], [0.77923, [3, -0.106667, 0], [3, 0.12, 0]], [0, [3, -0.12, 0], [3, 0.133333, 0]], [0.05058, [3, -0.133333, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0.106667, 0]], [0.05058, [3, -0.106667, -0.05058], [3, 0.106667, 0.05058]], [0.77923, [3, -0.106667, 0], [3, 0.12, 0]], [0.294329, [3, -0.12, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([0.2, 0.6, 1, 1.4, 1.72, 2.04, 2.4, 2.8, 3.2, 3.52, 3.84, 4.2])
	keys.append([[-0.00289152, [3, -0.0666667, 0], [3, 0.133333, 0]], [-1.00941, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.00941, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.00941, [3, -0.133333, 0], [3, 0.106667, 0]], [-1.00941, [3, -0.106667, 0], [3, 0.106667, 0]], [-1.01095, [3, -0.106667, 0], [3, 0.12, 0]], [-1.00941, [3, -0.12, 0], [3, 0.133333, 0]], [-1.00941, [3, -0.133333, 0], [3, 0.133333, 0]], [-1.00941, [3, -0.133333, 0], [3, 0.106667, 0]], [-1.00941, [3, -0.106667, 0], [3, 0.106667, 0]], [-1.01095, [3, -0.106667, 0], [3, 0.12, 0]], [0.00504533, [3, -0.12, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([0.2, 0.72, 2.52, 4.2])
	keys.append([[-0.35, [3, -0.0666667, 0], [3, 0.173333, 0]], [-0.184108, [3, -0.173333, 0], [3, 0.6, 0]], [-0.184108, [3, -0.6, 0], [3, 0.56, 0]], [-0.35, [3, -0.56, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([0.2, 0.72, 2.52, 4.2])
	keys.append([[0.00303459, [3, -0.0666667, 0], [3, 0.173333, 0]], [0.0675357, [3, -0.173333, 0], [3, 0.6, 0]], [0.0675357, [3, -0.6, 0], [3, 0.56, 0]], [0, [3, -0.56, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([0.2, 0.6, 1, 1.4, 1.72, 2.04, 2.4, 2.8, 3.2, 3.52, 3.84, 4.2])
	keys.append([[1.0023, [3, -0.0666667, 0], [3, 0.133333, 0]], [0.504728, [3, -0.133333, 0.0736319], [3, 0.133333, -0.0736319]], [0.431096, [3, -0.133333, 0], [3, 0.133333, 0]], [0.504728, [3, -0.133333, 0], [3, 0.106667, 0]], [0.431096, [3, -0.106667, 0], [3, 0.106667, 0]], [0.596768, [3, -0.106667, 0], [3, 0.12, 0]], [0.504728, [3, -0.12, 0.0261587], [3, 0.133333, -0.0290652]], [0.431096, [3, -0.133333, 0], [3, 0.133333, 0]], [0.504728, [3, -0.133333, 0], [3, 0.106667, 0]], [0.431096, [3, -0.106667, 0], [3, 0.106667, 0]], [0.596768, [3, -0.106667, -0.0903796], [3, 0.12, 0.101677]], [1.00727, [3, -0.12, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([0.2, 0.6, 1, 1.4, 1.72, 2.04, 2.4, 2.8, 3.2, 3.52, 3.84, 4.2])
	keys.append([[1.38723, [3, -0.0666667, 0], [3, 0.133333, 0]], [0.42641, [3, -0.133333, 0.0153397], [3, 0.133333, -0.0153397]], [0.41107, [3, -0.133333, 0], [3, 0.133333, 0]], [0.42641, [3, -0.133333, 0], [3, 0.106667, 0]], [0.41107, [3, -0.106667, 0.0153397], [3, 0.106667, -0.0153397]], [0.196309, [3, -0.106667, 0], [3, 0.12, 0]], [0.42641, [3, -0.12, 0], [3, 0.133333, 0]], [0.41107, [3, -0.133333, 0], [3, 0.133333, 0]], [0.42641, [3, -0.133333, 0], [3, 0.106667, 0]], [0.41107, [3, -0.106667, 0.0153397], [3, 0.106667, -0.0153397]], [0.196309, [3, -0.106667, 0], [3, 0.12, 0]], [1.3896, [3, -0.12, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([0.2, 0.6, 1.4, 2.04, 2.4, 3.2, 3.84, 4.2])
	keys.append([[0.251241, [3, -0.0666667, 0], [3, 0.133333, 0]], [0.630909, [3, -0.133333, 0], [3, 0.266667, 0]], [0.630909, [3, -0.266667, 0], [3, 0.213333, 0]], [0.572727, [3, -0.213333, 0], [3, 0.12, 0]], [0.630909, [3, -0.12, 0], [3, 0.266667, 0]], [0.630909, [3, -0.266667, 0], [3, 0.213333, 0]], [0.572727, [3, -0.213333, 0.058182], [3, 0.12, -0.0327274]], [0.25, [3, -0.12, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([0.2, 0.72, 2.52, 4.2])
	keys.append([[-0.45, [3, -0.0666667, 0], [3, 0.173333, 0]], [-0.336004, [3, -0.173333, 0], [3, 0.6, 0]], [-0.336004, [3, -0.6, 0], [3, 0.56, 0]], [-0.45, [3, -0.56, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([0.2, 0.72, 2.52, 4.2])
	keys.append([[-0.00288084, [3, -0.0666667, 0], [3, 0.173333, 0]], [0.0015544, [3, -0.173333, 0], [3, 0.6, 0]], [0.0015544, [3, -0.6, 0], [3, 0.56, 0]], [-0.00837686, [3, -0.56, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([0.2, 0.72, 2.52, 4.2])
	keys.append([[0.699999, [3, -0.0666667, 0], [3, 0.173333, 0]], [0.556428, [3, -0.173333, 0], [3, 0.6, 0]], [0.556428, [3, -0.6, 0], [3, 0.56, 0]], [0.7, [3, -0.56, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([0.2, 0.6, 1, 1.4, 1.72, 2.04, 2.4, 2.8, 3.2, 3.52, 3.84, 4.2])
	keys.append([[1.39931, [3, -0.0666667, 0], [3, 0.133333, 0]], [1.14441, [3, -0.133333, 0.0352819], [3, 0.133333, -0.0352819]], [1.10912, [3, -0.133333, 0], [3, 0.133333, 0]], [1.14441, [3, -0.133333, 0], [3, 0.106667, 0]], [1.10912, [3, -0.106667, 0], [3, 0.106667, 0]], [1.27173, [3, -0.106667, 0], [3, 0.12, 0]], [1.14441, [3, -0.12, 0.0256743], [3, 0.133333, -0.028527]], [1.10912, [3, -0.133333, 0], [3, 0.133333, 0]], [1.14441, [3, -0.133333, 0], [3, 0.106667, 0]], [1.10912, [3, -0.106667, 0], [3, 0.106667, 0]], [1.27173, [3, -0.106667, -0.0460592], [3, 0.12, 0.0518166]], [1.40275, [3, -0.12, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([0.2, 0.6, 1, 1.4, 1.72, 2.04, 2.4, 2.8, 3.2, 3.52, 3.84, 4.2])
	keys.append([[-0.299256, [3, -0.0666667, 0], [3, 0.133333, 0]], [-0.271559, [3, -0.133333, -0.0076841], [3, 0.133333, 0.0076841]], [-0.253151, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.271559, [3, -0.133333, 0], [3, 0.106667, 0]], [-0.253151, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.579894, [3, -0.106667, 0], [3, 0.12, 0]], [-0.271559, [3, -0.12, -0.0165672], [3, 0.133333, 0.018408]], [-0.253151, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.271559, [3, -0.133333, 0], [3, 0.106667, 0]], [-0.253151, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.579894, [3, -0.106667, 0], [3, 0.12, 0]], [-0.294329, [3, -0.12, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([0.2, 0.6, 1.4, 2.04, 2.4, 3.2, 3.84, 4.2])
	keys.append([[0.00274628, [3, -0.0666667, 0], [3, 0.133333, 0]], [0.958708, [3, -0.133333, 0], [3, 0.266667, 0]], [0.958708, [3, -0.266667, 0], [3, 0.213333, 0]], [0.944902, [3, -0.213333, 0], [3, 0.12, 0]], [0.958708, [3, -0.12, 0], [3, 0.266667, 0]], [0.958708, [3, -0.266667, 0], [3, 0.213333, 0]], [0.944902, [3, -0.213333, 0.0138056], [3, 0.12, -0.00776563]], [0.00504533, [3, -0.12, 0], [3, 0, 0]]])

	try:
	  motion = ALProxy("ALMotion",robotIP,port)
	  motion.angleInterpolationBezier(names, times, keys)
	except BaseException, err:
	  print err
  
if __name__ == "__main__":

    robotIP = "127.0.0.1"#"192.168.11.3"

    port = 55650 #9559 # Insert NAO port


    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)
