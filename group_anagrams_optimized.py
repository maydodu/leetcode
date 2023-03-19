class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = {}  # key: tuple, value: list

        for string in strs:
            # create a list of 26 zeros, each index represents a letter in the alphabet
            chars = [0] * 26
            
            # increment the index of the letter in the string
            for char in string:
                chars[ord(char) - ord('a')] += 1

            # add the string to the list of strings that have the same letter count
            result[tuple(chars)] = result.get(tuple(chars), [])
            result[tuple(chars)].append(string)

        return result.values()