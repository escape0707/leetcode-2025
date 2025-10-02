#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#


# @lc code=start
import copy


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        answer: list[list[int]] = []
        combination = list(range(1, k + 1))
        while True:
            answer.append(copy.copy(combination))
            for i in reversed(range(k)):
                if combination[i] != n - k + i + 1:
                    break
            else:
                break
            combination[i] += 1
            for j in range(i + 1, k):
                combination[j] = combination[j - 1] + 1

        return answer


def main():
    n, k = 4, 2
    print(Solution().combine(n, k))


# @lc code=end

if __name__ == "__main__":
    main()
