# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return _reverseList(head)


def _reverseList(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return _reverseList(next, head)