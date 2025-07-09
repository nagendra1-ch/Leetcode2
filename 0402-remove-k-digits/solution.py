class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if k == len(num):
            return '0'
        for i in num:
            while stack and i < stack[-1] and k:
                stack.pop()
                k -= 1
            stack.append(i)
            
        while k:
            stack.pop()
            k -= 1

        result = ''.join(stack).lstrip("0")

        return result if result else '0'
