from typing import List
import collections


class MySolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index2string = collections.defaultdict(list)
        index2counter = {}
        for idx, s in enumerate(strs):
            counter = collections.Counter(s)
            key_check = [k for k, v in index2counter.items() if v == counter]
            if key_check:
                key = key_check[0]
                index2string[key].append(s)
            else:
                index2counter[idx] = counter
                index2string[idx].append(s)
        return index2string.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())