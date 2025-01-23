from typing import List, Optional, Set
from graphs.transition import Transition
from predicates.guards import Guard
from predicates.state import State


def plan(initial_state: State, transitions: List[Transition], goal: Guard) -> Optional[List[str]]:
    """
    Implement a planning algorithm that can find the shortest path from the 
    initial state to a state where the goal predicate is true. Instead of creating a
    a graph first, perform the search directly using states and trasnitions.
    The path should be created based on the names of the transitions. 

    If the algorithm does not find a path to the goal, return None.
    """

    ## sort the list/stack 
    # Find the shortest path
    # We do not need to create a graph
    # We can search directly using states and transitions:
        # eval and next_planning methods


    #stateDict = { initial_state : [transition.name, initial_state, initial_state.next()]}
    #stack = [initial_state]

    #name = "t1"
    #guard = "v1"
    #action = "v2 += 1"

    #goal.eval(stateDict.keys())


    #visited: Set[State] = set()
    visited = []
    path = []
    stack = [(initial_state, path)] # a tuple inside a list
    #stacklist = [initial_state]
    #path = []

    while len(stack):   # while stack in not empty
        (vertex, path) = stack.pop()    # insert initial state to stack, list.pop() takes items -1 in the list, aka the last item
        initial_state = vertex

        if goal.eval(vertex):   # if we found the way  
            return path # return path, which is a list of all the vertecies we have went through

        if vertex not in visited:   # or if vertex is better than previous
            visited.append(vertex)
            for t in [t for t in transitions if t.eval(vertex) == True]:
            #for t in transitions:
            #    if t.eval(vertex):
                    next_state = t.next(vertex) # next transition
                    next_path = path.copy()
                    next_path.append(t.name)    # path is a list that inlcudes only the name of the vertecies we have went through

                    '''
                    insert takes an index as the first argument
                    the 0 index in stack is initial_state which is a dictonary
                    and it takes next_state and next_path as key and value

                    WRONG!
                    '''

                    '''
                    insert takes an index as the first argument
                    so in this case it updates the list with a new state and a new vertex name(path)
                    and the new add items will be added to index 0, aka will be the first items in the updated list
                    '''
                    stack.insert(0, (next_state, next_path))    # update the stack list with new state and new vertex name
                    #stacklist.append(next_state)
                    #path.append(next_path)
    return None
