from SearchProblem import SearchProblem
from copy import deepcopy

### modified by mollusk011


class AnalysisState(object):
    def __init__(self, num_records, min_num_records, is_thresholds_met,  is_analysis_complete, is_results_delivered, simulated_records_fetch):
        self.num_records = num_records
        self.min_num_records = min_num_records
        self.is_thresholds_met = is_thresholds_met
        self.is_analysis_complete = is_analysis_complete
        self.is_results_delivered = is_results_delivered
        self.simulated_records_fetch = simulated_records_fetch


    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class AutoAnalysisAgent(SearchProblem):

    def __init__(self, state, goal_state):
        self.startState = state
        self.goal_state = goal_state
        self.costFn = lambda x: 1
        self.actions = []
        self.actions.append(self.action_import_records())
        self.actions.append(self.action_check_thresholds())
        self.actions.append(self.action_do_analysis())
        self.actions.append(self.action_return_results())

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        if(state.is_results_delivered):
            return  True
        else:
            return False


    def getSuccessors(self, state):
        successors = []
        NAME = 0
        PRE_CONDITION = 1
        POST_EFFECT = 2

        for action in self.actions:
            if action[PRE_CONDITION](state):
                nextState = action[POST_EFFECT](state)
                cost = self.costFn(nextState)
                successors.append( ( nextState, action, cost) )

        return successors


    def action_import_records(self):
        def pre_condition(state):
            if(state.num_records <= state.min_num_records):
                return True
            else:
                return False

        def post_condition(state):
            nextState = deepcopy(state)
            #nextState.current_time += 1
            nextState.num_records += state.simulated_records_fetch #do import records
            return nextState

        return ["import records", pre_condition, post_condition, 0]

    def action_check_thresholds(self):
        def pre_condition(state):
            if(state.num_records >= state.min_num_records):
                return True
            else:
                return False

        def post_condition(state):
            nextState = deepcopy(state)
            #nextState.current_time += 1
            nextState.is_thresholds_met = True
            return nextState

        return ["check thresholds", pre_condition, post_condition, 0]


    def action_do_analysis(self):
        def pre_condition(state):
            if(state.is_analysis_complete is False and state.is_thresholds_met is True):
                return True
            else:
                return False

        def post_condition(state):
            nextState = deepcopy(state)
            #nextState.current_time += 1
            nextState.is_analysis_complete = True
            return nextState

        return ["do analysis", pre_condition, post_condition, 0]

    def action_return_results(self):
        def pre_condition(state):
            if(state.is_results_delivered is False and state.is_analysis_complete is True):
                return True
            else:
                return False

        def post_condition(state):
            nextState = deepcopy(state)
            #nextState.current_time += 1
            nextState.is_results_delivered = True
            return nextState

        return ["return results", pre_condition, post_condition, 0]



