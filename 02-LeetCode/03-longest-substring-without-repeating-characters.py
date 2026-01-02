from typing import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = Counter()
        ans = l = 0
        for r, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[l]] -= 1
                l += 1
                print(l)
            ans = max(ans, r - l + 1)
        return ans


solution = Solution()
solution.lengthOfLongestSubstring("pwwkew")
