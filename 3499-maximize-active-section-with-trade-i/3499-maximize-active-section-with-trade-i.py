class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ones = 0
        pre = float("-inf")
        mx = 0

        i = 0

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            length = j - i

            if s[i] == '1':
                ones += length
            else:
                mx = max(mx, pre + length)
                pre = length

            i = j

        return ones + mx