class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1

        ans = 0
        odd_found = False
        for word, freq in count.items():
            if word[0] == word[1]:
                # For palindromic words like "aa", "bb", etc.
                ans += (freq // 2) * 4
                if freq % 2 == 1:
                    odd_found = True
            else:
                # For non-palindromic words like "ab", "ba", etc.
                reverse_word = word[::-1]
                if reverse_word in count:
                    pairs = min(freq, count[reverse_word])
                    ans += pairs * 4
                    count[reverse_word] = 0
                count[word] = 0
        if odd_found:
            ans += 2    
        return ans

print(Solution().longestPalindrome(["lc", "cl", "gg"]))
print(Solution().longestPalindrome(["ab","ty","yt","lc","cl","ab"]))
print(Solution().longestPalindrome(["cc","ll","xx"]))