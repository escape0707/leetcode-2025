#
# @lc app=leetcode id=2872 lang=python3
#
# [2872] Maximum Number of K-Divisible Components
#

# @lc code=start

from typing import NamedTuple


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: list[list[int]], values: list[int], k: int
    ) -> int:
        class Result(NamedTuple):
            components: int
            total: int

        def sum_conquer(root: int, parent: int) -> Result:
            components = 0
            total = values[root]
            for child in adjacency_list[root]:
                if child == parent:
                    continue
                child_components, child_total = sum_conquer(child, root)
                components += child_components
                total += child_total
            if total % k == 0:
                components += 1
            return Result(components, total)

        adjacency_list: list[list[int]] = [[] for _ in range(n)]
        for edge in edges:
            a, b = edge[0], edge[1]
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        return sum_conquer(0, 0).components

# @lc code=end
