class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        createMap = defaultdict(list)
        for n in strs:
            sortedS = ''.join(sorted(n))
            createMap[sortedS].append(n)
        return list(createMap.values())

        