# auto-analysis-agent

Experiment using Goal Oriented Action Planning (GOAP) in Python using A*.  <br>
The beginning of a hypothetical agent for automating data analysis.

### Available Actions
<pre><code>self.action_import_records()
self.action_check_thresholds()
self.action_do_analysis()
self.action_return_results()</code></pre>

### Input
* Current State
<pre><code>
        num_records = 0
        min_num_records = 10
        is_thresholds_met = False
        is_analysis_complete = False
        simulated_records_fetch = 5
        is_results_delivered = False
</code></pre>

* Goal State
<pre><code>
        is_results_delivered = True
</code></pre>


### Example Output
<pre><code>
('PLAN STEP', {'action': 'import records'})
('PLAN STEP', {'action': 'import records'})
('PLAN STEP', {'action': 'check thresholds'})
('PLAN STEP', {'action': 'do analysis'})
('PLAN STEP', {'action': 'return results'})
</code></pre>

### Run Tests
<pre><code>python -m unittest -v unittest_AutoAnalysisAgent.TestAutoAnalysis</code></pre>

### Resources
* [Goal Oriented Action Planning](http://alumni.media.mit.edu/~jorkin/goap.html)
* [BerkeleyX: CS188.1x Artificial Intelligence](https://courses.edx.org/courses/BerkeleyX/CS188.1x-4/1T2015/info)


