# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: filter-characters-by-frequency
# source_path: LeetCode-Solutions-master/Python/filter-characters-by-frequency.py
# solution_class: Solution
# submission_id: 01a58e8979d4ccec17ef53b49d753299ccadef53
# seed: 2985970823

# Time:  O(n + 26)
# Space: O(26)

# freq table

class Solution(object):
    def filterCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        return "".join(x for x in s if cnt[ord(x)-ord('a')] < k)