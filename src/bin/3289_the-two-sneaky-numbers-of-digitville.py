#
# @lc app=leetcode id=3289 lang=python3
#
# [3289] The Two Sneaky Numbers of Digitville
#

# @lc code=start
from collections import Counter


class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        return [num for num, count in Counter(nums).items() if count == 2]


# @lc code=end
