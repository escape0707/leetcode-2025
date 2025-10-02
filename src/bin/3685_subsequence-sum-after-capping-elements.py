#
# @lc app=leetcode id=3685 lang=python3
#
# [3685] Subsequence Sum After Capping Elements
#


# @lc code=start
class Solution:
    def subsequenceSumAfterCapping_2_dimensional(self, nums: list[int], k: int) -> list[bool]:
        n = len(nums)
        dp = [[False] * (k + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True
        nums.sort()
        answer: list[bool] = []
        for i, num in enumerate(nums):
            for x in range(len(answer) + 1, num):
                answer.append(
                    any(
                        k >= x * cnt and dp[i][k - x * cnt]
                        for cnt in range(0, n - i + 1)
                    )
                )
            for v in range(k, -1, -1):
                dp[i + 1][v] = dp[i][v] or v >= num and dp[i][v - num]
        answer += [dp[n][k]] * (n - len(answer))
        return answer

    def subsequenceSumAfterCapping(self, nums: list[int], k: int) -> list[bool]:
        n = len(nums)
        dp = [True] + [False] * k
        nums.sort()
        answer: list[bool] = []
        for i, num in enumerate(nums):
            for x in range(len(answer) + 1, num):
                answer.append(
                    any(
                        k >= x * cnt and dp[k - x * cnt]
                        for cnt in range(0, n - i + 1)
                    )
                )
            for v in range(k, 0, -1):
                dp[v] = dp[v] or v >= num and dp[v - num]
        answer += [dp[k]] * (n - len(answer))
        return answer

def main():
    nums = [4, 3, 2, 4]
    k = 5
    ans = Solution().subsequenceSumAfterCapping(nums, k)
    print(ans)


# @lc code=end

if __name__ == "__main__":
    main()
