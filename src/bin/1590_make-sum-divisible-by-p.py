#
# @lc app=leetcode id=1590 lang=python3
#
# [1590] Make Sum Divisible by P
#

# @lc code=start
import itertools


class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        N = len(nums)
        prefix_sum_remainder = list(
            itertools.islice(
                itertools.accumulate(nums, lambda a, b: (a + b) % p, initial=0), 1, None
            )
        )
        if prefix_sum_remainder[-1] == 0:
            return 0

        postfix_sum_remainder = list(
            itertools.islice(
                itertools.accumulate(
                    reversed(nums), lambda a, b: (a + b) % p, initial=0
                ),
                1,
                None,
            )
        )
        postfix_sum_remainder.reverse()

        answer = N
        # Take care of the corner case where we might remove a prefix array from nums
        optimal_remove_left_bound_by_remainder = {0: 0}
        for i in range(N):
            # Find better remove possiblity where i is the right bound
            remove_right_bound = i
            complement_remainder = (p - postfix_sum_remainder[remove_right_bound]) % p
            if (
                optimal_remove_left_bound := optimal_remove_left_bound_by_remainder.get(
                    complement_remainder
                )
            ) is not None:
                answer = min(answer, remove_right_bound - optimal_remove_left_bound)
            # Maintain the hash table for further queries where i + 1 could be the left bound
            optimal_remove_left_bound_by_remainder[prefix_sum_remainder[i]] = i + 1
        # Take care of the corner case where we might remove a postfix array from nums
        if optimal_remove_left_bound_by_remainder[0] != 0:
            answer = min(answer, N - optimal_remove_left_bound_by_remainder[0])

        if answer == N:
            answer = -1
        return answer


def main():
    print(Solution().minSubarray([3, 1, 4, 2], 6))


# @lc code=end

if __name__ == "__main__":
    main()
