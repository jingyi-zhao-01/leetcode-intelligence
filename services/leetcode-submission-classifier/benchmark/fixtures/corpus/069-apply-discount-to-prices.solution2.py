# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apply-discount-to-prices
# source_path: LeetCode-Solutions-master/Python/apply-discount-to-prices.py
# solution_class: Solution2
# submission_id: fc0f8f5173cd2a237a3d1f1e636c8d0d7d7f429e
# seed: 3555829281

# Time:  O(n)
# Space: O(1)

# string

class Solution2(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        def format(discount, x):
            return "${:d}.{:02d}".format(*divmod(int(x[1:])*(100-discount), 100)) if x[0] == '$' and x[1:].isdigit() else x

        return " ".join(format(discount, x) for x in sentence.split())