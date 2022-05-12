from typing import List
import collections


class MySolution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ordered_log = []
        
        digdict = collections.defaultdict(list)
        letdict = collections.defaultdict(list)
        for log in logs:
            point = log.find(' ') + 1
            if log[point].isnumeric():
                digdict[log[point:]].append(log)
            else:
                letdict[log[point:]].append(log)
        
        for key in sorted(list(letdict.keys())):
            ordered_log.extend(sorted(letdict[key]))
        for key in digdict.keys():
            ordered_log.extend(sorted(digdict[key]))
            
        return ordered_log


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits