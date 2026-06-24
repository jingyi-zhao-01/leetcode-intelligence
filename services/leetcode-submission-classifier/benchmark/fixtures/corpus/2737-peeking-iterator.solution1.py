# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: peeking-iterator
# source_path: LeetCode-Solutions-master/Python/peeking-iterator.py
# solution_class: Solution
# submission_id: cdd9db40aa409d6a9c26094d531aafe370c8e67a
# seed: 1224235327

# Time:  O(1) per peek(), next(), hasNext()
# Space: O(1)

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.val_ = None
        self.has_next_ = iterator.hasNext()
        self.has_peeked_ = False


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.has_peeked_:
            self.has_peeked_ = True
            self.val_ = self.iterator.next()
        return self.val_

    def next(self):
        """
        :rtype: int
        """
        self.val_ = self.peek()
        self.has_peeked_ = False
        self.has_next_ = self.iterator.hasNext()
        return self.val_

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_next_



