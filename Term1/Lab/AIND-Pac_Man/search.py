# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def getActions(parents, node):
  """
  get a list of actions from source to target node 
  parents: a dictionary for {parenet:child} key (State),value (parent State, action) pair
  node: target node
  """
  n = (node,None)
  ret = []
  count = 0
  while parents[n[0]]:
    n = parents[n[0]]
    ret.append(n[1])
  return ret[::-1]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  frontier = util.Stack() # a stack for storing States to visit
  start = problem.getStartState()
  visited = [] # a set stores the States that were visited
  frontier.push((start,[]))
  while not frontier.isEmpty():
    currentState, path = frontier.pop()
    visited.append(currentState) # mark node as visited
    # if the node is the goal state,  return action list
    if problem.isGoalState(currentState):
        return path

    for node in problem.getSuccessors(currentState):   
      newState = node[0] # State of Successor node
      action = node[1] # action to Successor node
             
      # if current postion State is not visited, add it to frontier 
      if newState not in visited:
        frontier.push((newState, path+[action]))

  return None
  
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  frontier = util.Queue() # a queue for storing States to visit
  start = problem.getStartState()
  visited = [start] # a set stores the States that were visited
  frontier.push((start, []))

  while not frontier.isEmpty():
    currentState, path = frontier.pop()
    # if the pop out node is the target node, we find the best solution
    if problem.isGoalState(currentState):
      return path

    for node in problem.getSuccessors(currentState):
      # if the node is the goal state,  return action list
      newState = node[0] # State of Successor node
      action = node[1] # action to Successor node
      
         
      # if current postion State is not visited, add it to frontier 
      if newState not in visited:
        visited.append(newState) # mark node as visited
        frontier.push((newState, path+[action]))

  return None


  
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  queue = util.PriorityQueue() # a queue for storing States to visit
  start = problem.getStartState()
  frontier = [start]
  queue.push((start,[]),0)
  count = 0

  while not queue.isEmpty():
    currentState, path = queue.pop() # get both priority and State
    # if the pop out node is the target node, we find the best solution
    if problem.isGoalState(currentState):
        return path

    #if currentState not in visited:
    #  visited.append(currentState) # mark node as visited

    for node in problem.getSuccessors(currentState):
      # if the node is the goal state,  return action list
      newState = node[0] # State of Successor node
      action = node[1] # action to Successor node   
      # if current postion State is not visited, add it to frontier 
      if newState not in frontier:
        # f(n) = estimated total cost of path through n to goal 
        # g(n) = cost so far to reach n 
        # f(n) = g(n) 
        queue.push((newState, path+[action]), problem.getCostOfActions(path+[action]))
        frontier.append(newState)   
      else:
        queue.replace(newState, path+[action], problem.getCostOfActions(path+[action]))
      


  return None



  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  queue = util.PriorityQueue() # a queue for storing States to visit
  start = problem.getStartState()
  frontier = [start]
  queue.push((start,[]), 0)


  while not queue.isEmpty():
    currentState, path = queue.pop() # get both priority and State
    #print("cost:{}, State:{}", cost, currentState)
    # if the pop out node is the target node, we find the best solution
    if problem.isGoalState(currentState):
        return path

    #if currentState not in visited:
    #  visited.append(currentState) # mark node as visited

    for node in problem.getSuccessors(currentState):
      # if the node is the goal state,  return action list
      newState = node[0] # State of Successor node
      action = node[1] # action to Successor node      
      # if current postion State is not visited, add it to frontier 
      totalCost = problem.getCostOfActions(path+[action]) + heuristic(newState, problem)
      if newState not in frontier:
        # f(n) = estimated total cost of path through n to goal 
        # h(n) = estimated cost from n to goal heuristic(State,problem)
        # g(n) = cost so far to reach n == cost
        # f(n) = h(n) + g(n)
        
        queue.push((newState, path+[action]),totalCost)
        frontier.append(newState)
      else:
        queue.replace(newState, path+[action], totalCost)



  return None



  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
