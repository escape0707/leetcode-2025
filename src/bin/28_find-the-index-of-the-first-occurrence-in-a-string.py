#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
def calc_lps(s: str) -> list[int]:
    N = len(s)
    lps = [0] * N
    length = 0
    for i in range(1, N):
        while length > 0 and s[length] != s[i]:
            length = lps[length - 1]
        if s[length] == s[i]:
            length += 1
        lps[i] = length
    # print(lps)
    return lps


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N = len(needle)
        lps = calc_lps(needle)
        j = 0
        for i, c in enumerate(haystack):
            while j > 0 and needle[j] != c:
                j = lps[j - 1]
            if needle[j] == c:
                j += 1
                if j == N:
                    return i - j + 1
                    # print(i - j + 1)
                    # j = lps[-1]
        return -1


def main():
    print(Solution().strStr("sadbutsad", "sad"))


# @lc code=end

if __name__ == '__main__':
    main()
