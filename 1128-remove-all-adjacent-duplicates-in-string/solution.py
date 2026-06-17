class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[0]
        for i in s:
            if i==st[-1]:
                st.pop()
            else:
                st.append(i)
        return ''.join(st[1:])
