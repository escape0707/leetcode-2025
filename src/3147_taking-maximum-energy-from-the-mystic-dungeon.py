#
# @lc app=leetcode id=3147 lang=python3
#
# [3147] Taking Maximum Energy From the Mystic Dungeon
#


# @lc code=start
class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        length = len(energy)
        suffix_sum = [0] * length
        for i, val in reversed(list(enumerate(energy))):
            suffix_sum[i] = val + (suffix_sum[i + k] if i + k < length else 0)
        # print(suffix_sum)
        return max(suffix_sum)


def main():
    energy = [-2, -3, -1]
    print(Solution().maximumEnergy(energy, 3))
# @lc code=end

if __name__ == "__main__":
    main()
