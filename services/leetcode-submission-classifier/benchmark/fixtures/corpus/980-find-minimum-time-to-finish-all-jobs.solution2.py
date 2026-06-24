# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-time-to-finish-all-jobs
# source_path: LeetCode-Solutions-master/Python/find-minimum-time-to-finish-all-jobs.py
# solution_class: Solution2
# submission_id: 297f6089825b78b6ce7662bfd0d7fe273039cd87
# seed: 115832150

# Time:  O(k^n * logr), the real complexity shoud be much less, but hard to analyze
# Space: O(n + k)

class Solution2(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        def backtracking(jobs, i, counts, result):
            if i == len(jobs):
                result[0] = min(result[0], max(counts))
                return
            for j in xrange(len(counts)):
                if counts[j]+jobs[i] <= result[0]:
                    counts[j] += jobs[i]
                    backtracking(jobs, i+1, counts, result)
                    counts[j] -= jobs[i]
                if counts[j] == 0:
                    break

        jobs.sort(reverse=False)
        result = [sum(jobs)]
        backtracking(jobs, 0, [0]*k, result)
        return result[0]