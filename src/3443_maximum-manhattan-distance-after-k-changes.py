#
# @lc app=leetcode id=3443 lang=python3
#
# [3443] Maximum Manhattan Distance After K Changes
#

# @lc code=start
from collections import Counter


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def m_dist() -> int:
            return abs(x) + abs(y)

        cnt: Counter[str] = Counter()
        x, y = 0, 0
        res = 0
        for c in s:
            cnt[c] += 1
            match c:
                case "N":
                    y += 1
                case "E":
                    x += 1
                case "W":
                    x -= 1
                case "S":
                    y -= 1
                case _:
                    raise ValueError
            curr_dist = m_dist()
            optimized_dist = (
                curr_dist
                + min(k, (min(cnt["N"], cnt["S"]) + min(cnt["E"], cnt["W"]))) * 2
            )
            res = max(res, optimized_dist)
        return res


# @lc code=end
