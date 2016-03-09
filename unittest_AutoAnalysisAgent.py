import sys
import unittest

from AutoAnalysisAgent import AutoAnalysisAgent, AnalysisState
from aStar import aStarSearch


class TestAutoAnalysis(unittest.TestCase):

    def setUp(self):
        pass

    def test_fetch_data_2_times_before_analysis(self):
        """Fetch data 2 times before Analysis"""
        #set-up state parameters
        num_records = 0
        min_num_records = 10
        is_thresholds_met = False
        is_analysis_complete = False
        is_results_delivered = False
        simulated_records_fetch = 5

        current_state = AnalysisState(num_records, min_num_records, is_thresholds_met,  is_analysis_complete, is_results_delivered, simulated_records_fetch)

        is_results_delivered = True
        goal_state = AnalysisState(num_records, min_num_records, is_thresholds_met,  is_analysis_complete, is_results_delivered, simulated_records_fetch)

        plan = aStarSearch(AutoAnalysisAgent(current_state, goal_state))

        self.assertEqual(len([x for x in plan if x[0] == 'import records']), 2)

        for p in plan:
            print ("PLAN STEP", {'action' : p[0]})


    def test_fetch_data_1_times_before_analysis(self):
        """Fetch data 1 times before Analysis"""
        #set-up state parameters
        num_records = 0
        min_num_records = 5
        is_thresholds_met = False
        is_analysis_complete = False
        is_results_delivered = False
        simulated_records_fetch = 5

        current_state = AnalysisState(num_records, min_num_records, is_thresholds_met,  is_analysis_complete, is_results_delivered, simulated_records_fetch)

        is_results_delivered = True
        goal_state = AnalysisState(num_records, min_num_records, is_thresholds_met,  is_analysis_complete, is_results_delivered, simulated_records_fetch)

        plan = aStarSearch(AutoAnalysisAgent(current_state, goal_state))

        self.assertEqual(len([x for x in plan if x[0] == 'import records']), 1)

        for p in plan:
            print ("PLAN STEP", {'action' : p[0]})

    def test_fetch_data_0_times_before_analysis(self):
        """Fetch data 0 times before Analysis"""
        #set-up state parameters
        num_records = 6
        min_num_records = 5
        is_thresholds_met = False
        is_analysis_complete = False
        is_results_delivered = False
        simulated_records_fetch = 5

        current_state = AnalysisState(num_records, min_num_records, is_thresholds_met,  is_analysis_complete, is_results_delivered, simulated_records_fetch)

        is_results_delivered = True
        goal_state = AnalysisState(num_records, min_num_records, is_thresholds_met,  is_analysis_complete, is_results_delivered, simulated_records_fetch)

        plan = aStarSearch(AutoAnalysisAgent(current_state, goal_state))

        self.assertEqual(len([x for x in plan if x[0] == 'import records']), 0)

        for p in plan:
            print ("PLAN STEP", {'action' : p[0]})


if __name__ == '__main__':
    #unittest.main()
    fooSuite = unittest.TestLoader().loadTestsFromTestCase(TestAutoAnalysis)
    fooRunner = unittest.TextTestRunner(descriptions=True, verbosity=1)
    fooRunner.run(fooSuite)