#! Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited_nodes = set()
        current_node = head

        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next

        return False
    
s = Solution()
node1 = ListNode(3)
node2 = ListNode(2)
node1.next = node2
node2.next = node1
print(s.hasCycle(node1))  # True