from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Tuple
from predicates.state import State


@dataclass(frozen=True, order=True)
class Vertex(object):
    name: str
    """
    This class represents the vertices (or nodes) in a graph and is just a name that in simple
    cases will be named the same as the state. Later on we may add more things to
    this class if we need to. When creating this and have a state, use Vertex.from_state(state)
    You do not need to change this class
    """

    @classmethod
    def from_state(cls, state: State) -> Vertex:
        return cls(str(state))

@dataclass(frozen=True, order=True)
class Edge(object):
    name: str
    tail: Vertex
    head: Vertex
    """
    This class represents the edges of a graph and connects two vertices defining how 
    it is possible to navigate in the graph. If you have two states, use the 
    Edge.from_states(name, state_tail, state_head) so that the names will be correct
    You do not need to change this class
    """

    @classmethod
    def from_states(cls, name: str, tail: State, head: State) -> Edge:
        return cls(name, Vertex.from_state(tail), Vertex.from_state(head))


# When creating a new graph, you need to decide what fields the constructor should have
# and what you plan to save in the graph. I have added a dataclass decorator so you just add your fields 
# directly after te class name like the other classes. This class is not immutable (frozen) since you may 
# want to create a graph and then add more to it after that. Either you create the full representation of 
# the graph before creating it or you can also create an empty graph and add new vertices and edges to it.
# If you need to add data to it after creation, just add new methods to the graph. Also remember to write 
# tests for it
#  
# You also need to decide how you store the parts of the graph inside this class.
#
# Observe, the graph should not know anything about Transitions, States, Guards and actions!
@dataclass
class Graph(object):
    vertices: list[Vertex]
    edges: list[Edge]
    #graph: dict[Vertex, Edge]
    #graph1: list = [Vertex, Edge]

    def outgoing(self, vertex: Vertex) -> list[Edge]:
        """
        This method should return all edges that are outgoing from the given vertex
        """
        #return Edge.from_states(vertex)
        #raise NotImplementedError
        #outgoing = Vertex.from_state(tail)
        #return cls[1]
        #return list(Edge.from_states(name, Vertex.from_state(tail), Vertex.from_state(head)))
        #return Vertex.from_state()
        #return Edge.from_states()
        #currentIndex = self.vertices[0]
        #x = [currentIndex, Edge]
        #return x
        
        outgoing_edges = []
        #for edge in self.edges:
            #if edge.tail == vertex:
        for edge in [edge for edge in self.edges if edge.tail == vertex]:
            outgoing_edges.append(edge)
        return outgoing_edges

        # initial state might be tail

    def incoming(self, vertex: Vertex) -> list[Edge]:
        """
        This method should return all edges that are incoming to the given vertex
        """
        
        incoming_edges = []
        #for edge in self.edges:
            #if edge.head == vertex:
        for edge in [edge for edge in self.edges if edge.head == vertex]:
            incoming_edges.append(edge)
        return incoming_edges

    def successor(self, vertex: Vertex) -> list[Vertex]:
        """
        This method should return all vertices that are successors to the given vertex
        """
        
        
        #for vertex in [vertex for vertex in self.vertices if]
        #for edge in self.edges:
          #  if edge.tail == vertex:
         #       incoming_successor.append(self.vertices)
        #return incoming_successor

        #for successor in [successor for successor in self.vertices if successor.eval(state) == True]:

        '''A successor in a head vertex(state), or next state'''
        succVer = []
        for edge in self.outgoing(vertex):
            succVer.append(edge.head)
        return succVer

        #outgoing_tails = []
        #for edge in [edge for edge in self.edges if edge.tail == vertex]:
        #    outgoing_tails.append(edge)
        #for successor in self.vertices:
        #    if successor.from_state(State.state.(successor)):
            #successor = vertex.next()
            #if successor in outgoing_tails:
                #successor = vertex
        #        incoming_successor.append(successor)
        #return incoming_successor

        #for successor in self.vertices:
            #Vertex.from_state(state.next())
        #    initial_state = self.vertices.pop()
        #    incoming_successor.append(initial_state)
        #return incoming_successor
        
        #raise NotImplementedError

    def predecessor(self, vertex: Vertex) -> list[Vertex]:
        """
        This method should return all vertices that are preceding the given vertex
        """

        '''A predecessor in a tail vertex(state), or previous state'''

        predVer = []
        for edge in self.incoming(vertex):
            predVer.append(edge.tail)
        return predVer

    def from_path(self, vertex: Vertex, path: list[str]) -> Optional[Vertex]:
        """
        This method should return the vertex that you will reach if you follow
        the path of edge names from the given vertex, or None if the path 
        does not exists. 
        """
        
        #edges = {}
        #for edge in self.edges:
        #    edge_name = {edge.name : edge}
         #   edges.update({**edge_name})
        #for x in range(len(path) - 1):  # the last element in the list
        #    if path[x] in edges.keys():
        #        if edges[path[x]].head != edges[path[x+1]].tail:
        #            return None
        #        elif x == len(path) - 2:
        #            return edges[path[x+1]].head
        #return None
        

        goal = vertex
        for verName in path:
            prevState = goal
            for edge in self.outgoing(prevState):
                if verName == edge.name:
                    goal = edge.head
                    break
            if prevState == goal:
                return None
        return goal


    def source_vertices(self) -> list[Vertex]:
        """
        This method should return all vertices that are source vertices
        meaning that they do not have any incoming edges
        """


        #source_vertices = [] 
        #for vertex in self.vertices:
        #    for edge in self.edges:
        #        if edge.tail in self.vertices and edge.head not in self.vertices:
        #            edge = vertex
        #            source_vertices.append(vertex)
        #return source_vertices

        sourceVer = []
        verticesHeads = []

        for edge in self.edges: # for edge in all edges
            verticesHeads.append(edge.head) # add all the vertices with heads
        #for edge in self.edges:
            if edge.tail not in verticesHeads and edge.tail not in sourceVer:   # only the source vertex meets this condition
                sourceVer.append(edge.tail)
        return sourceVer



        #for edge in [edge for edge in self.edges if edge not in otherVer]:
        #for edge in self.edges:
        #    otherVer.append(edge.head)  # add all the vertices that have heads, aka all vertices except the source
            #if edge.tail not in otherVer:
        #    sourceVer.append(edge.tail)
        #return sourceVer
        #for edge in self.edges:
        #    if edge.tail == False:
        #        sourceVer.append(edge.tail)
        #return sourceVer

        #for edge in [edge for edge in self.edges if edge.head == vertex]

        #for source in self.vertices:
        #    for edge in self.edges:
        #        if source not in self.successor(edge.tail):
        #            sourceVer.append(source)
        #return sourceVer
        
            
        #for source in self.vertices:
        #    if source in self.outgoing(source) and source not in self.incoming(source):
        #        sourceVer.append(source)
        #return sourceVer
        #
        #for edge in self.edges:
        #    if edge.head:
        #        sourceVer.append(edge.head)
        #return sourceVer
        #for source in [source for source in self.vertices if source not in self.successor(source)]:
        #for source in [source for source in self.vertices if(source in self.outgoing(source) and source not in self.incoming(source))]:
        #for vertex in self.predecessor:
        #for source in [source for source in self.vertices]:
        #for source in self.predecessor:
        # if vertex in self.predecessor:
        #    if source in self.outgoing(source) and source not in self.incoming(source):
        #        sourceVer.append(source)
        #return sourceVer
        
    def sink_vertices(self) -> list[Vertex]:
        """
        This method should return all vertices that are sink vertices
        meaning that they do not have any outgoing edges
        """

        sinkVer = []
        verticesTails = []

        for edge in self.edges: # for edge in all edges
            verticesTails.append(edge.tail) # add all the vertices with tails
        for edge in self.edges:
            if edge.head not in verticesTails and edge.head not in sinkVer:
                sinkVer.append(edge.head)
        return sinkVer
        
        
        
        #    if edge.head not in verticesTails and edge.head not in sinkVer:   # only the source vertex meets this condition
        #        sinkVer.append(edge.head)
        #return sinkVer


        #sourceVer = []
        #verticesHeads = []

        #for edge in self.edges: # for edge in all edges
        #    verticesHeads.append(edge.head) # add all the vertices with heads
        #    if edge.tail not in verticesHeads and edge.tail not in sourceVer:   # only the source vertex meets this condition
        #        sourceVer.append(edge.tail)
        #return sourceVer

    # the below methods are already implemented and can be used for easy troubleshooting
    def print_nice(self, vertex: Vertex, depth: int, found = set(), to_print = ""):
        """
        A way to print part of the graph for better troubleshooting. If your methods above
        works, this should print the traces from vertex. You do not need to change it
        """
        if depth <= 0:
            return
        f = found.copy()
        f.add(vertex)
        outgoing = self.outgoing(vertex)
        if len(outgoing) == 0:
            print(to_print + str(vertex))

        for edge in outgoing:
            trace = to_print + f"{vertex} - {edge.name}"
            if edge.head not in f:
                trace = trace + " -> "
                self.print_nice(edge.head, depth - 1, f, trace)
            else:
                print(trace +f" -> {edge.head}")


    def print_from_sources(self, depth: int):
        for s in self.source_vertices():
            self.print_nice(s, depth)





