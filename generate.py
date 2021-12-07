import pyrosim.pyrosim as pyrosim

length, width, height = 1, 1, 1

def Create_World(): 
    pyrosim.Start_SDF("boxes.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-1.5, 1.5, 0.5], size=[length, width, height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    # Bodies
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
    
    pyrosim.Send_Joint(name="Torso_FLeg", parent="Torso", child="FrontLeg", type="revolute", position="1 0.0 1")
    pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
    
    pyrosim.Send_Joint(name="Torso_BLeg", parent="Torso", child="BackLeg", type="revolute", position="2 0.0 1")
    pyrosim.Send_Cube(name="BackLeg", pos=[0.5, 0, -0.5], size=[length, width, height])

    pyrosim.End()

if __name__ == "__main__":
    Create_World()
    Create_Robot()

