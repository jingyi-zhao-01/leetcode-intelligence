# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-substrings-containing-all-three-characters
# source_path: LeetCode-Solutions-master/Python/number-of-substrings-containing-all-three-characters.py
# solution_class: Solution3
# submission_id: 271c6065294f22a48466a57a92a6c350a5d45fb6
# seed: 3464672473

# Time:  O(n)
# Space: O(1)

class Solution3(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, right, count = 0, 0, [0]*3
        for left, c in enumerate(s):
            while right < len(s) and not all(count):
                count[ord(s[right])-ord('a')] += 1
                right += 1
            if all(count):
                result += (len(s)-1) - (right-1) + 1
            count[ord(c)-ord('a')] -= 1
        return result