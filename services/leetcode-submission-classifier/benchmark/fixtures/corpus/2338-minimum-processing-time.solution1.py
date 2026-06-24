# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-processing-time
# source_path: LeetCode-Solutions-master/Python/minimum-processing-time.py
# solution_class: Solution
# submission_id: c7296904b97b9a380227a3f7dcb68275577c8108
# seed: 2707486870

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        K = 4
        processorTime.sort()
        tasks.sort(reverse=True)
        result = 0
        for i in xrange(len(processorTime)):
            for j in xrange(K):
                result = max(result, processorTime[i]+tasks[i*K+j])
        return result