# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: phone-number-prefix
# source_path: LeetCode-Solutions-master/Python/phone-number-prefix.py
# solution_class: Solution2
# submission_id: 7e9b9ad4df35b3e4e6e876a468d24bb89b778558
# seed: 1211457248

# Time:  O(l * nlogn)
# Space: O(1)

# sort

class Solution2(object):
    def phonePrefix(self, numbers):
        """
        :type numbers: List[str]
        :rtype: bool
        """
        class Trie(object):
            def __init__(self):
                self.__nodes = []
                self.__new_node()
            
            def __new_node(self):
                self.__nodes.append([-1]*(10+1))
                return len(self.__nodes)-1

            def add(self, s):
                made = False
                curr = 0
                for i in xrange(len(s)):
                    x = ord(s[i])-ord('0')
                    if self.__nodes[curr][x] == -1:
                        self.__nodes[curr][x] = self.__new_node()
                        made = True
                    elif self.__nodes[self.__nodes[curr][x]][-1] == True:
                        return False
                    curr = self.__nodes[curr][x]
                self.__nodes[curr][-1] = True
                return made
    
        trie = Trie()
        return all(trie.add(x) for x in numbers)