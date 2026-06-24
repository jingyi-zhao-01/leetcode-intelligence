# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: capitalize-the-title
# source_path: LeetCode-Solutions-master/Python/capitalize-the-title.py
# solution_class: Solution
# submission_id: 2bcacd2c8574dc11e60cbf800e13bb909df0795f
# seed: 905203943

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title = list(title)
        j = 0
        for i in xrange(len(title)+1):
            if i < len(title) and title[i] != ' ':
                title[i] = title[i].lower()
                continue
            if i-j > 2:
                title[j] = title[j].upper()
            j = i+1
        return "".join(title)