# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-time-to-finish-all-jobs
# source_path: LeetCode-Solutions-master/Python/find-minimum-time-to-finish-all-jobs.py
# solution_class: Solution
# submission_id: c654aab32f668aa81d16530fb322beee7a31c651
# seed: 3579568389

# Time:  O(k^n * logr), the real complexity shoud be much less, but hard to analyze
# Space: O(n + k)

class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        def backtracking(jobs, i, cap, counts):
            if i == len(jobs):
                return True
            for j in xrange(len(counts)):
                if counts[j]+jobs[i] <= cap:
                    counts[j] += jobs[i]
                    if backtracking(jobs, i+1, cap, counts):
                        return True
                    counts[j] -= jobs[i]
                if counts[j] == 0:
                    break
            return False

        jobs.sort(reverse=True)
        left, right = max(jobs), sum(jobs)
        while left <= right:
            mid = left + (right-left)//2
            if backtracking(jobs, 0, mid, [0]*k):
                right = mid-1
            else:
                left = mid+1
        return left