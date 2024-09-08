'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.prev = None
        
    def next(self, next):
        self.next = next
        
    def prev(self, prev):
        self.prev = prev
        

# def addTwoNumbers(l1,l2):
#     # j = len(l1) - 1
#     result = []
#     pembantu = 0
#     for i in range(len(l2)):
#         print("Pembantu: ", pembantu)
#         dimsum = l1[i]+l2[i]+pembantu
#         print("dinsum : ", dimsum)
#         if dimsum >= 10:
#             leftover = dimsum % 10
#             if leftover > 0:
#                 pembantu = int(dimsum/10)
#             else:
#                 pembantu = 1
#             result.append(leftover)
#         else:
#             pembantu = 0
#             result.append(dimsum)
#         # j -= 1
#     return result

# def addTwoNumbers(l1,l2):
#     # j = len(l1) - 1
#     result = []
#     pembantu = 0
#     for i in range(len(l1)):
#         print("Pembantu: ", pembantu)
#         dimsum = 0
#         if i >= len(l2):
#             dimsum = l1[i] + pembantu
#         else:
#             dimsum = l1[i]+l2[i]+pembantu
#         print("dinsum : ", dimsum)
#         if dimsum >= 10:
#             leftover = dimsum % 10
#             if leftover > 0:
#                 pembantu = int(dimsum/10)
#             else:
#                 pembantu = 1
#             result.append(leftover)
#         else:
#             pembantu = 0
#             result.append(dimsum)
    
#     if pembantu > 0:
#         result.append(pembantu)
#         # j -= 1
#     # while i < len(l2) or pembantu>0
#     return result

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

def addTwoNumberLinkedList(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head    
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
            
    return dummy_head.next


test_l1 = node1
test_l2 = node4
# result = addTwoNumbers(test_l1, test_l2)
result = addTwoNumberLinkedList(test_l1, test_l2)

print(result)