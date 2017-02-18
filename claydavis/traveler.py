from sys import exit
from scipy import stats
import math
import random


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

    stay_quotes = [
        "Better lay low, Lt. Daniels is out there. We can wait it out here: ",
        """Because if some federal mothafucker comes walkin' through the door,
        I say hey, it's all in the game!
        But a city police, Baltimore City, Hell Naaaw, can't be happenin'
         because I know I done raised too much goddamn money for the Mayor
          and his ticket! Hell Naaaw, aint no soul in the world that fuckin' ungrateful! """,
        """I know you don't wanna know, but Im scratchin' and clawin' to get it
         done for you Clarence, for you and me and the rest of the team and
         who comes through my door but a Baltimore City police lookin' to get
         up in my shit about everything!""",
        """You wanna run a campaign with my money pillowed under your ass, you
         need yo people to back the fuck up Clarence!""",
        """Major crimes? Sheeeeeeeeeeyet. """
    ]

    move_quotes = [
    "Sheeeeeeeeeeeeeeit, warm up the car Day-Day. We need to collect our money from : ",

    """Mm-mmm. Twenty gets you the permits.
    Five is for me for bribing these downtown motherfuckers.
     I mean, I'm the one got to risk walking up to these thieving
     bitches with cash in hand, right?""",

     """Money Launderin' they gonna come talk to me about Money Launderin'
     in West Baltimore, SHIIIIT, Where do you think I'm gonna raise cash
     for the whole damn ticket! From Laundromats and shit, from some tiny ass
      korean groceries, you think I got time to ask a man why he given me
      money or where he gets his money from, I'll take any mothafucker's money
      if he given it away! """,

     """We spend this year dealing with the city, the next doing business with
     the state. However, year three, then we go for the gold. Then we go
      federal. Then we see the man with his hand on the faucet."""
    ]

    def __init__(self, starting_point, island_range):
        self.previous_point = starting_point
        self.current_point = starting_point
        self.island_range = island_range

    def speak(self):
        if(self.previous_point != self.current_point):
            return(Politician.move_quotes[
            random.randint(1,len(Politician.move_quotes)-1)] +
            '\n\n' + Politician.move_quotes[0])
        else:
            return(Politician.stay_quotes[
            random.randint(1,len(Politician.stay_quotes)-1)] +
            '\n\n' + Politician.stay_quotes[0])


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
        print("Iteration %d complete. Here is the relative distribution of visits:" % iteration_number)
        for key in self.chain:
            print( "*" * math.floor(100*self.chain[key]/iteration_number),":", Map.bmore[key]),
        print('\n\n')




    def simulate(self, sim_iterations=500):
        print(" Welcome to Baltimore. Senator Clay Davis\n",
        "needs to pick up money from his 'constituents'. With\n",
        "the help of his trusty driver, Damien 'Day-Day' Price,\n",
        "he needs to go around and pick up his money, going\n",
        "to the places with more money more frequently.  To\n",
        "accomplish this task he is going to use the Metropolis\n",
        "Hastings algorithm.\nTime to get started....\n\n")
        prompt = '> '
        verbose = 'y'
        # make it verbose or not ...
        for i in range(1, sim_iterations):

            self.clay.previous_point = self.clay.current_point
            self.clay.current_point = self.engine.next_hop(self.clay.current_point,
                                                            self.clay.island_range)
            self.chain[self.clay.current_point] += 1

            if(verbose == 'y'):
                print("Would you like to continue stepping through simulation?\n",
                "(y - continue, any other key - show results of simulation after 500 steps)")
                verbose = input(prompt)
                if(verbose == 'y'):
                    print("Clay: " + self.clay.speak() +
                    self.bmore[self.clay.current_point] + '\n\n')

            if i % 50 == 0:
                self.print_histogram(i)
# m = Map()
# m.simulate()
