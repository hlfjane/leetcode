# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None
"""the linked list is as below"""
"""(val, (val, (val, (val, None))))"""
class Solution(object):
    def __init__(self):
        pass
    def add_num_with_carry_over(self, n1, n2, n3):
        sum = n1 + n2 + n3
        carry_over = 0
        if sum >=10:
            carry_over = 1
            sum = sum - 10
        return sum, carry_over

    def addTwoNumbers(self, l1, l2):
        sum, carry_over = 0, 0
        target_list=ListNode(0)
        l3 = target_list
        while l1 or l2:
            if l1 is None:
                sum, carry_over = self.add_num_with_carry_over(0, l2.val, l3.val)
                l2 = l2.next
            elif l2 is None:
                sum, carry_over = self.add_num_with_carry_over(l1.val, 0, l3.val)
                l1 = l1.next
            else:
                sum, carry_over = self.add_num_with_carry_over(l1.val, l2.val, l3.val)
                l1 = l1.next
                l2 = l2.next
            l3.val = sum
            if l1 is None and l2 is None:
                if carry_over != 0:
                    l3.next = ListNode(carry_over)
                    l3 = l3.next
            else:
                l3.next = ListNode(carry_over)
                l3 = l3.next
        return target_list
