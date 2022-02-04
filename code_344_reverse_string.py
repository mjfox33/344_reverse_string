class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n == 1:
            return
        
        for i in range(n//2):
            temp = s[n-1-i]
            s[n-1-i] = s[i]
            s[i] = temp