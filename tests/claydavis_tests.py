from nose.tools import *
from claydavis.traveler import Map, Engine, Politician

# def setup():
#     print("SETUP!")
#
# def teardown():
#     print ("TEAR DOWN!")
#
# def test_basic():
#     print ("I RAN!")

def test_map():
    # test that map is created and chain is initialized
    # properly
    temp_map = Map()
    assert_equal(sum(temp_map.chain.values()),1)
    assert_equal(Map.n_islands, len(temp_map.chain))

def test_engine_direction():
    temp_engine = Engine()
    new_direction = temp_engine.direction()
    assert_in(new_direction,["east", "west"])

def test_engine_next_hop():
    temp_engine = Engine()
    # add additional test cases for different scenarios
    # 1) you are the bottom of the range
    # 2) you are at the top of the range
    # 3) you are in the center of the range
    next_spot = temp_engine.next_hop(1,[1,5])
    assert_in(next_spot, range(1,5))


def test_politician():
    test_range = [1,5]
    st_pt = 1
    clay = Politician(st_pt, test_range)
    assert_equal(clay.previous_point, clay.current_point)
    assert_equal(clay.previous_point, st_pt)
    assert_equal(clay.island_range, test_range)
