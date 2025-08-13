class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = (''.join(char for char in s if char.isalnum())).lower()
        return palindrome[::1] == palindrome[::-1]