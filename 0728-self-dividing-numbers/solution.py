class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        def issdn(n):
            n1=n
            while n1:
                r=n1%10
                if r==0:
                    return False
                elif n%r!=0:
                    return False
                n1//=10
            return True
                
        for i in range(left,right+1):
            if issdn(i):
                ans.append(i)
        return ans
