# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        tail = head

        while tail.next:
            tail = tail.next
            count += 1
        
        e = count - n


        if count + 1 == n:
            return head.next

        
        curr = head
        while e > 0:
            curr = curr.next
            e -= 1
        
        curr.next = curr.next.next
            
        
        return head


            