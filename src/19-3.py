def chain_from_add(self, word, all_words, chain_length, cache):
    # 순회되었으므로 현재 단어의 값이 직접 반환된다.
    if word in cache:
        return cache[word] + chain_length - 1

    max_chain_length = chain_length
    for i in range(len(word) + 1):
        # 각 글자 추가
        for a in string.ascii_lowercase:
            new_word = word[:i] + a + word[i:]
            # 현재 생성된 단어가 사전에 있는지 확인
            if new_word in all_words:
                # 깊이 탐색
                current_chain_length = self.chain_from_add(
                    new_word, all_words, chain_length + 1, cache)
            if current_chain_length > max_chain_length:
                max_chain_length = current_chain_length

    cache[word] = max_chain_length
    return cache[word]


def longest_subword_additive(self, words):
    all_words = set()
    # 모든 단어를 해시 테이블에 밀어 넣는다.
    for w in words:
        all_words.add(w)

    max_chain_length = 0
    cache = {}
    # 각 단어를 감지하고 탐색한다.
    for w in words:
        current_chain_length = self.chain_from_add(w, all_words, 1, cache)
        if current_chain_length > max_chain_length:
            max_chain_length = current_chain_length

    return max_chain_length
