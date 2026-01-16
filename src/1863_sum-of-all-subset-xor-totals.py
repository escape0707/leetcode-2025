#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
import itertools
import functools
import operator


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        return functools.reduce(operator.or_, nums) << (len(nums) - 1)


def main():
    print(Solution().subsetXORSum([3, 4, 5, 6, 7, 8]))


# @lc code=end

if __name__ == "__main__":
    main()
