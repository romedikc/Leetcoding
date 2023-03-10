# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def linked_list_to_array(head):
            curr = head
            arr = []
            while curr:
                arr.append(curr.val)
                curr = curr.next
            return arr

        # swapping
        array = linked_list_to_array(head)
        front, back = k - 1, len(array) - k
        array[front], array[back] = array[back], array[front]

        # converting back to LL
        curr = head
        i = 0
        while curr:
            curr.val = array[i]
            i += 1
            curr = curr.next
        return head
