class WORLD:
    def __init__(self, p):
        self.p = p
        self.p.loadURDF("plane.urdf")