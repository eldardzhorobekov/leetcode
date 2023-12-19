from queue import Queue


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_neighbor(candidate: str, target: str) -> bool:
            if len(candidate) != len(target):
                return False
            
            wrong_ch_occured = False
            for i in range(len(candidate)):
                if candidate[i] != target[i]:
                    if wrong_ch_occured:
                        return False
                    wrong_ch_occured = True

            return True

        def bfs() -> None:
            q = Queue()
            distance[beginWord] = 0
            q.put(beginWord)
            
            while not q.empty():
                node = q.get()
                for word in wordList:
                    if distance[word] is None and is_neighbor(word, node):
                        distance[word] = distance[node] + 1
                        q.put(word)

        distance = {word: None for word in wordList}
        bfs()
        if endWord not in distance or distance[endWord] is None:
            return 0
        return distance[endWord] + 1
