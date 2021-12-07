from motor import MOTOR
from sensor import SENSOR

import pybullet as p
import pyrosim.pyrosim as pyrosim

import numpy as np

class ROBOT:
    def __init__(self, p, s, m):
        self.motors = {}
        self.motorValues = np.linspace(-np.pi, np.pi, 10000)

        self.id = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prerpare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        self.sensorValues = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            self.sensorValues[linkName] = np.zeros(10000)

    def Prerpare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName, self.id)

    def Sense(self, i):
        for sensor in self.sensors:
            self.sensorValues[sensor][i] = self.sensors[sensor].Sense()

    def Act(self, i):
        for motor in self.motors:
            self.motors[motor].Set_Value(self.motorValues[i])
            
            
