# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-of-spliced-array
# source_path: LeetCode-Solutions-master/Python/maximum-score-of-spliced-array.py
# solution_class: Solution
# submission_id: 057483ead70feee7d541c07701f59cb5661137e0
# seed: 3130147271

# Time:  O(n)
# Space: O(1)

# greedy, kadane's algorithm

class Solution(object):
    def maximumsSplicedArray(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def kadane(a):
            result = curr = 0
            for x in a:
                curr = max(curr+x, 0)
                result = max(result, curr)
            return result
    
        return max(sum(nums1)+kadane((nums2[i]-nums1[i] for i in xrange(len(nums1)))),
                   sum(nums2)+kadane((nums1[i]-nums2[i] for i in xrange(len(nums2)))))