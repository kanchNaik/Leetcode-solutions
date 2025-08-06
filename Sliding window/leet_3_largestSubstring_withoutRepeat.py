class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        maxlen = 0
        l = 0  # Left pointer of the window

        for r, char in enumerate(s):
            if char in char_index and char_index[char] >= l:
                # Move left pointer past the last occurrence
                l = char_index[char] + 1

            char_index[char] = r  # Update last seen index of char
            maxlen = max(maxlen, r - l + 1)

        return maxlen
