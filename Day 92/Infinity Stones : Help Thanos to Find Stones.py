https://my.newtonschool.co/playground/code/rxx0037q8hjt


from collections import deque
import sys

INF = float('inf')

def is_safe(x, y, n, maze):
    return 0 <= x < n and 0 <= y < n and maze[x][y] != -2

def bfs(n, c, maze):
    dirs = [(0,1), (0,-1), (-1,0), (1,0)]
    dist = [[[INF]*n for _ in range(n)] for _ in range(1<<c)]
    
    q = deque()
    q.append((0, 0, 0))  # x, y, collected_bits
    dist[0][0][0] = 0
    ans = INF

    while q:
        x, y, cval = q.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not is_safe(nx, ny, n, maze):
                continue

            ncval = cval
            if maze[nx][ny] >= 0:
                ncval |= (1 << maze[nx][ny])

            if dist[ncval][nx][ny] > dist[cval][x][y] + 1:
                dist[ncval][nx][ny] = dist[cval][x][y] + 1
                if nx == n - 1 and ny == n - 1 and ncval == (1 << c) - 1:
                    ans = min(ans, dist[ncval][nx][ny])
                q.append((nx, ny, ncval))

    return -1 if ans == INF else ans

def main():
    n = int(sys.stdin.readline())
    maze = [[0]*n for _ in range(n)]
    c = 0

    for i in range(n):
        s = sys.stdin.readline().strip()
        for j in range(n):
            if s[j] == '.':
                maze[i][j] = -1
            elif s[j] == '#':
                maze[i][j] = -2
            elif s[j] == '*':
                maze[i][j] = c
                c += 1

    print(bfs(n, c, maze))

if __name__ == "__main__":
    main()
