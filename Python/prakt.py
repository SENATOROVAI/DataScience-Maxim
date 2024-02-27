class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        b = list(filter(lambda x: x.isupper(), list(pattern)))
        for i in queries:
            for j in b:
                if i.index(j) >= b.index(j) and 
            
                