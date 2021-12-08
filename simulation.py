from world import WORLD
from robot import ROBOT

import pybullet as p
import pybullet_data

import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD(p)
        self.robot = ROBOT(p, 2, 2)

    def Demo(self, n):
        for i in range(n):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think(i)
            self.robot.Act(i)
            time.sleep(1.0/3000.0)

    def Run(self, n):
        for i in range(n):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think(i)
            self.robot.Act(i)
        
        return self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()