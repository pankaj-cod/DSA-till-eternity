class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        matrx = [[0]*n for _ in range(m)]
        i,j = 0,0
        while j<n:
            matrx[i][j]="."
            j+=1
        j-=1
        while i<m:
            matrx[i][j]='.'
            i+=1
        i,j = 0,0
        for i in range(m):
            for j in range(n):
                if matrx[i][j]==0:
                    matrx[i][j]="#"
        fin = []
        for mat in matrx:
            ans = ''
            ans = ''.join(mat)
            fin.append(ans)
        return fin
            

        