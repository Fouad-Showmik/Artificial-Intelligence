import random


# Genetic Algorithm Functions
def fitness(selected_batsmen, average_runs):
    #return sum(avg_run for selected, avg_run in zip(selected_batsmen, average_runs) if selected)
    total_runs = 0
    for selected, avg_run in zip(selected_batsmen, average_runs):
        if selected:
            total_runs += avg_run
    return total_runs

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(selected_batsmen, mutation_rate=0.2):
    mutated_batsmen = selected_batsmen.copy()
    for i in range(len(mutated_batsmen)):
        if random.random() < mutation_rate:
            mutated_batsmen[i] = 1 - mutated_batsmen[i]  # Flip the bit
    return mutated_batsmen


def generate_population(population_size, num_batsmen):
    population = []

    for _ in range(population_size):
        selected_batsmen = []
        for _ in range(num_batsmen):
            random_bit = random.randint(0, 1)
            selected_batsmen.append(random_bit)
        population.append(selected_batsmen)

    return population



# Open the input file
with open('task.txt', 'r') as file:
    # Read the first line to get the number of batsmen and the target score
    num_batsmen, target_score = map(int, file.readline().split())

    # Read the next lines to get the list of batsmen with their names and average scores
    batsmen_info = [list(map(str, line.split())) for line in file]

# Extract names and average_runs

names = []
for info in batsmen_info:
    batsman_name = info[0]
    names.append(batsman_name)

# Convert average runs to integers from batsmen_info
average_runs = []
for info in batsmen_info:
    batsman_avg = int(info[1])
    average_runs.append(batsman_avg)

# Model the solution as a binary array
length = num_batsmen

# Create initial population
pop_size = 500
population = generate_population(pop_size, length)

# Run genetic algorithm
num_generations = 1000
for gen in range(num_generations):

    # Calculate fitness
    fitness_scores = []
    for individual in population:
        individual_fitness = fitness(individual, average_runs)
        fitness_scores.append(individual_fitness)

    # Check if solution found
    if target_score in fitness_scores:
        index = fitness_scores.index(target_score)
        print(names)
        print("".join(map(str, population[index])))
        break

        # Select parents based on fitness
    parents = random.choices(population=population, weights=fitness_scores, k=int(pop_size / 2))

    # Create next generation
    next_generation = []
    for i in range(0, pop_size, 2):
        parent1 = parents[i]
        parent2 = parents[i + 1]
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        next_generation.append(child1)
        next_generation.append(child2)

    population = next_generation

if target_score not in fitness_scores:
    print(names)
    print(-1)
