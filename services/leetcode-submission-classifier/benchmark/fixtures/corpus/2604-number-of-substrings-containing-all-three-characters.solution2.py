# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-substrings-containing-all-three-characters
# source_path: LeetCode-Solutions-master/Python/number-of-substrings-containing-all-three-characters.py
# solution_class: Solution2
# submission_id: 5cb5a77072d6cf3e774287d19a466f8e77ca0eff
# seed: 4173606331

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, left, count = 0, 0, [0]*3
        for right, c in enumerate(s):
            count[ord(s[right])-ord('a')] += 1
            while all(count):
                count[ord(s[left])-ord('a')] -= 1
                left += 1
            result += left
        return result