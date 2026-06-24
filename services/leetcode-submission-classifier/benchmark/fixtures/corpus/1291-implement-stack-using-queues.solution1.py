# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: implement-stack-using-queues
# source_path: LeetCode-Solutions-master/Python/implement-stack-using-queues.py
# solution_class: Solution
# submission_id: 5c1d9ef6f47f367383cf82c8f11e1427b929ae7c
# seed: 409509927

# Time: push: O(n), pop: O(1), top: O(1)
# Space: O(n)

import collections


class Queue(object):
    def __init__(self):
        self.data = collections.deque()

    def push(self, x):
        self.data.append(x)

    def peek(self):
        return self.data[0]

    def pop(self):
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0


class Stack(object):
    # initialize your data structure here.
    def __init__(self):
        self.q_ = Queue()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q_.push(x)
        for _ in xrange(self.q_.size() - 1):
            self.q_.push(self.q_.pop())

    # @return nothing
    def pop(self):
        self.q_.pop()

    # @return an integer
    def top(self):
        return self.q_.peek()

    # @return an boolean
    def empty(self):
        return self.q_.empty()


# Time: push: O(1), pop: O(n), top: O(1)
# Space: O(n)
class Stack2(object):
    # initialize your data structure here.
    def __init__(self):
        self.q_ = Queue()
        self.top_ = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q_.push(x)
        self.top_ = x

    # @return nothing
    def pop(self):
        for _ in xrange(self.q_.size() - 1):
            self.top_ = self.q_.pop()
            self.q_.push(self.top_)
        return self.q_.pop() 

    # @return an integer
    def top(self):
        return self.top_

    # @return an boolean
    def empty(self):
        return self.q_.empty()

