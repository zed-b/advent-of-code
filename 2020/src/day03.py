import sys

def solvePath(lines, y, x):
    at = 0
    res = 0
    cy = 1
    for l in lines:
        cy += 1
        if (cy % y) == 0:
            res += l[at] == "#"
            at = (at + x) % len(l)
    return res

def solve1(lines):
    return solvePath(lines, 1, 3)

def solve2(lines):
    ans = 1
    dy = [1,1,1,1,2]
    dx = [1,3,5,7,1]
    for i in range(len(dy)):
        ans *= solvePath(lines, dy[i], dx[i])
    return ans

if __name__ == "__main__":
    lines = [line.rstrip() for line in sys.stdin]
    print(solve1(lines))
    print(solve2(lines))