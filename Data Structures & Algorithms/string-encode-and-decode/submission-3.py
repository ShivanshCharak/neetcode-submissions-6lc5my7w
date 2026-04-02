class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res+=str(len(string)) + '#' + string
        return res
        
    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i < len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=s[i:j]
            print(length,i)
            i=j+1
            j=i+int(length)
            res.append(s[i:j])
            i=j
        return res