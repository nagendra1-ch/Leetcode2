# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        dummy=head
        c=1
        while dummy.next!=None:
            dummy=dummy.next
            c+=1
        dummy.next=head
        t=head
        k=k%c
        

        for i in range(c-k-1):
            t=t.next
        res=t.next
        t.next=None
        return res
        

