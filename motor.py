import pyrosim.pyrosim as pyrosim
import pybullet as p

import numpy as np

class MOTOR:
    def __init__(self, jointName, bodyId):
        self.jointName = jointName
        self.bodyId = bodyId
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.vector = [np.pi/4, 100, 0]

    def Set_Value(self, value):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = self.bodyId,
                jointName = self.jointName,
                controlMode = p.POSITION_CONTROL,
                targetPosition = value,#self.vector[0] * np.sin(self.vector[1] * value + self.vector[2]),
                maxForce = 50)
