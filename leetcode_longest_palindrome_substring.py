class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # initializing DP matrix
        dp_matrix = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(False)
            dp_matrix.append(tmp)

        # filling values that are known
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp_matrix[i][j] = True
                elif j < n and i < n and j == i + 1 and s[i] == s[j]:
                    dp_matrix[i][j] = True

        for i in range(n-1, -1, -1):
            for j in range(n):
                if i+1<n and j-1>=0 and dp_matrix[i + 1][j - 1] and s[i] == s[j]:
                    dp_matrix[i][j] = True

        max_length_subarray = ''
        max_length = float('-inf')

        for i in range(n):
            for j in range(n):
                k = j - i
                if dp_matrix[i][j] and k>=max_length:
                    max_length_subarray = s[i:j+1]
                    max_length = j-i+1
        return max_length_subarray
