# -------------------------------------------------------------------------
# In this file, the various actions, that we will use, are defined 
# (or will be when you have fixed the missing parts)
# -------------------------------------------------------------------------

from curses.ascii import isdigit
from optparse import Values
from typing import List, Optional, Protocol, Any, Tuple
from predicates.state import State
from dataclasses import dataclass
from predicates.errors import NotInStateException, NextException

# this is a test
class Action(Protocol):
    """
    This is our action protocol, which we use to keep track of our duck-typing classes
    Read more about protocol: 
    https://docs.python.org/3/library/typing.html#typing.Protocol
    https://mypy.readthedocs.io/en/stable/protocols.html#simple-user-defined-protocols

    This is just a way for us to document for the users of our code what types we expect
    """
    def next(self, state: State) -> State:
        ...

@dataclass(frozen=True, order=True)
class Assign(object):
    variable: str
    value_or_variable: Any
    """
    The Assign action will assign the given value (or the value of the other variable) 
    to the variable when next is called
    """

    def next(self, state: State) -> State:
        """
        This function creates a new state with an updated value of self.variable in the state
        
        If self.value_or_variable is a variable in state, the value of that variable
        is assigned to self.variable in the state. If self.value_or_variable is not in 
        the state, i.e. it is a value, that value is instead assigned to the state

        If self.variable is not part of the state, the function will raise an NextException
        """

        if not state.contains(self.variable):
            raise NextException("The variable is not in the state")
            
        if state.contains(self.value_or_variable):
            case1 = {self.variable : state.get(self.value_or_variable)}
            return state.next(**case1)
        else:
            case2 = {self.variable : self.value_or_variable}
            return state.next(**case2)

@dataclass(frozen=True, order=True)
class Inc(object):
    variable: str
    inc: int
    """
    The Inc acion will increment the value of the variable with inc 
    """

    def next(self, state: State) -> State:
        """
        This fn creates a new state with the current value of the variable
        incremented with inc steps. If the variable value does not exists, 
        or if the value is not a number, this method will raise a NextException
        Include a good message describing the error
        """

        #if state.get(self.variable) not in state.contains(self.variable) or type(state.get(self.variable)) != type(self.inc):
        #if not state.get(self.variable) or type(state.get(self.variable)) != type(self.inc):
        #    raise NextException("The variable is not in the state")
        #else:
        #    case = {self.variable : state.get(self.variable)+self.inc}
        #    return state.next(**case)

        if state.contains(self.variable) and type(state.get(self.variable)) == type(self.inc):
            case = {self.variable : state.get(self.variable)+self.inc}
            return state.next(**case)
        else:
            raise NextException("The variable is not in the state")

        #raise NotImplementedError
    
    
@dataclass(frozen=True, order=True)
class Dec(object):
    variable: str
    dec: int
    """
    The Dec action will decrement the value of the variable with dec
    """

    def next(self, state: State) -> State:
        """
        This fn creates a new state with the current value of the variable
        decremented with dec steps. If the variable value does not exists, 
        or if the value is not a number, this method will raise a NextException
        Include a good message describing the error
        """
        if state.contains(self.variable) and type(state.get(self.variable)) == type(self.dec):
            case = {self.variable : state.get(self.variable)-self.dec}
            return state.next(**case)
        else:
            raise NextException("The variable is not in the state")
    

