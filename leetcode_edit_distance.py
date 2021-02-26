class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # initializing DP matrix with some default value.
        dp_matrix = []
        for i in range(n+1):
            tmp = []
            for j in range(m+1):
                tmp.append(0)
            dp_matrix.append(tmp)

        dp_matrix[0][0] = 0

        # filling values that are known
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j != 0:
                    dp_matrix[i][j] = j
                elif j == 0 and i != 0:
                    dp_matrix[i][j] = i

        # word1 = horse, n = 5
        # word2 = ros, m = 3

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp_matrix[i][j] = dp_matrix[i-1][j-1]
                else:
                    dp_matrix[i][j] = min(dp_matrix[i-1][j-1] + 1, dp_matrix[i][j-1] + 1, dp_matrix[i-1][j] + 1)

        return dp_matrix[n][m]
