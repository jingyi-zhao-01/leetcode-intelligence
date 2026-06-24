# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-tasks-you-can-assign
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-tasks-you-can-assign.py
# solution_class: Solution4
# submission_id: 8f88a7acd06fe4896019b15c282dcf046bfeac82
# seed: 4108477902

# Time:  O(n * (logn)^2)
# Space: O(n)

from sortedcontainers import SortedList

class Solution4(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        def check(tasks, workers, pills, strength, x):
            w = workers[-x:]
            for task in tasks[-x:]:  # enumerate from the hardest task to the easiest task, greedily assign it to the weakest worker whom it can be done by
                i = bisect.bisect_left(w, task)
                if i != len(w):
                    w.pop(i)
                    continue
                if pills:
                    i = bisect.bisect_left(w, task-strength)
                    if i != len(w):
                        w.pop(i)
                        pills -= 1
                        continue
                return False
            return True

        tasks.sort(reverse=True)
        workers.sort()
        left, right = 1, min(len(workers), len(tasks))
        while left <= right:
            mid = left + (right-left)//2
            if not check(tasks, workers, pills, strength, mid):
                right = mid-1
            else:
                left = mid+1
        return right