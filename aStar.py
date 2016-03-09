import util
from copy import deepcopy


def nullHeuristic(state, problem=None):

    return 0



def aStarSearch(problem, heuristic=nullHeuristic):

    #Typical A* implementation
    #written by mollusk011



    closed = set()

    from util import PriorityQueue
    fringe = PriorityQueue()

    STATE = 0
    ACT = 1
    COST = 2
    DATA = 3

    node = problem.getStartState()
    plan = []
    plan_cost = []

    fringe.push((node, plan, plan_cost), heuristic(problem.getStartState(), problem))

    while True:
        if fringe.isEmpty():
            return []
            break

        popped = fringe.pop()
        node = popped[0]
        plan = popped[1]
        plan_cost = popped[2]

        if problem.isGoalState(node):
            return plan
            break


        if not node in closed:
            closed.add(node)
            children = problem.getSuccessors(node)

            for child in children:
                sum_plan_cost = sum(plan_cost)
                child[ACT][DATA] = child[STATE]
                fringe.push((child[STATE],plan + deepcopy([child[ACT]]), plan_cost + [child[COST]]), heuristic(child[STATE], problem) + sum(plan_cost + [child[COST]]))  # according to comments priorityqueue prioritizes the lowest priority. depth will make the deepest node the hightest priority
