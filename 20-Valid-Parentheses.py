class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():  # If it's an opening bracket
                stack.append(char)
            elif char in bracket_map.keys():  # If it's a closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # If the character is not a bracket, return False (though the problem says s consists of brackets only)
                return False

        # If the stack is empty, all brackets are matched
        return not stack