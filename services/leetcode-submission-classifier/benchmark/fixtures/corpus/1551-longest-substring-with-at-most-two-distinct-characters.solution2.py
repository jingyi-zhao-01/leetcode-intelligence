# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-substring-with-at-most-two-distinct-characters
# source_path: LeetCode-Solutions-master/Python/longest-substring-with-at-most-two-distinct-characters.py
# solution_class: Solution2
# submission_id: 6ddc00817ed7012e9bd62a412b9f9eabedd068b1
# seed: 3150050342

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter()
        left, max_length = 0, 0
        for right, char in enumerate(s):
            counter[char] += 1
            while len(counter) > 2:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            max_length = max(max_length, right-left+1)
        return max_length