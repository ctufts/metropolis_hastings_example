from sys import exit
from scipy import stats
import math


class Engine(object):

    def direction(self):
        if stats.bernoulli.rvs(0.5, size = 1)[0]:
            direction = 'east'
        else:
            direction = 'west'
        return direction

    def next_hop(self, current_point, island_range):
        next_direction = self.direction()
        if next_direction == 'west' and (current_point + 1 <= island_range[1]):
            current_point += 1
        elif next_direction == 'west':
            current_point = current_point
        elif (current_point - 1) >= island_range[0]:
            p_move = (current_point - 1)/current_point
            spinner = stats.uniform.rvs(size = 1)
            if spinner < p_move:
                current_point -= 1
            else:
                current_point = current_point
        else:
            current_point = current_point

        return current_point

class Politician(object):

    quotes = {
        "move": "Shiiiiiiiiiiiiiiiiiiiit, warm up the car Day-Day. We need to collect our money from : ",
        "stay": "Better lay low, Lt. Daniels is out there. We can wait it out here: "
    }

    def __init__(self, starting_point, island_range):
        self.previous_point = starting_point
        self.current_point = starting_point
        self.island_range = island_range

    def speak(self):
        if(self.previous_point != self.current_point):
            return(Politician.quotes["move"])
        else:
            return(Politician.quotes["stay"])



class Map(object):


    bmore = {
        1:"The Pit",
        2:"The Tower",
        3:"City Hall",
        4:"Little Johnnies",
        5:"Marlo's Court"
    }

    n_islands = len(bmore)
    start_point = 3

    def __init__(self):
        self.engine = Engine()
        self.chain = {}
        # self.island_chain = range(1,n_islands)
        self.clay = Politician(Map.start_point, [1,Map.n_islands])
        for i in range(1,Map.n_islands+1):
            self.chain[i] = 0
            if i == Map.start_point:
                self.chain[i] += 1



    def print_histogram(self, iteration_number):
        """
        prints a scaled histogram of the distributions generated
        """
        print("Iteration %d complete. Here is the distribution:" % iteration_number)
        for key in self.chain:
            print( "*" * math.floor(100*self.chain[key]/iteration_number),":", Map.bmore[key]),
        print('\n\n')




    def simulate(self, sim_iterations=500):
        for i in range(1, sim_iterations):

            self.clay.previous_point = self.clay.current_point
            self.clay.current_point = self.engine.next_hop(self.clay.current_point,
                                                            self.clay.island_range)
            self.chain[self.clay.current_point] += 1
            print(self.clay.speak() + self.bmore[self.clay.current_point])
            if i % 100 == 0:
                self.print_histogram(i)

m = Map()
m.simulate()
