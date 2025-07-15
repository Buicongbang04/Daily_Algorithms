def isValid(word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False

        if not all(c.isalnum() for c in word):
            return False

        vowels = set('aeiouAEIOU')
        has_vowel = any(c in vowels for c in word if c.isalpha())
        has_consonant = any(c.isalpha() and c not in vowels for c in word)

        return has_vowel and has_consonant