#The Place class includes path and non-path places.#

import random
import unit.py

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

    def strategy(self, campus):
        exits = [p for p in campus.places.values() if p.entrance is self]
        for squirrel in self.assault_plan.get(campus.time, []):
            squirrel.move_to(random.choice(exits))
            campus.active_squirrels.append(squirrel)

class Base(Place):
    """What the students are defending."""
    def add_unit(self, unit):
        assert not unit.is_human, 'Cannot add {0} to Base'
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
    pass

class SquirrelsWinException(GameOverException):
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

    def __init__(self, strategy, tree, unit_types, create_places, dimensions, nuts=2):
        """Create an AntColony for simulating a game.

        Arguments:
        strategy -- a function to deploy ants to places
        tree -- a Tree full of bees
        unit_types -- a list of unit constructors
        create_places -- a function that creates the set of places
        dimensions -- a pair containing the dimensions of the game layout
        """
        self.time = 0
        self.nuts = nuts
        self.strategy = strategy
        self.tree = tree
        self.unit_types = OrderedDict((a.name, a) for a in unit_types)
        self.active_squirrels = []
        self.configure(tree, create_places)

    def configure(self, tree, create_places):
        """Configure the places in the campus."""
        self.places = OrderedDict()
        self.squirrel_entrances = []
        def register_place(place, is_squirrel_entrance):
            self.places[place.name] = place
            if is_squirrel_entrance:
                place.entrance = tree
                self.squirrel_entrances.append(place)
        register_place(self.tree, False)
        create_places(base, register_place, self.dimensions[0], self.dimensions[1])
        # create_places originally takes in self.queen for create places here. 

    def simulate(self):
        """Simulate an attack on the campus (i.e., play the game)."""
        num_squirrels = len(self.squirrels)
        try:
            while True:
                self.tree.strategy(self)            # squirrels invade
                self.strategy(self)                 # humans deploy
                for human in self.humanss:               # humans take actions
                    if human.health > 0:
                        human.action(self)
                for squirrel in self.active_squirrels[:]:     # squirrels take actions
                    if squirrel.health > 0:
                        squirrel.action(self)
                    if squirrel.health <= 0:
                        num_squirrels -= 1
                        self.active_squirrels.remove(squirrel)
                if num_squirrels == 0:
                    raise HumansWinException()
                self.time += 1
        except HumansWinException:
            print('All squirrels are vanquished. You win!')
            return True
        except SquirrelsWinException:
            print('Humans have perished. Please try again.')
            return False

    def deploy_human(self, place_name, human_type_name):
        """Place an ant if enough food is available.

        This method is called by the current strategy to deploy humans.
        """
        constructor = self.unit_types[human_type_name]
        if self.nuts < constructor.nut_cost:
            print('Not enough nut remains to place ' + human_type_name)
        else:
            human = constructor()
            self.places[place_name].add_unit(human)
            self.nut -= constructor.nut_cost
            return huma

    def remove_human(self, place_name):
        """Remove a human from the Campus."""
        place = self.places[place_name]
        if place.ant is not None:
            place.remove_unit(place.human)

    @property
    def humans(self):
        return [p.human for p in self.places.values() if p.human is not None]

    @property
    def squirrels(self):
        return [s for p in self.places.values() for s in p.bees]

    @property
    def units(self):
        return self.humans + self.squirrels

    def __str__(self):
        status = ' (Nut: {0}, Time: {1})'.format(self.nut, self.time)
        return str([str(i) for i in self.humans + self.squirrels]) + status


# Weiwei's edit: add layouts
###########
# Layouts #
###########

def plaza_layout(queen, register_place, tunnels=1, length=10, moat_frequency=3):
    """Register Sproul Plaza layout."""
    # for tunnel in range(tunnels):
    #     exit = queen
    #     for step in range(length):
    #         if moat_frequency != 0 and (step + 1) % moat_frequency == 0:
    #             exit = Water('water_{0}_{1}'.format(tunnel, step), exit)
    #         else:
    #             exit = Place('tunnel_{0}_{1}'.format(tunnel, step), exit)
    #         register_place(exit, step == length - 1)

    

=======
class AssaultPlan(dict):

