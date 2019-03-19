'''
Given a linked list, remove the n-th node from the end of list and return its head.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p = head
        listNode_length = 0
        
        while p.next != None:
            listNode_length += 1
            p = p.next
        p = dummy
        
        for i in range(listNode_length-n+1):
            p = p.next
        p.next = p.next.next
        
        return dummy.next