#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

from typing import Optional, Self


class ListNode:
    def __init__(self, val: int = 0, next: Optional[Self] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return repr(LinkedListIter(self))


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
#         self.val = val
#         self.next = next
import copy
from collections.abc import Iterable, Iterator
from typing import Optional, Self


class LinkedListIter(Iterator[ListNode]):
    def __init__(self, curr: Optional[ListNode]):
        self.curr = curr

    def __bool__(self) -> bool:
        return bool(self.curr)

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> ListNode:
        if not self.curr:
            raise StopIteration
        result = self.curr
        self.curr = self.curr.next
        return result

    def __repr__(self) -> str:
        return "->".join(map(repr, copy.copy(self)))

    def __copy__(self) -> Self:
        return type(self)(self.curr)


class LinkedList(Iterable[ListNode]):
    def __init__(self, prev: ListNode, tail: ListNode):
        self.prev = prev
        self.tail = tail

    @classmethod
    def new(cls) -> Self:
        prev = ListNode()
        return cls(prev, prev)

    def __bool__(self) -> bool:
        return not self.is_empty()

    def __iter__(self) -> LinkedListIter:
        return LinkedListIter(self.prev.next)

    def __repr__(self) -> str:
        return f"LinkedList({repr(iter(self))})"

    def cut_off(self, prev: ListNode) -> Self:
        if prev is self.tail:
            return self.new()
        new_prev, prev.next = ListNode(next=prev.next), None
        res = type(self)(new_prev, self.tail)
        self.tail = prev
        return res

    def head(self) -> Optional[ListNode]:
        return self.prev.next

    def __head(self) -> ListNode:
        head = self.head()
        assert head
        return head

    def is_empty(self) -> bool:
        return self.prev.next is None

    def peek(self) -> int:
        return self.__head().val

    def pop(self) -> ListNode:
        head = self.__head()
        self.prev.next, head.next = head.next, None
        if self.is_empty():
            self.tail = self.prev
        return head

    def append(self, node: ListNode):
        self.tail.next = node
        self.tail = node

    def extend(self, linked_list: Self):
        if not linked_list:
            return
        self.tail.next, linked_list.prev.next = linked_list.prev.next, None
        self.tail = linked_list.tail
        linked_list.tail = linked_list.prev

    def merge_sort(self):
        length, _ = get_list_length_tail(self.prev)
        self.__merge_sort(length)

    def __merge_sort(self, length: int):
        step = 1
        while step < length:
            self.__sort_at_step(step)
            step *= 2

    def __sort_at_step(self, step: int):
        # (l, m] (m, r]
        prev = self.prev
        while slices := self.__divide(prev, step):
            left, right, after = slices
            merged_list = self.__merge(left, right)
            self.extend(merged_list)
            prev = self.tail
            self.extend(after)

    def __divide(self, prev: ListNode, step: int) -> None | tuple[Self, Self, Self]:
        """
        Try to cut out `step`s nodes after `prev` into the `left` list,
        then cut out at least one, at most `step`s more nodes into the `right` list.

        If not enough nodes for cutting, return None

        Returns the two lists and the new `prev` for the node originally after `right`.
        """
        l = prev
        m = advance(l, step)
        r = advance(m, step)
        if m is r:
            return None
        left = self.cut_off(l)
        right = left.cut_off(m)
        after = right.cut_off(r)
        return left, right, after

    @classmethod
    def __merge(
        cls,
        left: Self,
        right: Self,
    ) -> Self:
        merged_list = cls.new()
        while left and right:
            merged_list.append((left if left.peek() < right.peek() else right).pop())
        merged_list.extend(left or right)
        return merged_list


def get_list_length_tail(node: ListNode) -> tuple[int, ListNode]:
    length = 0
    while node.next:
        length += 1
        node = node.next
    return length, node


def advance(node: ListNode, step: int) -> ListNode:
    """
    Seek `step`s forward from `node`, early stop at the last valid `ListNode`
    """
    while node.next and step:
        node = node.next
        step -= 1
    return node


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(next=head)
        _, tail = get_list_length_tail(prev)
        linked_list = LinkedList(prev, tail)
        linked_list.merge_sort()
        return linked_list.head()


def main():
    linked_list = LinkedList.new()
    for val in (-1, 5, 3, 4, 0):
        linked_list.append(ListNode(val))
    print(LinkedListIter(Solution().sortList(linked_list.head())))

# @lc code=end


if __name__ == "__main__":
    main()
