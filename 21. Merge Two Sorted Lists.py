# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None or list2 is None:
            return list1 or list2
        
        current = ListNode(0)
        T = current
        while list1 and list2:
            if list1.val <= list2.val:
                T.next = list1
                list1 = list1.next
            else:
                T.next = list2
                list2 = list2.next
            T = T.next
        T.next = list1 or list2 
        return current.next

def print_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print("->".join(vals))

s = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list2 = ListNode(1)
list2.next = ListNode(3)
merged = s.mergeTwoLists(list1, list2)
print_list(merged)  # Expected: 1->1->2->3

# Test case: list1 = 1->2->3->10, list2 = 3->5->6->10->11
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(10)

list2 = ListNode(3)
list2.next = ListNode(5)
list2.next.next = ListNode(6)
list2.next.next.next = ListNode(10)
list2.next.next.next.next = ListNode(11)

merged = s.mergeTwoLists(list1, list2)
print_list(merged)  # Expected: 1->2->3->3->5->6->10->10->11

# Recreate lists for Solution2
list1_r = ListNode(1)
list1_r.next = ListNode(2)
list1_r.next.next = ListNode(3)
list1_r.next.next.next = ListNode(10)

list2_r = ListNode(3)
list2_r.next = ListNode(5)
list2_r.next.next = ListNode(6)
list2_r.next.next.next = ListNode(10)
list2_r.next.next.next.next = ListNode(11)

# Solution2 with recursion

class Solution2:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

s2 = Solution2()
merged2 = s2.mergeTwoLists(list1_r, list2_r)
print_list(merged2)  # Expected: 1->2->3->3->5->6->10->10->11