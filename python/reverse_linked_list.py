'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        print head
        temp = head
        new = head.next
        if new != None:
            head.next = None
            while (temp != None):
                # if temp.next == None:
                #     break
                temp = new
                if temp.next != None:
                    new = temp.next
                    # if new == None:
                    #     break
                else:
                    temp.next = head
                    head = temp
                    return head
                temp.next = head
                head = temp
        else:
            return head


#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
