class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
            return []

        small = 1
        big = len(arr)
        n = len(arr)
        ans = list()
        for j in range(len(arr)):
            for i in range(n):
                if arr[i] == big:
                    k = i+1
                    temp = arr[0:k]
                    arr[0:k] = temp[::-1]
                    ans.append(k)
                    print(k)
                    print(arr)
                    if arr[0] == big:
                        k = n
                        temp = arr[0:k]
                        arr[0:k] = temp[::-1]
                        ans.append(k)
                        print(k)
                        print(arr)
                    print(big)
                    big -= 1
                    n -= 1
            if big == small:
                break
        return ans

                
        