# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        result = dummy
        while list1 is not None and list2 is not None:
            if(list1.val <= list2.val):
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            
            result = result.next
        if list1 is not None:
            result.next = list1
        if list2 is not None:
            result.next = list2
        
        return dummy.next
        
            

        
