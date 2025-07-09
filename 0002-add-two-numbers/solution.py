# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_sum=''
        l2_sum=''
        curr=l1
        while curr!=None:
            l1_sum=str(curr.val)+l1_sum
            curr=curr.next
        curr=l2
        while curr!=None:
            l2_sum=str(curr.val)+l2_sum
            curr=curr.next
        
        num=int(l1_sum)+int(l2_sum)
        if num == 0:
            return ListNode(0)
        head=None
        print(num)
        while num>0:
            node=ListNode(num%10)
            if head==None:
                head=node
            else:
                node.next=head
                head=node
            num//=10
        curr=head
        prev=None
        while curr!=None:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        head=prev

        return head
