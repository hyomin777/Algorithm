class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        idx = 0
        length = 0
        
        for i in range(len(s)):
            if s[i] in hash_map:
                idx = max(idx, hash_map[s[i]] + 1)
            
            hash_map[s[i]] = i
            length = max(length, i - idx + 1)
        
        return length
            
        