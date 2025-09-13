# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        intersection_node = None
        visited_nodes = set()

        currentA = headA
        currentB = headB

        while currentA:
            visited_nodes.add(currentA)
            currentA = currentA.next

        while currentB:
            if currentB in visited_nodes:
                return currentB
            currentB = currentB.next

        return None

s = Solution()
# Create first linked list: 4 -> 1 \
# Shared intersection part
intersect_node = ListNode(2)
intersect_node.next = ListNode(4)

# First list: 1 -> 9 -> 1 -> 2 -> 4
nodeA1 = ListNode(1)  
nodeA2 = ListNode(9)
nodeA3 = ListNode(1)

nodeA1.next = nodeA2
nodeA2.next = nodeA3
nodeA3.next = intersect_node  # <-- Shared node starts here

# Second list: 3 -> 2 -> 4
nodeB1 = ListNode(3)
nodeB1.next = intersect_node  # <-- Points directly to same shared node
result = s.getIntersectionNode(nodeA1, nodeB1)
if result:
    print(result.val)
else:
    print("No intersection found")

#! Better solution:

class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA  

