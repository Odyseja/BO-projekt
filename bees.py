import random

def fitness_function(solution_array):
    return 0

def create_random_bee(array):
    copy_array = array[:]       #array are passed by reference 
    random.shuffle(copy_array)  #operation on array, returns None
    return copy_array

def create_neigh_bee(site, patch_size):
    copy_array = site[:]
    for i in range(int(patch_size)):
        i, j = random.randint(0, len(site)), random.randint(0, len(site))
        copy_array[i], copy_array[j] = copy_array[j], copy_array[i] #change position of two elements
    return copy_array

def evaluate_population(population):
    fitness = map(fitness_function, population)
    fitness_population = zip(fitness, population)
    fitness_population.sort(key=lambda x: x[0])
    return list(map(lambda x: x[1], fitness_population))

def select_best_sites(population, sites_num):
    return evaluate_population(population)[:sites_num]

def get_best_solution(population):
    return evaluate_population(population)[0]

def initialize_population(bees_num, search_space):
    return [create_random_bee(search_space) for i in xrange(bees_num)]


def search(max_gens, search_space, num_bees, num_sites, elite_sites, patch_size, elite_bees, other_bees, patch_decrease_factor=0.95):
    """ Search for the best solution with the bees algorithm
    Args:
        max_gens: maximal number of generations
        search_space: array of image sizes
        num_bees: number of bees
        num_sites: number of selected best sides
        elite_sites: number of elite sites, where the most bees goes
        patch_size: size of how far the neighbor will be searched
        elite_bees: number of elite bees
        other_bees: number of other bees
        patch_decrease_factor: decreasing factor of patch in every iteration
    Returns:
        tuple of the best solution and best solution history
    """
    bee_best = None
    patch = patch_size
    iteration = 0
    fitness_history = []
    population = initialize_population(num_bees, search_space)
    while iteration < max_gens and fitness_history[-1] > 0:
        bee_best = get_best_solution(population)
        fitness_history.append(fitness_function(bee_best))

        next_generation = []
        patch = patch_size * patch_decrease_factor
        sites_best = select_best_sites(population, num_sites)
        site_num = 0
        for site in sites_best:
            recruited_bees = []
            if site_num < elite_sites:
                recruited_bees = elite_bees
            else:
                recruited_bees = other_bees

            neighborhood = []
            for i in xrange(recruited_bees):
                neighborhood.append(create_neigh_bee(site, patch))
            next_generation.append(get_best_solution(neighborhood))
        
        for i in range(num_bees - num_sites):
            next_generation.append(create_random_bee(search_space))
        population = next_generation
        iteration += 1

    return bee_best, fitness_history



