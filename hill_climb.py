from simulate import eval, demo
import random

def step(gene, fitness):
    s = random.randint(0, 8)
    m = random.randint(0, 7)
    old_gene = gene[m][s]
    gene[m][s] = random.random() * 2 - 1
    new_fitness = eval(gene, True, True)
    if new_fitness > fitness:
        fitness = new_fitness
    else:
        gene[m][s] = old_gene
    return gene, fitness

gene = [[random.random() - 0.5 for _ in range(9)] for _ in range(8)]

fitness = eval(gene, True, True)
for i in range(1000):
    gene, fitness = step(gene, fitness)
    print(i, fitness)

demo()