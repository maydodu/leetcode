class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count the number of each character in each string
        counts = {} # key: string, value: dict of char counts
        for string in strs: 
            counts[string] = {}
            for char in string:
                counts[string][char] = counts[string].get(char, 0) + 1
        
        # compare the counts of each string to each other
        result = []  # list of groups
        is_used = [False] * len(strs)  # list of booleans to keep track of which strings have been used
        for i in range(len(strs)):  
            if is_used[i] == True:  # if the string has already been used,
                continue            # skip it    
            group = [] 
            group.append(strs[i])  
            for j in range(i+1, len(strs)): # compare the string to all other strings
                if counts[strs[i]] == counts[strs[j]] and is_used[j] == False:
                    is_used[j] = True
                    group.append(strs[j])
            result.append(group)

        return result