
__version__ = "0.1"

from .iface import caspo_control

from colomoto.types import PartialState
from algorecell_types import *

from colomoto.minibn import BooleanNetwork

class CaspoControl(object):
    def __init__(self, bn, fixed={}):
        self.bn = BooleanNetwork.auto_cast(bn)
        self.fixed = fixed

    def reprogramming_to_attractor(self, *goal_spec,
            exclude_goal=False, maxsize=0, **goal_kwspec):
        """
        TODO
        """
        goal = PartialState(*goal_spec, **goal_kwspec)
        interventions = caspo_control(self.bn, goal, self.fixed,
                allow_goal_intervention=not exclude_goal,
                maxsize=maxsize)
        strategies = ReprogrammingStrategies()
        for control in interventions:
            st = FromAny(PermanentPerturbation(control))
            strategies.add(st)
        return strategies

def load(bn):
    return CaspoControl(bn)

