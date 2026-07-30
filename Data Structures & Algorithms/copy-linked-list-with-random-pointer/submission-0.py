"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old =collections.defaultdict(lambda: Node(0))
        old[None] = None

        cur = head
        while cur:
            old[cur].val= cur.val
            old[cur].next = old[cur.next]
            old[cur].random = old[cur.random]
            cur = cur.next
        return old[head]
        