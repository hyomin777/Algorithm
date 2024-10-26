class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        start = 0
        length = 0
        
        for end in range(len(s)):
            if s[end] in hash_map:
                start = max(start, hash_map[s[end]] + 1)
            
            hash_map[s[end]] = end
            length = max(length, end - start + 1)
        
        return length
            
        