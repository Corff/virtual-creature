import pyrosim.pyrosim as pyrosim

import numpy as np

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName

    def Sense(self):
        return pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
