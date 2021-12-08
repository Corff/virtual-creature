from simulation import SIMULATION
from generate import Create_Brain

def eval(genes):
	Create_Brain(genes)
	sim = SIMULATION()
	return sim.Run(2500)

if __name__ == "__main__":
	eval([[0.1 for _ in range(8)] for _ in range(8)])