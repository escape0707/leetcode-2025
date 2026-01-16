#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start
import itertools

class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        N = len(boxes)
        boxes_int = tuple(map(int, boxes))
        prefix_sum = list(itertools.accumulate(boxes_int))
        postfix_sum = list(itertools.accumulate(reversed(boxes_int)))
        postfix_sum.reverse()
        move_left, move_right = [0] * N, [0] * N
        for i in range(1, N):
            move_left[i] = move_left[i - 1] + prefix_sum[i - 1]
        for i in reversed(range(N - 1)):
            move_right[i] = move_right[i + 1] + postfix_sum[i + 1]
        return [move_left[i] + move_right[i] for i in range(N)]

def main():
    print(Solution().minOperations("001011"))


# @lc code=end

if __name__ == '__main__':
    main()
