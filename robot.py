from motor import MOTOR
from sensor import SENSOR

import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

import numpy as np

class ROBOT:
    def __init__(self, p, s, m):
        self.motors = {}
        self.motorValues = np.linspace(-np.pi, np.pi, 10000)
        self.id = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
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

    def Think(self, i):
        self.nn.Update()

    def Act(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                self.motors[jointName].Set_Value(desiredAngle)  

    def Get_Fitness(self):
        pos = p.getLinkState(self.id,0)[0]
        return ((pos[0] ** 2) + (pos[1] ** 2)) ** 0.5
