/* 
Title: Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
*/

namespace Palindrome;

class Palindromic
{
    public string LongestPalindrome(string s) {
        if (string.IsNullOrEmpty(s) || s.Length < 2){
            return s;
        }
        int maxlen = 0;
        int start = 0;

        for (int i = 0; i < s.Length; i++){
            int oddlen = ExpandAroundCenter(s, i, i);
            int evenlen = ExpandAroundCenter(s, i, i + 1);
            int len = Math.Max(oddlen, evenlen);

            if (len > maxlen){
                start = i - (len - 1) / 2;
                maxlen = len;
            }
        }
        return s.Substring(start, maxlen);
    }
    public int ExpandAroundCenter(string s, int left, int right){
        while(left >= 0 && right < s.Length && s[left] == s[right]){
            left--;
            right++;
        }
        return right - left - 1;
    }    
}