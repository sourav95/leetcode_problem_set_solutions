# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Approach
1. Keep three pointers to track the elements
2. ptr1 will keep a track of the next element in case there are duplicates
3. ptr2 will be used to check for duplicate elements
4. ptr3 to traverse the linked list
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ptr1 = None
        ptr2 = None
        ptr3 = head
        flag = 0
        same = False
        while ptr3:
            if ptr2 and ptr2.val == ptr3.val:
                same = True
                ptr3 = ptr3.next
            else:
                if same:
                    if ptr1:
                        ptr1.next = ptr3
                    else:
                        head = ptr3
                    same = False
                else:
                    if flag == 1:
                        ptr1 = ptr2
                    else:
                        flag = 1
                ptr2 = ptr3
                ptr3 = ptr3.next
        if same:
            if ptr1:
                ptr1.next = ptr3
            else:
                head = ptr3
        return head