class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {} #s : [s, anagram]

        if len(strs) == 1:
            return [[strs[0]]]

        for i, s in enumerate(strs):
            if i == 0:
                anagramMap[''.join(sorted(s))] = [s]
                continue
            else:
                if ''.join(sorted(s)) in anagramMap:
                    anagramMap[''.join(sorted(s))].append(s)
                else:
                    anagramMap[''.join(sorted(s))] = [s]
        return list(anagramMap.values())
