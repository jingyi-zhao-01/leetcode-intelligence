# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-strings-that-appear-as-substrings-in-word
# source_path: LeetCode-Solutions-master/Python/number-of-strings-that-appear-as-substrings-in-word.py
# solution_class: Solution
# submission_id: 6d71998cfe46647d762a423120d3f4d1667783ee
# seed: 3483712005

# Time:  O(n * l + m), n is the number of patterns
#                    , l is the max length of patterns
#                    , m is the length of word     
# Space: O(t)        , t is the total size of ac automata trie

import collections


class AhoNode(object):
    def __init__(self):
        self.children = collections.defaultdict(AhoNode)
        self.indices = []
        self.suffix = None
        self.output = None


class AhoTrie(object):
    def step(self, letter):
        while self.__node and letter not in self.__node.children:
            self.__node = self.__node.suffix
        self.__node = self.__node.children[letter] if self.__node else self.__root
        return self.__get_ac_node_outputs(self.__node)
    
    def __init__(self, patterns):
        self.__root = self.__create_ac_trie(patterns)
        self.__node = self.__create_ac_suffix_and_output_links(self.__root)
        self.__lookup = set()  # modified
    
    def __create_ac_trie(self, patterns):  # Time: O(n * l), Space: O(t)
        root = AhoNode()
        for i, pattern in enumerate(patterns):
            node = root
            for c in pattern:
                node = node.children[c]
            node.indices.append(i)
        return root

    def __create_ac_suffix_and_output_links(self, root):  # Time: O(n * l), Space: O(t)
        queue = collections.deque()
        for node in root.children.itervalues():
            queue.append(node)
            node.suffix = root

        while queue:
            node = queue.popleft()
            for c, child in node.children.iteritems():
                queue.append(child)
                suffix = node.suffix
                while suffix and c not in suffix.children:
                    suffix = suffix.suffix
                child.suffix = suffix.children[c] if suffix else root
                child.output = child.suffix if child.suffix.indices else child.suffix.output
                
        return root

    def __get_ac_node_outputs(self, node):  # Total Time: O(n), modified
        result = []
        if node not in self.__lookup:  # modified
            self.__lookup.add(node)  # modified
            for i in node.indices:
                result.append(i)
            output = node.output
            while output and output not in self.__lookup:  # modified
                self.__lookup.add(output)  # modified
                for i in output.indices:
                    result.append(i)
                output = output.output
        return result


# ac automata solution

class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        trie = AhoTrie(patterns)
        return sum(len(trie.step(c)) for c in word)