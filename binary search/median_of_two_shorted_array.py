# brute force
class Solution:
    def median(self, arr1, arr2):
        i = j = 0
        ans = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1

        ans += arr1[i:]
        ans += arr2[j:]
        n = len(ans)

        if n % 2 == 0:
            median = (ans[n // 2 - 1] + ans[n // 2]) / 2
        else:
            median = ans[n // 2]

        
        return median