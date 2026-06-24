# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: implement-queue-using-stacks
# source_path: LeetCode-Solutions-master/Python/implement-queue-using-stacks.py
# solution_class: Solution
# submission_id: 847920527f5d3062a2ea26262716ec8bbd3fce84
# seed: 2947179908

# Time:  O(1), amortized
# Space: O(n)

class MyQueue(object):

    def __init__(self):
        self.A, self.B = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.B.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        return self.B[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.A and not self.B
