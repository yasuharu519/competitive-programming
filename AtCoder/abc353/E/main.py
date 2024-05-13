#!/usr/bin/env python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> int:
        current = self.root

        prev_count = 0
        length = 0
        contributions = []
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                current.children[c] = TrieNode()
                current = current.children[c]
            current.count += 1
            prev_count = current.count - 1
            length += 1
            contributions.append((length, prev_count))
        result = 0
        added = 0
        for length, prev_count in reversed(contributions):
            if prev_count > added:
                result += length * (prev_count - added)
                added = prev_count
        return result

def main():
    N = int(input().strip())
    S = list(input().strip().split())

    trie = Trie()
    result = 0
    trie.insert(S[0])

    for s in S[1:]:
        result += trie.insert(s)
    print(result)
    return

if __name__ == '__main__':
    main()