from collections import deque


def isdelim(x):
    print(f"delim is {x}")
    if x[0] == -1 and x[1] == -1:
        return True
    return False


def isvalid(i, j, n, m):
    if (i>=0 and i<m) and (j>=0 and j<n):
        return True
    return False


def rottenFinder(grid):
    q = deque()
    m = len(grid)
    n = len(grid[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append([i, j])
    q.append([-1, -1])
    print(q)
    while len(q)!=0:
        flag = False
        while not isdelim(q[0]):
            i,j=q[0]
            # right
            if isvalid(i, j + 1, n, m) and grid[i][j + 1] == 1:
                print('right')
                print(i,j)
                if not flag:
                    ans, flag = ans + 1, True
                grid[i][j + 1] = 2
                q.append([i, j + 1])
            # left
            if isvalid(i, j - 1, n, m) and grid[i][j - 1] == 1:
                print('left')
                print(i, j)
                if not flag:
                    ans, flag = ans + 1, True
                grid[i][j - 1] = 2
                q.append([i, j - 1])
            # up
            if isvalid(i + 1, j, n, m) and grid[i + 1][j] == 1:
                print('up')
                print(i, j)
                if not flag:
                    ans, flag = ans + 1, True
                grid[i + 1][j] = 2
                q.append([i + 1, j])
            # down
            if isvalid(i - 1, j, n, m) and grid[i - 1][j] == 1:
                print('down')
                print(i, j)
                if not flag:
                    ans, flag = ans + 1, True
                grid[i - 1][j] = 2
                q.append([i - 1, j])
            print("here")
            print(q)
            q.popleft()
        q.popleft()
        if len(q) != 0:
            print('adding again')
            q.append([-1, -1])
        print(ans)
    return ans


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    grid1 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    grid3 = [[0, 2]]
    grid4 = [[1], [2]]
    grid5 = [[2, 0, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    print(rottenFinder(grid5))
