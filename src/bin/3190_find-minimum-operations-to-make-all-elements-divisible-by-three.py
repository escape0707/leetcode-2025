#
# @lc app=leetcode id=3190 lang=python3
#
# [3190] Find Minimum Operations to Make All Elements Divisible by Three
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return sum(map(lambda num: min(1, num % 3), nums))

# @lc code=end
