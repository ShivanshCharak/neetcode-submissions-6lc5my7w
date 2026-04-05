class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for i in s:
            a[i]=a.get(i,0)+1
        for j in t:
            b[j]=b.get(j,0)+1
        return a == b
        