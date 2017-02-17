from sys import exit
from scipy import stats
import math

class Island(object):

    def __init__(self, starting_point, island_range):
        self.current_point = starting_point
        self.island_range = island_range

    def direction(self):
        if stats.bernoulli.rvs(0.5, size = 1)[0]:
            direction = 'east'
        else:
            direction = 'west'
        return direction

    def next_hop(self):
        next_direction = self.direction()
        if next_direction == 'west' and (self.current_point + 1 <= self.island_range[1]):
            self.current_point += 1
        elif next_direction == 'west':
            self.current_point = self.current_point
        elif (self.current_point - 1) >= self.island_range[0]:
            p_move = (self.current_point - 1)/self.current_point
            spinner = stats.uniform.rvs(size = 1)
            if spinner < p_move:
                self.current_point -= 1
            else:
                self.current_point = self.current_point
        else:
            self.current_point = self.current_point



class Map(object):

    chain = {}

    def __init__(self, n_islands, start_point):
        self.n_islands = n_islands
        self.start_point = start_point
        # self.island_chain = range(1,n_islands)
        self.current_island = Island(start_point, [1,self.n_islands])
        for i in range(1,n_islands+1):
            self.chain[i] = 0
            if i == start_point:
                self.chain[i] += 1



    def print_histogram(self, iteration_number):
        """
        prints a scaled histogram of the distributions generated
        """
        print("Iteration %d complete. Here is the distribution:" % iteration_number)
        for key in self.chain:
            print(key, ": ", "*" * math.floor(100*self.chain[key]/iteration_number)),
        print('\n\n')

    def conversation(self):
        pass
        #1) The Pit - Body, De'Angelo
        # 2) The Tower - Stikum and Webe
        # 3) City Hall -
        # 4) Little Johnnies - The Greeks
        # 5) Marlo's Court


    def simulate(self, sim_iterations=5000):
        for i in range(1, sim_iterations):
            self.current_island.next_hop()
            self.chain[self.current_island.current_point] += 1
            if i % 100 == 0:
                self.print_histogram(i)

m = Map(5, 3)
m.simulate()
