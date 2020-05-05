"""Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2."""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for char in range(len(s)):
            if s.count(s[char])==1:
                return char
        return -1
