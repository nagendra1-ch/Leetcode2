class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        ans = []

        word1 = set(words[0])

        for char in word1:
            frequency = min([word.count(char) for word in words])
            ans += [char] * frequency

        return ans
            
