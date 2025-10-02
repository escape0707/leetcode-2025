/*
 * @lc app=leetcode id=77 lang=rust
 *
 * [77] Combinations
 */

// @lc code=start
impl Solution {
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        let mut answer = vec![];
        let mut combination: Vec<i32> = (1..=k).collect();
        loop {
            answer.push(combination.clone());
            let Some((pivot_index, _)) = combination
                .iter()
                .enumerate()
                .rev()
                .find(|&(i, &elem)| elem != n - k + i as i32 + 1)
            else {
                break;
            };
            combination[pivot_index] += 1;
            for j in pivot_index + 1..k as usize {
                combination[j] = combination[j - 1] + 1;
            }
        }
        answer
    }
}

fn _main() {
    let n = 4;
    let k = 2;
    println!("{:?}", Solution::combine(n, k))
}

// @lc code=end

struct Solution;

fn main() {
    _main()
}
