
__version__ = "0.1"

from .iface import caspo_control

from colomoto.types import PartialState
from algorecell_types import *

def reprogramming_to_attractor(bn, *goal_spec, fixed={},
        exclude_goal=False, maxsize=0, **goal_kwspec):
    """
    TODO
    """
    goal = PartialState(*goal_spec, **goal_kwspec)
    interventions = caspo_control(bn, goal, fixed,
            allow_goal_intervention=not exclude_goal,
            maxsize=maxsize)
    strategies = ReprogrammingStrategies()
    for control in interventions:
        st = FromAny(PermanentPerturbation(control))
        strategies.add(st)
    return strategies

