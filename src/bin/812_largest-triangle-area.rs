/*
 * @lc app=leetcode id=812 lang=rust
 *
 * [812] Largest Triangle Area
 */

// @lc code=start

use itertools::Itertools;

type Point = Vec<i32>;

impl Solution {
    pub fn largest_triangle_area(points: Vec<Vec<i32>>) -> f64 {
        fn area(a: &Point, b: &Point, c: &Point) -> f64 {
            (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])).abs() as f64 / 2.
        }
        points
            .iter()
            .array_combinations()
            .map(|[a, b, c]| area(a, b, c))
            .fold(0., f64::max)
    }
}

fn _main() {
    let my_points = vec![vec![1, 0], vec![0, 0], vec![0, 1]];
    let result = Solution::largest_triangle_area(my_points);
    println!("Max area: {}", result);
}

// @lc code=end

struct Solution;

fn main() {
    _main()
}
