from typing import Tuple, List
import pytest
from predicates.state import State
from predicates import guards, actions
from graphs.transition import Transition
from graphs.graph import Edge, Vertex, Graph
from graphs.factory import graph_factory
from planning.planner import plan

# ---------------------------------------------------------------------------
# ...
# ---------------------------------------------------------------------------

g = guards.from_str
a = actions.from_str


def test_planner_model1():
    """
    This test checks the implementation of the planner with a simple model with two 
    different goals
    """
    initial_state = State(
        v1 = False,
        v2 = 0
    )

    t1 = Transition(
        name = f"t1", 
        guard = g("!v1"),
        actions = a(f"v1"),
    )
    t2 = Transition(
        name=f"t2", 
        guard = g("v1 && v2 == 0"),
        actions = a(f"v2 += 1"),
    )
    t3 = Transition(
        name=f"t3", 
        guard = g("v1 && v2 == 0"),
        actions = a(f"v2 += 2"),
    )
    t4 = Transition(
        name=f"t4", 
        guard = g("v1 && v2 == 2"),
        actions = a(f"v2 += 1"),
    )
    t5 = Transition(
        name=f"t5", 
        guard = g("v1"),
        actions = a(f"v2 <- 0"),
    )


    goal = g("v2 == 3")
    p = plan(initial_state, [t1, t2, t3, t4, t5], goal)
    assert p != None
    assert len(p) != 0
    assert p == [t1.name, t3.name, t4.name]

    goal = g("v2 == 1")
    p = plan(initial_state, [t1, t2, t3, t4, t5], goal)
    assert p == [t1.name, t2.name]

    goal = g("v2 == 10")
    p = plan(initial_state, [t1, t2, t3, t4, t5], goal)
    assert p == None

def test_planner_model2():
    """
    This test checks the implementation of the planner with a simple model
    """
    initial_state = State(
        v1 = False,
        v2 = 0
    )
    ts = []
    for i in range(100):
        ts.append(Transition(
            name=f"t{i}", 
            guard = g("!v1"), 
            actions = a(f"v1"), 
        ))

    ts.append(Transition(
        name=f"final", 
        guard = g("v1 && v2 == 0"),
        actions = a(f"v2 += 1"),
    ))

    goal = g("v2 == 1")
    p = plan(initial_state, ts, goal)
    print(p)
    assert p != None
    assert len(p) == 2
    assert p[1] == "final"

def test_planner_model3():
    """
    This test checks the implementation of the planner with a simple model
    """
    initial_state = State(
        v1 = False,
        v2 = 0
    )
    ts = []
    for i in range(100):
        ts.append(Transition(
            name=f"t{i}", 
            guard = g(f"v2 == {i}"), 
            actions = a(f"v2 +=1")
        ))
    

    goal = g("v2 == 100")
    p = plan(initial_state, ts, goal)
    print(p)
    assert p != None
    assert len(p) == 100


def test_planner_model4():
    """
    This test checks the implementation of the planner with a simple model
    """
    initial_state = State(
        v1 = False,
        v2 = 0
    )
    ts = []
    for i in range(100):
        ts.append(Transition(
            name=f"t{i}", 
            guard = g(f"v2 == {i}"), 
            actions = a(f"v2 +=1")
        ))
        
        ts.append(Transition(
            name=f"t{i}_wrong", 
            guard = g(f"v2 != 0"), 
            actions = a(f"v2 -=1")
        ))
    

    goal = g("v2 == 100")
    p = plan(initial_state, ts, goal)
    print(p)
    assert p != None
    assert len(p) == 100