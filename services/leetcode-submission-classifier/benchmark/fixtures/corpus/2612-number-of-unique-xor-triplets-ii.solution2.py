# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-unique-xor-triplets-ii
# source_path: LeetCode-Solutions-master/Python/number-of-unique-xor-triplets-ii.py
# solution_class: Solution2
# submission_id: 013232ab5d44e2b10cada7ad4e70eb46f7072393
# seed: 1177497766

# Time:  O(nlogn)
# Space: O(n)

# FWHT, fst

class Solution2(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt2, cnt3 = set([0]), set(),  
        max_cnt = 1<<max(nums).bit_length()
        for x in nums:
            for y in cnt2:
                cnt3.add(x^y)
            for y in nums:
                cnt2.add(x^y)
            if len(cnt3) == max_cnt:
                break
        return len(cnt3)