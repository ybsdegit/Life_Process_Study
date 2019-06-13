#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/6/12 16:56
# @author: Paulson●Wier
# @file: 链表.py
# @desc:

# 链表
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# 反转链表

# 单向链表
class ListNode1:
    def __init__(self, val):
        self.val = val
        self.next = None

    # in python next is a reversed word
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

class Solution:
    def threeSum(self, numbers):
        triplets = []
        length = len(numbers)
        if length < 3:
            return triplets
        numbers.sort()
        for i in range(length):
            target = 0 - numbers[i]

            # 2 sum
            hashmap = {}
            for j in range(i+1, length):
                item_j = numbers[j]
                if (target - item_j) in hashmap:
                    triplet = [numbers[i], target-item_j, item_j]
                    if triplet not in triplets:
                        triplets.append(triplet)
                else:
                    hashmap[item_j] = j
        return triplets

s = Solution()
x = [-1, 0, 1, 2, -1, -4]
y = s.threeSum(x)
print(y)
