from world import WORLD
from robot import ROBOT

import pybullet as p
import pybullet_data

import time

class SIMULATION:
    def __init__(self, demo):
        if demo:
            self.physicsClient = p.connect(p.GUI)
        else:
            self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD(p)
        self.robot = ROBOT(p, 2, 2)

    def Demo(self, n):
        while True:
            p.stepSimulation()
            self.robot.Sense(0)
            self.robot.Think(0)
            self.robot.Act(0)
            time.sleep(1.0/10000.0)

    def Run(self, n, penalty, onlyStraight):
        if penalty:
            penalty_total = 0
            penalty_counter = 0
        for i in range(n):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think(i)
            self.robot.Act(i)
            if penalty:
                if self.robot.nn.neurons['0'].Get_Value() == 1:
                    penalty_counter+=1
                    penalty_total+=0.5*(1/penalty_counter)
        
        fitness =  self.robot.Get_Fitness(onlyStraight)
        if penalty:
            fitness-=penalty_total
        p.disconnect()
        return fitness
