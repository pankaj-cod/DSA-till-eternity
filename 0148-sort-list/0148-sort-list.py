# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # we have to sort a linkedlist
        # merge sort is the best way as it is nlogn
        # first make two halves using fast and slow pointer
        if not head or not head.next:
            return head
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # splitting list into 2
        mid = slow.next
        slow.next=None

        left = self.sortList(head)
        right = self.sortList(mid)

        #merging
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val<right.val:
                tail.next=left
                left = left.next
            else:
                tail.next = right 
                right = right.next
            tail = tail.next
        tail.next = left if left else right

        return dummy.next 