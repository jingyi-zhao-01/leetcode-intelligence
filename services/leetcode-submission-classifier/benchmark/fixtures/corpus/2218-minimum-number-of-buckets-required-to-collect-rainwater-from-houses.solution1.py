# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-buckets-required-to-collect-rainwater-from-houses
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-buckets-required-to-collect-rainwater-from-houses.py
# solution_class: Solution
# submission_id: 1ecaa36ecbb6059637bd20fe71c82462fd24a57f
# seed: 2493928494

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def minimumBuckets(self, street):
        """
        :type street: str
        :rtype: int
        """
        result = 0
        street = list(street)
        for i, c in enumerate(street):
            if c != 'H' or (i and street[i-1] == 'B'):
                continue
            if i+1 < len(street) and street[i+1] == '.':
                street[i+1] = 'B'
                result += 1
            elif i and street[i-1] == '.':
                street[i-1] = 'B'
                result += 1
            else:
                return -1
        return result