from simulate import eval, demo
import random

def step(gene, fitness):
    s = random.randint(0, 8)
    m = random.randint(0, 7)
    old_gene = gene[m][s]
    gene[m][s] = random.random() * 2 - 1
    new_fitness = eval(gene)
    if new_fitness > fitness:
        fitness = new_fitness
    else:
        gene[m][s] = old_gene
    return gene, fitness

best_gene = []
best_fitness = 0

for n in range(100):
    gene = [[random.random() - 0.5 for _ in range(9)] for _ in range(8)]
    fitness = eval(gene)
    for i in range(100):
        gene, fitness = step(gene, fitness)
        print(n, i, fitness, end='\r')

    if fitness > best_fitness:
        best_gene = gene
        best_fitness = fitness
    
    print(n, best_fitness, fitness)

print(gene)
demo()