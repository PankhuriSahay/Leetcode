# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next

        index = 1
        first = -1
        last = -1
        min_dist = float('inf')
        max_dist = -1

        while curr.next:
            next_node = curr.next

            is_critical = (
                (curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)
            )

            if is_critical:
                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - last)
                    max_dist = index - first

                last = index

            prev = curr
            curr = curr.next
            index += 1

        if max_dist == -1:
            return [-1, -1]

        return [min_dist, max_dist]