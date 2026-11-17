# 5. Longest Palindromic Substring

**Difficulty:** Medium  
**Pattern:** Expand Around Center (Two Pointers)  
**Link:** [LeetCode #5 - Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

---

## Intuition

A palindrome mirrors around its center. Instead of checking every substring from the outside in ($O(n^3)$), we iterate through the string, treat each index (or block of identical characters) as a potential center, and expand two pointers (`l` and `r`) outward while `s[l - 1] == s[r + 1]`.

### Key Optimizations
1. **Fast-Path Base Check (`n < 2 or s == s[::-1]`):** Returns immediately in C-level execution time if the string has 0–1 characters or is already a full palindrome.
2. **Duplicate Center Collapsing (`s[r + 1] == s[i]`):** Groups consecutive identical characters (e.g., `"aaaa"`) into a single center and advances `i = r + 1`. This handles both odd and even centers simultaneously and turns worst-case inputs like `"a" * 1000` into $O(n)$ time.
3. **Early Loop Termination (`n - i <= maxlen // 2`):** Because `n - i` represents the maximum possible radius remaining to the right of `i`, we break early once it becomes mathematically impossible to beat `maxlen`.
4. **Short-Circuit Bounds Checking:** Evaluating `l > 0 and r + 1 < n` before `s[l - 1] == s[r + 1]` prevents negative index wrap-around (`s[-1]`) and `IndexError` exceptions without extra helper function overhead.

---

## Complexity Analysis

* **Time Complexity:** $O(n^2)$ in the worst case (e.g., alternating characters with multiple partial palindromes), though pruning and center-collapsing make it approach $O(n)$ on most inputs (9 ms runtime, beating 99.89% of submissions).
* **Space Complexity:** $O(1)$ auxiliary space (excluding the $O(n)$ slice check `s[::-1]` and output string).

---

## Solution (Python 3)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ''' Automatically a palindrome:
            - Single char or empty string (n < 2)
            - String equals its reversed copy (s == s[::-1])
        '''
        if n < 2 or s == s[::-1]:
            return s

        start, maxlen = 0, 1
        i = 0
        while i < n:
            if n - i <= maxlen // 2:  # What's left cannot beat maxlen
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