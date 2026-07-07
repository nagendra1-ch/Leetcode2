class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        n=len(sentence)
        k=len(searchWord)
        for i in range(n):
            if len(sentence[i])>=k and sentence[i][:k]==searchWord:
                return i+1
        return -1
