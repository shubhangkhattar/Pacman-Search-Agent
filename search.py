# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    myStack = util.Stack()
    myStack.push(problem.getStartState())
    closedNodes = []

    backTracking = util.Stack()

    while not myStack.isEmpty():
        current = myStack.pop()

        if(backTracking.isEmpty()):
            backTrack = []
        else:
            backTrack = backTracking.pop()

        if not (current in closedNodes):

            if problem.isGoalState(current):
                return backTrack

            for successor in problem.getSuccessors(current):

                next = successor[0]
                action = successor[1]
                steps = backTrack[::]
                steps.append(action)
                myStack.push(next)
                backTracking.push(steps)

            closedNodes.append(current)

    return backTrack

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    myQueue = util.Queue()
    myQueue.push(problem.getStartState())
    closedNodes = []

    backTracking = util.Queue()

    while not myQueue.isEmpty():
        current = myQueue.pop()

        if (backTracking.isEmpty()):
            backTrack = []
        else:
            backTrack = backTracking.pop()

        if not (current in closedNodes):

            if problem.isGoalState(current):
                return backTrack

            for successor in problem.getSuccessors(current):
                next = successor[0]
                action = successor[1]
                steps = backTrack[::]
                steps.append(action)
                myQueue.push(next)
                backTracking.push(steps)

            closedNodes.append(current)

    return backTrack


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    myPriorityQueue = util.PriorityQueue()
    myPriorityQueue.push((problem.getStartState(),0),0)
    closedNodes = []

    backTracking = util.PriorityQueue()

    while not myPriorityQueue.isEmpty():
        current,cost = myPriorityQueue.pop()


        if (backTracking.isEmpty()):
            backTrack = []
        else:
            backTrack,cost = backTracking.pop()

        if not (current in closedNodes):

            if problem.isGoalState(current):
                return backTrack

            for successor in problem.getSuccessors(current):
                next = successor[0]
                action = successor[1]
                new_cost = successor[2] + cost
                steps = backTrack[::]
                steps.append(action)
                myPriorityQueue.push((next,new_cost),new_cost)
                backTracking.push((steps,new_cost),new_cost)

            closedNodes.append(current)

    return backTrack


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    myPriorityQueue = util.PriorityQueue()
    myPriorityQueue.push((problem.getStartState(),0),0)
    closedNodes = []

    backTracking = util.PriorityQueue()

    while not myPriorityQueue.isEmpty():
        current,cost = myPriorityQueue.pop()

        if (backTracking.isEmpty()):
            backTrack = []
        else:
            backTrack,cost = backTracking.pop()

        if not (current in closedNodes):

            if problem.isGoalState(current):
                return backTrack

            for successor in problem.getSuccessors(current):
                next = successor[0]
                action = successor[1]
                new_cost = successor[2] + cost
                heuristicCost = new_cost + heuristic(next,problem)
                steps = backTrack[::]
                steps.append(action)
                myPriorityQueue.push((next,new_cost),heuristicCost)
                backTracking.push((steps,new_cost),heuristicCost)

            closedNodes.append(current)

    return backTrack



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
