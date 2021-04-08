class Solution:
    def halvesAreAlike(self, s):
        str_len = len(s)
        half = str_len // 2
        frst_half = self.check_Vow(s[:half])
        secnd_half = self.check_Vow(s[half:])

        return frst_half == secnd_half
    
    def check_Vow(self, string):
        vowels = "AaEeIiOoUu"
        final = [each for each in string if each in vowels]
        return len(final)


a = Solution()
print(a.halvesAreAlike("textbook"))