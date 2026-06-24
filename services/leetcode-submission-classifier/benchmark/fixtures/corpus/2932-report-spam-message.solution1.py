# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: report-spam-message
# source_path: LeetCode-Solutions-master/Python/report-spam-message.py
# solution_class: Solution
# submission_id: 19a479b5604add15f09bc95e67006f5fc0d3a691
# seed: 4231599968

# Time:  O(n + m)
# Space: O(m)

# hash table

class Solution(object):
    def reportSpam(self, message, bannedWords):
        """
        :type message: List[str]
        :type bannedWords: List[str]
        :rtype: bool
        """
        THRESHOLD = 2
        lookup = set(bannedWords)
        return sum(m in lookup for m in message) >= THRESHOLD