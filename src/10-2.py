def addWord(self, word: str) -> None:
    """
    데이터 구조에 단어 추가
    """
    cur = self.root
    for c in word:
        if c not in cur.children:
            cur.children[c] = TrieNode()
        cur = cur.children[c]

    cur.isWord = True