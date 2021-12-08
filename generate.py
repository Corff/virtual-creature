import pyrosim.pyrosim as pyrosim

length, width, height = 1, 1, 1

def Create_World(): 
    pyrosim.Start_SDF("boxes.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-1.5, 1.5, 0.5], size=[length, width, height])
    pyrosim.End()

def Create_Body():
    pyrosim.Start_URDF("body.urdf")

    # Bodies
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[2, 1, 0.5])
    
    pyrosim.Send_Joint(name="Torso_FLT", parent="Torso", child="FLT", type="revolute", position="1 -0.5 1.25")
    pyrosim.Send_Cube(name="FLT", pos=[0, 0, -0.5], size=[0.15, 0.15, 0.5])
    pyrosim.Send_Joint(name="FLT_FLL", parent="FLT", child="FLL", type="revolute", position="0 0 -0.5")
    pyrosim.Send_Cube(name="FLL", pos=[0, 0, -0.5], size=[0.1, 0.1, 0.5])

    pyrosim.Send_Joint(name="Torso_FRT", parent="Torso", child="FRT", type="revolute", position="1 0.5 1.25")
    pyrosim.Send_Cube(name="FRT", pos=[0, 0, -0.5], size=[0.15, 0.15, 0.5])
    pyrosim.Send_Joint(name="FRT_FRL", parent="FRT", child="FRL", type="revolute", position="0 0 -0.5")
    pyrosim.Send_Cube(name="FRL", pos=[0, 0, -0.5], size=[0.1, 0.1, 0.5])
    
    pyrosim.Send_Joint(name="Torso_BLT", parent="Torso", child="BLT", type="revolute", position="-1 -0.5 1.25")
    pyrosim.Send_Cube(name="BLT", pos=[0, 0, -0.5], size=[0.15, 0.15, 0.5])
    pyrosim.Send_Joint(name="BLT_BLL", parent="BLT", child="BLL", type="revolute", position="0 0 -0.5")
    pyrosim.Send_Cube(name="BLL", pos=[0, 0, -0.5], size=[0.1, 0.1, 0.5])

    pyrosim.Send_Joint(name="Torso_BRT", parent="Torso", child="BRT", type="revolute", position="-1 0.5 1.25")
    pyrosim.Send_Cube(name="BRT", pos=[0, 0, -0.5], size=[0.15, 0.15, 0.5])
    pyrosim.Send_Joint(name="BRT_BRL", parent="BRT", child="BRL", type="revolute", position="0 0 -0.5")
    pyrosim.Send_Cube(name="BRL", pos=[0, 0, -0.5], size=[0.1, 0.1, 0.5])

    pyrosim.End()

def Create_Brain(genes):
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "FLT")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FLL")
    pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "FRT")
    pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "FRL")
    pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BLT")
    pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BLL")
    pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "BRT")
    pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "BRL")

    pyrosim.Send_Motor_Neuron(name = 9 , jointName = "Torso_FLT")
    pyrosim.Send_Motor_Neuron(name = 10 , jointName = "Torso_FRT")
    pyrosim.Send_Motor_Neuron(name = 11 , jointName = "Torso_BLT")
    pyrosim.Send_Motor_Neuron(name = 12 , jointName = "Torso_BRT")
    pyrosim.Send_Motor_Neuron(name = 13 , jointName = "FLT_FLL")
    pyrosim.Send_Motor_Neuron(name = 14 , jointName = "FRT_FRL")
    pyrosim.Send_Motor_Neuron(name = 15 , jointName = "BLT_BLL")
    pyrosim.Send_Motor_Neuron(name = 16 , jointName = "BRT_BRL")

    for s in range(8):
        for m in range(8):
            pyrosim.Send_Synapse(sourceNeuronName = s , targetNeuronName = m+9 , weight = genes[m][s])

    pyrosim.End()

if __name__ == "__main__":
    Create_Body()
    Create_Brain([[0.1 for _ in range(8)] for _ in range(8)])
