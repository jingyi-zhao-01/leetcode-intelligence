# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-vowels-in-a-string
# source_path: LeetCode-Solutions-master/Python/sort-vowels-in-a-string.py
# solution_class: Solution
# submission_id: db558eda6469341626e16ef4f7f083b5ad44c5c3
# seed: 4153184099

# Time:  O(n)
# Space: O(1)

# counting sort

class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        def inplace_counting_sort(nums, reverse=False):  # Time: O(n)
            if not nums:
                return
            count = [0]*(max(nums)+1)
            for num in nums:
                count[num] += 1
            for i in xrange(1, len(count)):
                count[i] += count[i-1]
            for i in reversed(xrange(len(nums))):  # inplace but unstable sort
                while nums[i] >= 0:
                    count[nums[i]] -= 1
                    j = count[nums[i]]
                    nums[i], nums[j] = nums[j], ~nums[i]
            for i in xrange(len(nums)):
                nums[i] = ~nums[i]  # restore values
            if reverse:  # unstable sort
                nums.reverse()
    
        VOWELS = "AEIOUaeiou"
        LOOKUP = {x:i for i, x in enumerate(VOWELS)}
        vowels = [LOOKUP[x] for x in s if x in LOOKUP]
        inplace_counting_sort(vowels, reverse=True)
        return "".join(VOWELS[vowels.pop()] if x in LOOKUP else x for x in s)