#
# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#

# @lc code=start
import itertools


class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        equal_sum = total // 3
        find = 1
        j = 0
        for j, prefix_sum in enumerate(itertools.accumulate(arr)):
            if prefix_sum == equal_sum * find:
                find += 1
                if find == 3:
                    break
        return find == 3 and j + 1 < len(arr)


# @lc code=end
