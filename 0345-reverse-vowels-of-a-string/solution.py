class Solution:
    def reverseVowels(self, s: str) -> str:
        s1=set('aeiouAEIOU')
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            while i<j and s[i] not in s1:
                i+=1
            while i<j and s[j] not in s1:
                j-=1
            if i<j:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1

            
        return ''.join(s)
