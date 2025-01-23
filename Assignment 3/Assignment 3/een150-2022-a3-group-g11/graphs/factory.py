from typing import List, Optional
from graphs.transition import Transition
from predicates.state import State
from graphs.graph import Graph, Vertex, Edge


def graph_factory(state: State, transitions: List[Transition]) -> Graph:
    """
    In this method you should create a graph that represent the "execution" of
    the transitions from the initial state. I.e. start in the initial state and
    evaluate what transitions that are enabled in that state. call next on these transitions
    so new states are created, from where you continue to take new transitions to new states.
    Observe that there may be loops taking you back to an already visited state, so if 
    you do not handle that, your algorithm may get stuck in an endless loop.

    The name of each vertex in the graph (nodes) should be named as the states since each
    vertex is directly related to one state. So use Vertex.from_state(...) or the Edge.from_states(...)
    class methods. The name of the edges in your graph should be the same name as the transition that can take you
    from the tail vertex (state) to the head vertex (state). That means that different edges can have the
    same name in the graph since one transition can be enabled in multiple states

    You need to decide how you will represent the graph inside the graph class
    and then generate all the objects you need. 
    """

    stack = [state]
    visited = []
    transitioned_edges = []
    transitioned_vertices = []

    while len(stack):   # while stack in not empty
        initial_state = stack.pop() # insert initial state to stack, list.pop() takes items -1 in the list, aka the last item
        state = initial_state
        
        if state not in visited:    # if the state is not in visited, add it to avoid infinite loop
            visited.append(state)

            #for transition in transitions:
            #    if transition.eval(state) == True: 
            possible_transtions = [transition for transition in transitions if transition.eval(state) == True]  # a list of possible transitions
            for transition in possible_transtions:
   
                next_state = transition.next(state)
                edge = Edge.from_states(transition.name, state, next_state) # create an edge with the name of the transition
            
                stack.append(next_state)    # add the next state to the stack
                transitioned_edges.append(edge) # add the edge to the transitioned edges list
                transitioned_vertices.append(Vertex.from_state(state))  # add the vertex to the transitioned vertices list

    return Graph(transitioned_vertices,transitioned_edges)  # return the graph with both vertices and edges
        




















    #stack: list[State]
    #stack = []
    #visited: list[State]

    #graph_edges = Graph.graph1
    
    #new_graph = Graph
    #initial_state = stack_list.pop()
    #stack_list.append(initial_state)    # insert initial state into a new list(stack)
    #while len(stack_list):  # while stack is not empty
    #    initial_state = stack_list.pop()    # take out one state from the stack
        #initial_state = Vertex.from_state(stack_list.pop())
    #    for possible_transitions in transitions:    # for each possible transtions for the state
    #        if state.state == possible_transitions.eval(initial_state):
    #            edge = Edge.from_states(possible_transitions.name, initial_state, initial_state.next()) # create an edge with the name of the transition
    #           edges_transitied.append(edge)   # add the edge to an empty list
    #
    #        if initial_state not in visited_list:    # if the next state is not in visited
    #            stack_list.append(initial_state.next()) # add the next state to stack
    #            visited_list.append(initial_state)  # add the current state to visited to avoid infite loop
    #
    #            vertices_transitied.append(Vertex.from_state(initial_state))

    #return Graph(vertices_transitied, edges_transitied)

    # Insert initial state into a new list (stack)
    #list(state.state.keys())[0]
    #initial_state = list(state.state.items())[0]
    #stack_list.append(initial_state)
    #
    #
    #return Graph
        #for trans in Transition.eval:
            # create an edge
            #edge = Edge.from_states("new_edge", Vertex.from_state(), Vertex.from_state(initial_state.next()))
            #edge = Edge.from_states("t1", initial_state, State(a = 1))
            #edge.append(edges)
            #if successor state not in visited:
            #if state.next() not in visited:
             #  stack.append(state.next())
             #   visited.append(state.next())
        #return edge
    #
    #Edge.from_states("t1", initial_state, State(a = 1))
    #raise NotImplementedError