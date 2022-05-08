import re


class MySolution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-z0-9]", "", s)

        for i in range(len(s)):
            if s[i] != s[-i-1]:
                return False
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


if __name__ == "__main__":
    print(MySolution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))