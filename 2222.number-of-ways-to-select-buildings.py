#
# @lc app=leetcode id=2222 lang=python3
#
# [2222] Number of Ways to Select Buildings
#

# @lc code=start
import itertools

class Solution:
    def numberOfWays(self, s: str) -> int:
        def ones_before(i: int) -> int:
            if i == 0:
                return 0
            return prefix_sum[i - 1]

        def ones_after(i: int) -> int:
            return prefix_sum[length - 1] - prefix_sum[i]

        def zeros_before(i: int) -> int:
            return i - ones_before(i)

        def zeros_after(i: int) -> int:
            return (length - i - 1) - ones_after(i)

        length = len(s)
        arr = list(map(int, s))
        prefix_sum = list(itertools.accumulate(arr))
        answer = 0
        for i, val in enumerate(arr):
            if val == 0:
                answer += ones_before(i) * ones_after(i)
            else:
                answer += zeros_before(i) * zeros_after(i)
        return answer
# @lc code=end
