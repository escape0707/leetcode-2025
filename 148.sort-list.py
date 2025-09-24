#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def get_list_length(node: Optional[ListNode]) -> int:
    length = -1
    while node:
        length += 1
        node = node.next
    return length


def advance(node: ListNode, step: int) -> ListNode:
    while node.next and step:
        node = node.next
        step -= 1
    return node


def divide(prev: ListNode, step: int) -> tuple[ListNode, ListNode, ListNode]:
    left = prev
    mid = advance(left, step)
    right = advance(mid, step)
    return (left, mid, right)


def merge(left: ListNode, mid: ListNode, right: ListNode):
    # (left, mid] (mid, right]
    l = left.next
    l_end = mid.next
    r = mid.next
    r_end = right.next
    assert l and l_end and r
    new_list = ListNode()
    tail = new_list
    while l is not l_end and r is not r_end:
        assert l and r
        if l.val < r.val:
            tail.next = l
            l = l.next
        else:
            tail.next = r
            r = r.next
        tail = tail.next
    # concat
    left.next = new_list.next
    if l is not l_end:
        tail.next = l
        mid.next = r_end
        return mid
    # else, r is not r_end
    tail.next = r
    # right.next = r_end
    return right


def sort_with_step(linked_list: ListNode, step: int):
    # (left, mid] (mid, right]
    (left, mid, right) = divide(linked_list, step)
    while mid is not right:
        right = merge(left, mid, right)
        (left, mid, right) = divide(right, step)


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linked_list = ListNode(next=head)
        length = get_list_length(linked_list)
        step = 1
        while step < length:
            sort_with_step(linked_list, step)
            step *= 2
        return linked_list.next


# @lc code=end
