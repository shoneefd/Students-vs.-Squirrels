#The Place class includes path and non-path places.#

import random

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

class GameOverException(Exception):
    """Base game over Exception."""
    pass

class HumansWinException(GameOverException):
    """Exception to signal that the ants win."""
    pass

class SquirrelsWinException(GameOverException):
    """Exception to signal that the bees win."""
    pass
