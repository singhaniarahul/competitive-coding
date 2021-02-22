# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        length = 0
        while(temp != None):
            length += 1
            temp = temp.next
        answer = 0
        #print(length)
        while(length>0):
            answer += (pow(2,length-1)*head.val)
            head = head.next
            length -= 1
        return answer