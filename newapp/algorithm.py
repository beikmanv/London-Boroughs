from queue import PriorityQueue

class PathfindingProblem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def is_goal(self, state):
        return state == self.goal

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def expand(problem, node, boroughs, neighbors):
    children = []
    for neighbor in neighbors.get(node.state, []):
        new_cost = node.cost + heuristic(node.state, neighbor, boroughs)
        child = Node(state=neighbor, parent=node, cost=new_cost, heuristic=heuristic(neighbor, problem.goal, boroughs))
        children.append(child)
    return children

def heuristic(a, b, boroughs):
    a_coords = boroughs[a]
    b_coords = boroughs[b]
    return ((a_coords[0] - b_coords[0]) ** 2 + (a_coords[1] - b_coords[1]) ** 2) ** 0.5

def a_star(problem, boroughs, neighbors):
    frontier = PriorityQueue()
    start_node = Node(state=problem.initial, cost=0, heuristic=heuristic(problem.initial, problem.goal, boroughs))
    frontier.put(start_node)
    explored = set()

    while not frontier.empty():
        current_node = frontier.get()
        if problem.is_goal(current_node.state):
            return current_node

        explored.add(current_node.state)
        for child in expand(problem, current_node, boroughs, neighbors):
            if child.state not in explored:
                frontier.put(child)

    return None

def path_states(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    return path
