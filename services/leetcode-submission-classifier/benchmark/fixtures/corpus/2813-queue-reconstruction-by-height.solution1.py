# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: queue-reconstruction-by-height
# source_path: LeetCode-Solutions-master/Python/queue-reconstruction-by-height.py
# solution_class: Solution
# submission_id: 5b345a23f490de5ec14d142b84f1b3842286cdd2
# seed: 251259962

# Time:  O(n * sqrt(n))
# Space: O(n)

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda h_k: (-h_k[0], h_k[1]))

        blocks = [[]]
        for p in people:
            index = p[1]

            for i, block in enumerate(blocks):
                if index <= len(block):
                    break
                index -= len(block)
            block.insert(index, p)

            if len(block) * len(block) > len(people):
                blocks.insert(i+1, block[len(block)/2:])
                del block[len(block)/2:]

        return [p for block in blocks for p in block]