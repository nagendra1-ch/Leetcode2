class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence=sentence.split()
        l=[]
        c=2
        for word in sentence:
            if word[0] in 'aeiouAEIOU':
                l.append(word+'m'+c*'a')
            else:
                l.append(word[1:]+word[0]+'m'+c*'a')
            c+=1
        return ' '.join(l)
