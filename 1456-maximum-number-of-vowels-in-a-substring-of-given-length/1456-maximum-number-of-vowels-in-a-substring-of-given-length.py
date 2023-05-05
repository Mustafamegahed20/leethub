class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s=list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        max_vowel_count = 0
        vowel_count = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1

        max_vowel_count = vowel_count

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                vowel_count -= 1
            if s[i] in vowels:
                vowel_count += 1
            max_vowel_count = max(max_vowel_count, vowel_count)
        
        return max_vowel_count