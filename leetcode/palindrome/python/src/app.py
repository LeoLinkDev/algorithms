class Palindrome:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ''' Automatically a palindrome:
            - Single char or empty string (n < 2)
            - String equals it's reversed copy s == s[::-1]
        '''
        if n < 2 or s == s[::-1]:
            return s

        start, maxlen = 0, 1
        i = 0
        while i < n:
            if n - i <= maxlen // 2: # n - i = what's left is impossible to beat maxlen (shortcut :)
                break
            l = r = i
            while r + 1 < n and s[r + 1] == s[i]:
                r += 1
            i = r + 1
            while l > 0 and r + 1 < n and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            if r - l + 1 > maxlen:
                maxlen = r - l + 1
                start = l
        return s[start:start + maxlen]