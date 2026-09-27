class Solution:
    def isPalindrome(self, s: str) -> bool:
        #return true if string is palindrome
        # string is palindrome if it is the same reverse and backwards.
        newStr = ""

        for i in s:
            if i.isalnum():
                newStr += i.lower()
        return newStr == newStr[::-1]