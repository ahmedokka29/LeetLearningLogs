class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        prefix_sum = [0] * len(words)
        vowels = {"a", "e", "i", "o", "u"}
        s = 0
        for i, q in enumerate(words):
            if q[0] in vowels and q[-1] in vowels:
                s += 1
            prefix_sum[i] = s

        print(prefix_sum)
        for i in range(len(queries)):
            if queries[i][0] == 0:
                ans[i] = prefix_sum[queries[i][1]]
            else:
                ans[i] = prefix_sum[queries[i][1]] - prefix_sum[queries[i][0] - 1]

        return ans

        # Brute Force - Time Limit Exceeded
        # ans = [0] * len(queries)
        # for q in queries:
        #     single_q = 0
        #     filtered = words[q[0]:q[1]+1]
        #     for i in filtered:
        #         if i.startswith(vowels) and i.endswith(vowels):
        #             single_q += 1
        #     ans.append(single_q)
        # return ans
