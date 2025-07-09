class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        flag=True
        d={']':'[','}':'{',')':'('}
        for i in s:
            print(i)
            if i in '[{(':
                stack.append(i)
            elif i in']})' :
                if len(stack)!=0 and stack[-1]==d[i]:
                    stack.pop()
                else :
                    return False
        print(stack)
        if len(stack)==0:
            return True
        else:
            return False  
