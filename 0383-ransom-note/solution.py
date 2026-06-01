class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom=list(ransomNote)
        magazine=list(magazine)
        result=[]
        for i in ransom:
            if i in magazine:
                magazine.remove(i)
                result+=i
        return len(result)==len(ransomNote)
