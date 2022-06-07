from typing import List
import collections
import re


class MySolution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub(r"[!?',;.]", ' ', paragraph)
        paragraph = paragraph.split()
        counter = collections.Counter(paragraph)
        for item in counter.most_common():
            if item[0] in banned:
                continue
            else:
                return item[0]


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]