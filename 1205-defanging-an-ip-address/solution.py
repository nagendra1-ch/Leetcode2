class Solution:
    def defangIPaddr(self, address: str) -> str:
        new=""
        for i in address:
            if i=='.':
                new=new+"[.]"
            else:
                new=new+i
        return new
