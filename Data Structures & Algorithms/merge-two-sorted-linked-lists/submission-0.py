class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        output = dummy
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                output.next = curr1
                curr1 = curr1.next
            else:
                output.next = curr2
                curr2 = curr2.next
            output = output.next
        
        output.next = curr1 if curr1 else curr2
        return dummy.next