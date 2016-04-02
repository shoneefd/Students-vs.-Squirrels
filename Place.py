#The Place class includes path and non-path places.#

import random
import unit.py

class Place(object):
    """A Place holds squirrels/humans and has an exit leading to another Place."""

    def __init__(self, name, exit=None):
        self.name = name
        self.exit = exit
        self.squirrels = squirrels
        self.human = None
        self.entrance = None
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
        """Remove an Insect from this Place.

        A target Ant may either be directly in the Place, or be contained by a
        container Ant at this place. The true QueenAnt may not be removed. If
        remove_insect tries to remove an Ant that is not anywhere in this
        Place, an AssertionError is raised.

        A Bee is just removed from the list of Bees.
        """
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

    def strategy(self, campus):
        exits = [p for p in campus.places.values() if p.entrance is self]
        for squirrel in self.assault_plan.get(campus.time, []):
            squirrel.move_to(random.choice(exits))
            campus.active_squirrels.append(squirrel)

class Base(Place):
    def add_unit(self, unit):
        """Add an Insect to this Place.

        Can't actually add Ants to a QueenPlace. However, if a Bee attempts to
        enter the QueenPlace, a BeesWinException is raised, signaling the end
        of a game.
        """
        assert not unit.is_human, 'Cannot add {0} to QueenPlace'
        raise SquirrelsWinException()

# Weiwei's edit: added ants_win and bees_win
def ants_win():
    """Signal that Ants win."""
    raise AntsWinException()

def bees_win():
    """Signal that Bees win."""
    raise BeesWinException()

class GameOverException(Exception):
    """Base game over Exception."""
    pass

class HumansWinException(GameOverException):
    """Exception to signal that the ants win."""
    pass

class SquirrelsWinException(GameOverException):
    """Exception to signal that the bees win."""
    pass


# Weiwei's edit: added the Game Setting: campus
##################
# Game Setting #
##################
class Campus(object):
    """An ant collective that manages global game state and simulates time.

    Attributes:
    time -- elapsed time
    food -- the colony's available food total
    queen -- the place where the queen resides
    places -- A list of all places in the colony (including a Hive)
    bee_entrances -- A list of places that bees can enter
    """

    def __init__(self, strategy, hive, ant_types, create_places, dimensions, food=2):
        """Create an AntColony for simulating a game.

        Arguments:
        strategy -- a function to deploy ants to places
        hive -- a Hive full of bees
        ant_types -- a list of ant constructors
        create_places -- a function that creates the set of places
        dimensions -- a pair containing the dimensions of the game layout
        """
        self.time = 0
        self.food = food
        self.strategy = strategy
        self.hive = hive
        self.ant_types = OrderedDict((a.name, a) for a in ant_types)
        self.dimensions = dimensions
        self.active_bees = []
        self.configure(hive, create_places)

    def configure(self, hive, create_places):
        """Configure the places in the colony."""
        self.queen = QueenPlace('AntQueen')
        self.places = OrderedDict()
        self.bee_entrances = []
        def register_place(place, is_bee_entrance):
            self.places[place.name] = place
            if is_bee_entrance:
                place.entrance = hive
                self.bee_entrances.append(place)
        register_place(self.hive, False)
        create_places(self.queen, register_place, self.dimensions[0], self.dimensions[1])

    def simulate(self):
        """Simulate an attack on the ant colony (i.e., play the game)."""
        num_bees = len(self.bees)
        try:
            while True:
                self.hive.strategy(self)            # Bees invade
                self.strategy(self)                 # Ants deploy
                for ant in self.ants:               # Ants take actions
                    if ant.armor > 0:
                        ant.action(self)
                for bee in self.active_bees[:]:     # Bees take actions
                    if bee.armor > 0:
                        bee.action(self)
                    if bee.armor <= 0:
                        num_bees -= 1
                        self.active_bees.remove(bee)
                if num_bees == 0:
                    raise AntsWinException()
                self.time += 1
        except AntsWinException:
            print('All bees are vanquished. You win!')
            return True
        except BeesWinException:
            print('The ant queen has perished. Please try again.')
            return False

    def deploy_ant(self, place_name, ant_type_name):
        """Place an ant if enough food is available.

        This method is called by the current strategy to deploy ants.
        """
        constructor = self.ant_types[ant_type_name]
        if self.food < constructor.food_cost:
            print('Not enough food remains to place ' + ant_type_name)
        else:
            ant = constructor()
            self.places[place_name].add_insect(ant)
            self.food -= constructor.food_cost
            return ant

    def remove_ant(self, place_name):
        """Remove an Ant from the Colony."""
        place = self.places[place_name]
        if place.ant is not None:
            place.remove_insect(place.ant)

    @property
    def ants(self):
        return [p.ant for p in self.places.values() if p.ant is not None]

    @property
    def bees(self):
        return [b for p in self.places.values() for b in p.bees]

    @property
    def insects(self):
        return self.ants + self.bees

    def __str__(self):
        status = ' (Food: {0}, Time: {1})'.format(self.food, self.time)
        return str([str(i) for i in self.ants + self.bees]) + status
