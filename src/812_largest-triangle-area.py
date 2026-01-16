#
# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#

# @lc code=start
import itertools
from typing import TypeAlias

Point: TypeAlias = list[int]


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        def area(a: Point, b: Point, c: Point) -> float:
            return (
                abs(
                    (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
                )
                / 2
            )

        return max(itertools.starmap(area, itertools.combinations(points, 3)))


def main():
    points = [[1, 0], [0, 0], [0, 1]]
    print(Solution().largestTriangleArea(points))


# @lc code=end

if __name__ == "__main__":
    main()
