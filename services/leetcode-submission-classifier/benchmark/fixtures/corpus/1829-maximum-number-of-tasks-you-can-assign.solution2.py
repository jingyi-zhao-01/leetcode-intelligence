# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-tasks-you-can-assign
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-tasks-you-can-assign.py
# solution_class: Solution2
# submission_id: fd6df5bba09cf7337846af9a3f1f5b9526c9c17d
# seed: 2951250524

# Time:  O(n * (logn)^2)
# Space: O(n)

from sortedcontainers import SortedList

class Solution2(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        def check(tasks, workers, pills, strength, x):
            w = SortedList(workers[-x:])
            for task in tasks[-x:]:  # enumerate from the hardest task to the easiest task, greedily assign it to the weakest worker whom it can be done by
                i = w.bisect_left(task)
                if i != len(w):
                    w.pop(i)
                    continue
                if pills:
                    i = w.bisect_left(task-strength)
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