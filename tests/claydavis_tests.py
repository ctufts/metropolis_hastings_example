from nose.tools import *
from claydavis.traveler import Island

# def setup():
#     print("SETUP!")
#
# def teardown():
#     print ("TEAR DOWN!")
#
# def test_basic():
#     print ("I RAN!")

def test_island():
    starting_point = 1
    island_range = [1,10]
    print("Testing Island init")
    baltimore = Island(starting_point, island_range)
    assert_equal(baltimore.current_point, starting_point)
    assert_equal(baltimore.island_range,island_range)

def test_direction():
    temp_island = Island(1,[1,5])
    new_direction = temp_island.direction()
    assert_in(new_direction,["east", "west"])

def test_next_hop():
    temp_island = Island(1,[1,5])
    assert False
    # generate the different possible scenarios
    # 1) you are the bottom of the range
    # 2) you are at the top of the range
    # 3) you are in the center of the range
