class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # idea:
        #   givin arr
        # edge cases:
        #   -- same char in the same string ex: ['uun']  
        # approch:
        # loop over arr to exclude duplicate chars in the same string(edge case)
        # make every combination and check for duplicates and drop them
        # Filter out strings with duplicate characters
        arr = [s for s in arr if len(set(s)) == len(s)]
        
        # Initialize the maximum length
        max_len = 0
        
        # Backtracking function
        def backtrack(index, current_string):
            nonlocal max_len
            # Update the maximum length if the current string is valid
            if len(current_string) == len(set(current_string)):
                max_len = max(max_len, len(current_string))
            else:
                # If the current string has duplicates, stop further exploration
                return
            
            # Explore all possible subsequences
            for i in range(index, len(arr)):
                backtrack(i + 1, current_string + arr[i])
        
        # Start backtracking
        backtrack(0, "")
        return max_len
        