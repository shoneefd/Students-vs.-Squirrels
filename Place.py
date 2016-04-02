#The Place class includes path and non-path places.#

import random

class Place(object):
    """A Place holds squirrels/humans and has an exit leading to another Place."""

    def __init__(self, name, is_path, exit=None):
        self.name = name
        self.exit = exit
        self.squirrels = squirrels
        self.human = None
        self.entrance = None
        self.is_path = is_path
        if self.exit != None:
            self.exit.entrance = self

    def add_unit(self, unit):
        if insect.is_human:
            if self.human is None:
                self.human = unit;
            else:
                assert self.human is None, 'Two humans in {0}'.format(self)
        else:
            self.squirrels.append(unit)
        unit.place = self

    def remove_unit(self, unit):
        if unit.is_human
            self.human = None
        else:
            self.squirrels.remove(unit)
        unit.place = None

class Tree(Place):
    """The place from where the squirrels attack."""
    def __init__(self, assault_plan):
        self.name = 'Tree'
        self.assault_plan = assault_plan
        self.squirrels = []
        for squirrel in assault_plan.all_squirrels:
            self.add_unit(squirrel)
        self.entrance = None
        self.ant = None
        self.exit = None

    def strategy(self, campus): #what is this function doing???#
        exits = [p for p in campus.places.values() if p.entrance is self]
        for squirrel in self.assault_plan.get(campus.time, []):
            squirrel.move_to(random.choice(exits))
            campus.active_squirrels.append(squirrel)

class Base(Place):
    """What the students are defending."""
    def add_unit(self, unit):
        assert not unit.is_human, 'Cannot add {0} to Base'
        raise SquirrelsWinException()

class GameOverException(Exception):
    """Base game over Exception."""
    pass

class HumansWinException(GameOverException):
    pass

class SquirrelsWinException(GameOverException):
    pass

class AssaultPlan(dict):
    """Dictionary from times to waves(list of bees)"""
    def add_wave(self, squirrel_type, bee_health, time, count):
        """Add a wave at time with count Squirrels that have the specified health."""
        squirrels = [squirrel_type(squirrel_health) for _ in range(count)]
        self.setdefault(time, []).extend(squirrels)
        return self

    @property
    def all_squirrels(self):
        """Place all Squirrels in the Tree and return the list of Squirrels."""
        return [squirrel for wave in self.values() for squirrel in wave]

    def make_test_assault_plan():
            plan = AssaultPlan()
            for time in range(3, 16, 2):
                plan.add_wave(Squirrel, 3, time, 1)
            return plan

def interactive_strategy(campus):
    print('campus: ' + str(campus))
    msg = '<Control>-D (<Control>-Z <Enter> on Windows) completes a turn.\n'
    interact(msg)

def start_with_strategy(args, strategy):
    """Reads command-line arguments and starts a game with those options."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Students vs Squirrels")
    parser.add_argument('-d', type=str, metavar='DIFFICULTY',
                        help='sets difficulty of game (easy/medium/hard/insane)')
    parser.add_argument('--cost', type=int,
                        help='number of cost to start with when testing', default=2)
    args = parser.parse_args()

    assault_plan = make_test_assault_plan()
    tunnel_length = 10
    num_tunnels = 1
    costs = args.cost

    tree = Tree(assault_plan)
    dimensions = (num_tunnels, tunnel_length)
    return AntColony(strategy, tree, human_types(), layout, dimensions, cost).simulate()

from utils import *
@main
def run(*args):
    start_with_strategy(args, interactive_strategy)
