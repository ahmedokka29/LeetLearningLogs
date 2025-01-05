def encode_string(s):
    char_to_num = {}
    encoded = []
    current_num = 0

    for char in s:
        if char not in char_to_num:
            char_to_num[char] = current_num
            current_num += 1
        encoded.append(str(char_to_num[char]))

    return '-'.join(encoded)


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        encoded_strings = [encode_string(s) for s in words]
        for original, encoded in zip(words, encoded_strings):
            print(f"{original} → {encoded}")

        encoded_pattern = encode_string(pattern)
        print(f"{pattern} → {encoded_pattern}")

        ans = []
        for i,s in enumerate(encoded_strings):
            if s == encoded_pattern:
                ans.append(words[i])
        return ans
