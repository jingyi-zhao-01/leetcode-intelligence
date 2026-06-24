# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-email-addresses
# source_path: LeetCode-Solutions-master/Python/unique-email-addresses.py
# solution_class: Solution
# submission_id: 28d59d957f2dd07a8af6d4c82444b45cd2aeb29d
# seed: 2917514426

# Time:  O(n * l)
# Space: O(n * l)

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def convert(email):
            name, domain = email.split('@')
            name = name[:name.index('+')]
            return "".join(["".join(name.split(".")), '@', domain])

        lookup = set()
        for email in emails:
            lookup.add(convert(email))
        return len(lookup)