class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        # First Approach
        # brute Aprroach
        
        lst_s = list(s)
        
        for i in range(len(s)):
            # update the index according to the given indices
            
            lst_s[ indices[i] ] = s[i]
        
        return "".join(lst_s)
        
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)
        
        
        
            
            