class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mcode=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result=[]
        for word in words:
            s=''
            for ch in word:
                s+=mcode[ord(ch)-97]
            result.append(s)
        return len(set(result))
