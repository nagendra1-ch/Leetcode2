# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        current=head
        while current!=None:
            length+=1
            current=current.next
        current=head
        print(length)
        count=0
        while current!=None:
            count+=1
            if count==length//2+1:
                return current
            current=current.next