@dataclass(frozen=True, order=True)
class Next(object):
    variable: str
    domain: Tuple
    """
    The Next acion will pick the next value from a list of values and assign it to the variable. 
    If the last value is currently assigned, the first value in the list is assigned.
    """

    def next(self, state: State) -> State:
        """
        This function will create a new state where the value of the variable is updated with the 
        next value in the domain list. Based on where the current value is in the domain, 
        the next value in that domain should be assigned to the variable. 
        
        If the variable is not in the in the state, or if current value is not in the domain, this 
        method will raise an NextException
        """
        #self.domain.next(state)
        #self.domain[Inc]
        #Inc(self.domain)
        #self.domain.Inc()
        #Inc.next(state)
        
        #if state.contains(self.variable) or state.get(self.variable) in self.domain:
        #    currentIndex = self.domain.index(state.get(self.variable))
        #    if currentIndex+1 < len(self.domain):
        #        return state.next(**{})

        #if state.contains(self.variable) and type(state.get(self.variable)) == type(self.variable):
        if state.contains(self.variable) and state.get(self.variable) in self.domain:
            
            currentIndex = self.domain.index(state.get(self.variable))
            '''
            The value of the variable must be a string and not an integer, here we are chaning a string with another string
            so we need to check if the value of the variable is a string.
            But how does index() get an integer as an arguemnt?
            '''
            if currentIndex+1 < len(self.domain):
                case = {self.variable : self.domain[currentIndex+1]}
                return state.next(**case)
            else:
                case = {self.variable : self.domain[0]}
                return state.next(**case)

        else:
            raise NextException('error')




        #if state.contains(self.variable) and state.get(self.variable) in self.domain:
        #if state.contains(self.variable) and state.get(self.variable) in self.domain: 
            #values = state.state.values()
            #index = list(values)
#            if index > self.domain.__len__():
 #               index = self.domain.index(0)
        #    index = state.state[self.variable]
        #    for value in self.domain.__iter__():
        #        if value != len(self.domain):
        #            return self.domain[0]
        #    self.domain[state.get(self.variable).index]


        #    case = {self.variable : self.domain+1}
        #    return state.next(**case)
        #else:
            #raise NextException("The variable is not in the state")
        
        
    






#--------------------------------------------
# below is a parser to simplify wring of guards. You do not need to 
# change anything but can take a look how a text parser can be written. 
# See the test_parser.py for example tests
#--------------------------------------------

import re
import ast
from parsec import sepEndBy1, string, regex, generate, many, separated

whitespace = regex(r'\s+')
ignore = many(whitespace)
lexeme = lambda p: p << ignore  # skip all ignored characters.

eq = lexeme(string('='))
arrow = lexeme(string('<-'))
assign_signs = eq | arrow
plus = lexeme(string('+='))
minus = lexeme(string('-='))
not_sign = lexeme(string('!'))
delimiter = lexeme(string(','))
symbol = lexeme(regex(r'\w+'))
number = lexeme(regex(r'\d+'))
lkrull = lexeme(string('{'))
rkrull = lexeme(string('}'))


@generate
def domain():
    """matches {v1, v2, ...}"""
    yield lkrull
    xs = yield sepEndBy1(symbol, delimiter)
    res = []
    for x in xs:
        try:
            val = ast.literal_eval(x)
            res.append(val)
        except ValueError as e:
            res.append(x)
    yield rkrull
    return tuple(res)

@generate
def assign():
    """matches v1 <- value, v1 = value, or v1 <- v2"""
    key = yield symbol
    yield assign_signs
    val = yield symbol
    try:
        val = ast.literal_eval(val)
    except ValueError as e:
        pass
    res = Assign(key, val)
    return res

@generate
def set_to_true():
    """matches v1, which assign True to v1"""
    key = yield symbol
    res = Assign(key, True)
    return res

@generate
def set_to_false():
    """matches !v1, which assign False to v1"""
    yield not_sign
    key = yield symbol
    res = Assign(key, False)
    return res

@generate
def inc():
    """matches v1 += inc, where inc is a number"""
    key = yield symbol
    yield plus
    i = yield number
    res = Inc(key, int(i))
    return res

@generate
def dec():
    """matches v1 -= dec, where dec is a number"""
    key = yield symbol
    yield minus
    i = yield number
    res = Dec(key, int(i))
    return res

@generate
def next() -> Next:
    """matches v1 <- {a, b, c}, where a, b, c are values in the domain"""
    key = yield symbol
    yield assign_signs
    xs = yield domain
    res = Next(key, xs)
    return res



def actions() -> List[Action]:
    return sepEndBy1(next ^ inc ^ dec ^ assign ^ set_to_false ^ set_to_true, delimiter) # type: ignore

def from_str(str) -> Tuple[Action]:
    """This function will parse a str into a list of actions. There may be situation that is not handled though"""
    predicate = ignore >> actions()
    return tuple(predicate.parse(str)) # type: ignore


