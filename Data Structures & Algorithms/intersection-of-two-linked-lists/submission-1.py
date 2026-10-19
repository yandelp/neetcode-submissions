class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #create node pointers at the start of both lists
        a, b = headA, headB
        while a != b: #while node a is not node b
            a = a.next if a else headB # set a to a.next if a is not null, else set it to headb
            b = b.next if b else headA # set b to b.next if b is not null, else set to heada
        return a #when this process is finished, both are equal.
