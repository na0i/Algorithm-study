class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = {}

        for idx in range(len(strs)):

            temp = ''
            for s in sorted(strs[idx]):
                temp += s

            new_strs[idx] = temp

        new_strs = sorted(new_strs.items(), key=lambda x: x[1])

        result = [[strs[new_strs[0][0]]]]

        for idx in range(1, len(new_strs)):
            if new_strs[idx][1] == new_strs[idx - 1][1]:
                result[-1].append(strs[new_strs[idx][0]])
            else:
                result.append([strs[new_strs[idx][0]]])

        return result