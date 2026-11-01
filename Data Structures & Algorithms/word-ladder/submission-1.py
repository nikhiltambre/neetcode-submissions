from collections import deque
class Solution:

    def ladderLength(self, beginWord: str, endWord: str, Listofwords: List[str]) -> int:
        wordList=set(Listofwords)
        if endWord not in wordList:
            return 0
        visited={beginWord}
        queue=deque()
        queue.append((beginWord,1))
        while queue:
            node,dist=queue.popleft()
            if node==endWord:
                return dist
            for i in range(len(node)):
                for j in range(26):
                    c = chr(ord("a") + j)
                    new_word = node[:i] + c + node[i+1:]
                    if new_word in wordList and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word,dist+1))
        return 0
            

        