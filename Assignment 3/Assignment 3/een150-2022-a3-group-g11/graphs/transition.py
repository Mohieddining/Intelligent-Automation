from dataclasses import dataclass
from typing import Optional, Tuple
from predicates.state import State
from predicates.guards import Guard
from predicates.actions import Action
from predicates.errors import NextException

# A Transition class includes a name of the transition, a guard predicate
# and a list of actions.
# The class should implement both the eval funtion and the next function
# in the same way as the guards and the actions. Look at the test so the
# method parameters and return types are correct.

@dataclass(frozen=True, order=True)
class Transition(object):
    name: str
    guard: Guard
    actions: Tuple[Action]


    def eval(self, state: State) -> bool:
        """
        This evaluates to true if the guard is true
        """
        #if self.guard:
        #    return self.guard.eval(state)
        #else:
        #    raise NotImplementedError

        return self.guard.eval(state)

    def next(self, state: State) -> State:
        """
        The transition can be fired when its guard is true, If it is true, a new state is created
        where each action, one at the time, updates the state. Next should raise an NextException
        if next is called when its guard is not true.
        You have to add the next method to Transition
        """
        if self.guard.eval(state):
            for action in self.actions:
                #case = {self.name : self.actions}
                state = action.next(state) # the action to the next state
            return state
            
        else:    
            raise NextException("The guard is not true!")