import ants
import graphics
from graphics import shift_point
from ucb import *
from math import pi
import math
import os
import random

STRATEGY_SECONDS = 3


class GUI:

    from utils import *
    @main
    def run(*args):
        humans.start_with_strategy(args, GUI().strategy)
