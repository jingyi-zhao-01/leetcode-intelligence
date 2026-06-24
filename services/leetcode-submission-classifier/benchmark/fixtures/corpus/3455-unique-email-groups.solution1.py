# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-email-groups
# source_path: LeetCode-Solutions-master/Python/unique-email-groups.py
# solution_class: Solution
# submission_id: 091c63842f24c2c8d7ae03be0ca458d8aef251cc
# seed: 4119880635

# Time:  O(n * l)
# Space: O(n * l)

# string, hash table

class Solution(object):
    def uniqueEmailGroups(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for email in emails:
            email = email.lower()
            local = email[:next(i for i, x in enumerate(email) if x in "+@")].replace('.', '')
            domain = email[next(i for i, x in enumerate(email) if x == '@')+1:]
            result.add(local+'@'+domain)
        return len(result)