#
# @lc app=leetcode id=3668 lang=python3
#
# [3668] Restore Finishing Order
#

# @lc code=start
class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        friends_set = set(friends)
        return list(filter(friends_set.__contains__, order))


# @lc code=end
