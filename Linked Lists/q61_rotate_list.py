# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Approach:
1. Maintain two pointers one slow and the other fast Initialize slow pointer to None and fast pointer to head.
2. Maintain the count of number of nodes traversed so far in a variable
3. If count == k, set the slow pointer to head.
4. If count > k, keep on moving the slow pointer until the fast pointer encounters null
5. If k > no of elements in the linked list, slow pointer will be None even after the fast pointer has tracersed the
entire linked list.
6. In this case, set the number of rotations  = number of rotations % count of the number of nodes in the linked list
and again call the method with the number of rotations
"""


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If there is no element or the number of rotations to be done is 0, return the head simply
        if not head or k == 0:
            return head
        # If there is a single element in the linked list, no matter how many rotations we make, the end result will be
        # the element itself
        elif not head.next:
            return head
        # Initialize slow ptr
        slow_ptr = None
        # Initialize fast ptr
        fast_ptr = head
        # prev_fast_ptr holds the last element in the linked list
        prev_fast_ptr = None
        # nodes_checked holds the count of the number of nodes in the linked list
        nodes_checked = 0

        while fast_ptr:
            if nodes_checked == k:
                slow_ptr = head
            elif nodes_checked > k:
                slow_ptr = slow_ptr.next
            nodes_checked += 1
            prev_fast_ptr = fast_ptr
            fast_ptr = fast_ptr.next
        if slow_ptr:
            modified_head = slow_ptr.next
            slow_ptr.next = None
            temp = head
            head = modified_head
            prev_fast_ptr.next = temp
        else:
            no_of_rotations = k % nodes_checked
            head = self.rotateRight(head, no_of_rotations)
        return head
