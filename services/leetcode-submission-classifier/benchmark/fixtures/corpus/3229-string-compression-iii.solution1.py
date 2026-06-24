# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: string-compression-iii
# source_path: LeetCode-Solutions-master/Python/string-compression-iii.py
# solution_class: Solution
# submission_id: 7fc6fd7eb359056f9868f7ce3a2264358014d6d8
# seed: 3940337080

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        result = []
        cnt = 0
        for i in xrange(len(word)):
            cnt += 1
            if cnt == 9 or (i+1 == len(word) or word[i+1] != word[i]):
                result.append("%s%s" % (cnt, word[i]))
                cnt = 0
        return "".join(result)