#
# @lc app=leetcode id=1592 lang=python3
#
# [1592] Rearrange Spaces Between Words
#


# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        total = text.count(" ")
        words = text.split()
        if len(words) == 1:
            return words[0] + " " * total
        space_len = total // (len(words) - 1)
        append = " " * (total % (len(words) - 1))
        return (" " * space_len).join(words) + append


# @lc code=end
