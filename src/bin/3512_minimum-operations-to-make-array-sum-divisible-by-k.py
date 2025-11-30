#
# @lc app=leetcode id=3512 lang=python3
#
# [3512] Minimum Operations to Make Array Sum Divisible by K
#

# @lc code=start
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(nums) % k
# @lc code=end
