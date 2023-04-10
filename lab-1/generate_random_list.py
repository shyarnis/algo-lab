import random

def random_list(n):
    '''Return random list of size n with random number between 1 and n'''
    random_list = []
    for _ in range(n):
        random_int = random.randint(1, n)
        random_list.append(random_int)
    return random_list

def rand_list(n):
    '''Return random list of size n with random number between 1 and n'''
    return [random.randint(1, n) for _ in range(n)]

