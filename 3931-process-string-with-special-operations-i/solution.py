class Solution:
    def processStr(self, s: str) -> str:
        result=[]
        for j in s:
            if j=='*':
                if result:
                
                    result. pop() 
            elif j=='%':
                result=result[::-1]
            elif j=='#':
                result+=result
            else:
                result. append(j)
        result="".join(result)
        return result
