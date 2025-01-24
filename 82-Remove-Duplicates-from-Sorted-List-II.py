# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        data = list()
        
        c = head
        dummy = ListNode(0)
        d = dummy

        while c:
            data.append(c.val)
            c = c.next

        c_data = Counter(data)

        for k , v in c_data.items():
            if v == 1:
                n = ListNode(k)
                d.next = n
                d = d.next

        return dummy.next