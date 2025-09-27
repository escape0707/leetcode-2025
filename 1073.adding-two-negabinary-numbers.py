#
# @lc app=leetcode id=1073 lang=python3
#
# [1073] Adding Two Negabinary Numbers
#

# @lc code=start
import itertools


class Solution:
    def _addNegabinary_naive(self, arr1: list[int], arr2: list[int]) -> list[int]:
        res: list[int] = []
        carry1, carry2 = 0, 0
        for x, y in itertools.zip_longest(reversed(arr1), reversed(arr2), fillvalue=0):
            total = x + y + carry1
            match total:
                case 0 | 1:
                    res.append(total)
                    carry1, carry2 = carry2, 0
                case 2 | 3:
                    res.append(total - 2)
                    print(carry1, carry2)
                    if carry2 == 0:
                        carry1, carry2 = 1, 1
                    elif carry2 == 1:
                        carry1, carry2 = 0, 0
                    else:
                        raise ValueError
                    # But if you think about this,
                    # it means that if the new carry is 1 in base 2,
                    # it should be -1 in base -2.
                    # And if the new carry is 0 in base 2,
                    # it should remain 0 in base -2.
                case _:
                    raise ValueError
        res.extend((carry1, carry2))
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        res.reverse()
        return res

    def addNegabinary(self, A: list[int], B: list[int]) -> list[int]:
        res: list[int] = []
        carry = 0
        while A or B or carry:
            carry += (A or [0]).pop() + (B or [0]).pop()
            res.append(carry & 1)
            carry = -(carry >> 1)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        res.reverse()
        return res


# @lc code=end
