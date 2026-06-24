# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: detect-pattern-of-length-m-repeated-k-or-more-times
# source_path: LeetCode-Solutions-master/Python/detect-pattern-of-length-m-repeated-k-or-more-times.py
# solution_class: Solution
# submission_id: fec4b124b2490d7d871fe7ab3117b6a9d255601a
# seed: 1591737575

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        cnt = 0
        for i in xrange(len(arr)-m):
            if arr[i] != arr[i+m]:
                cnt = 0
                continue
            cnt += 1
            if cnt == (k-1)*m:
                return True
        return False