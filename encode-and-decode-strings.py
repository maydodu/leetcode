class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # to encode, add the length of the string to the front of the string
        result = ''
        for string in strs:
            result += str(len(string)) + '#' + string
        
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, string):
        result = []
        i = 0

        while(i < len(string)):
            j = i
            while(string[j] != '#'):
                j += 1
            length = int(string[i:j])
            result.append(string[j+1:j+1+length])
            i = j + 1 + length
            
        return result
        