'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = ListNode(0)
        q = ListNode(0)
        p = l1
        q = l2
        new_list = ListNode(0)
        np = new_list
        
        if p == None:
            return q
        elif q == None:
            return p
        else: 
            while p.next != None and q.next != None:
                if p.val <= q.val:
                    np.next = p
                    p = p.next
                    np = np.next
                else:
                    np.next = q
                    q = q.next
                    np = np.next
                
        while p.next != None:
            np.next = p
            np = np.next
            p = p.next
        while q.next != None:
            np.next = q
            np = np.next
            q = q.next
        
        return new_list.next