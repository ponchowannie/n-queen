import random

class Individual:
    def __init__(self):
        self.list = [0]*8
        self.score = 0
        self.rand()
    
    def rand(self):
        for i in range(8):
           self.list[i] = random.randint(0,7)

def attacking(x1, y1, x2, y2):
    if y1 == y2:
        return 1
    
    d1, d2 = x1, y1
    while (d1 < 7) and (d2 < 7):
        d1 += 1
        d2 += 1
        if (d1==x2) and (d2==y2):
            return 1
        
    d1, d2 = x1, y1
    while (d1 < 7) and (d2 > 0):
        d1 += 1
        d2 -= 1
        if (d1==x2) and (d2==y2):
            return 1
    return 0

def score():
    smax = 0 
    for i in range(POP_MAX):
        personal_score = 0
        for j in range(8):
            for k in range(j+1, 8):
                if not (attacking(j, population[i].list[j], k, population[i].list[k])):
                    personal_score += 1

        population[i].score = personal_score
        smax = max(personal_score, smax)
    return smax    

def reproduce():
    sorted_population = sorted(population, key=lambda x: x.score, reverse=True)
    parent1 = sorted_population[0]
    parent2 = sorted_population[1]
    for i in range(POP_MAX):
        CUTOFF = random.randint(1,7)
        for j in range(CUTOFF):
            population[i].list[j] = parent1.list[j]
        for j in range(CUTOFF, 8):
            population[i].list[j] = parent2.list[j]

def mutate():
    for i in range(random.randint(1,2)):
        population[i].list[random.randint(0,7)] = random.randint(0,7)

def print_pop():
    for i in range(POP_MAX):
        print(f'{population[i].list}, Score: {population[i].score}')
    print('\n ---------------- \n')

def print_queen():
    for _ in range(POP_MAX):
        if population[_].score == 28:
            print_board(population[_].list)

def print_board(rows):
    n = len(rows)
    for row in range(n):
        line = "|"
        for col in range(n):
            if rows[col] == row:
                line += " ♕ |"
            else:
                line += "   |"
        print("+---+---+---+---+---+---+---+---+")
        print(line)
    print("+---+---+---+---+---+---+---+---+")

def initialize_pop():
    for _ in range(4):
        dummy = Individual()
        population.append(dummy)
        print(population[_].list)

def main():
    initialize_pop()
    itr = 0
    while (score() != 28):
        itr += 1
        print(f'Iteration {itr}')
        print_pop()
        reproduce()
        mutate()
    
    print_pop()
    print(f'Found Solution at Iteration: {itr}')
    print_queen()

population = []
POP_MAX = 4
random.seed(3)
main()