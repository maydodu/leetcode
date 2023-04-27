class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric characters
        alnum_str = ""
        # for every character in s, if it is alphanumeric, add it to alnum_str
        for char in s:
            if char.isalnum():
                alnum_str += char
        
        # convert alnum_str to lowercase
        alnum_str = alnum_str.lower()

        return alnum_str == alnum_str[::-1]