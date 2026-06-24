# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: intersection-of-two-arrays
# source_path: LeetCode-Solutions-master/Python/intersection-of-two-arrays.py
# solution_class: Solution
# submission_id: 3e8f11e6fbfbde954521423326df4dd316b690a7
# seed: 2200840472

# Time:  O(m + n)
# Space: O(min(m, n))

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        lookup = set()
        for i in nums1:
            lookup.add(i)

        res = []
        for i in nums2:
            if i in lookup:
                res += i,
                lookup.discard(i)

        return res

    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))