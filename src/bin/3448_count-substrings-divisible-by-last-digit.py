#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        dp = [[0] * 10 for _ in range(10)]
        for val in map(int, s):
            for divisor in range(1, 10):
                aux = [0] * divisor
                aux[val % divisor] += 1
                for remainder in range(divisor):
                    aux[(remainder * 10 + val) % divisor] += dp[divisor][remainder]
                dp[divisor] = aux
            ans += dp[val][0]
        return ans

# @lc code=end
