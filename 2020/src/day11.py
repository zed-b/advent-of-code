import sys

def simulate(seats, adj, adj_tolerance):
    R,C = len(seats), len(seats[0])
    taken = [[False for c in range(C)] for r in range(R)]
    while True:
        change = False
        new_taken = [[taken[r][c] for c in range(C)] for r in range(R)]
        seated = 0
        for r in range(R):
            for c in range(C):
                if seats[r][c] != 'L':
                    continue
                adj_taken = 0
                for y,x in adj[r][c]:
                    adj_taken += taken[y][x]
                if adj_taken == 0 and not taken[r][c]:
                    new_taken[r][c] = True
                elif adj_taken >= adj_tolerance and taken[r][c]:
                    new_taken[r][c] = False
                change |= new_taken[r][c] != taken[r][c]
                seated += new_taken[r][c]
        if not change:
            return seated
        taken = new_taken

def solve1(seats):
    R,C = len(seats), len(seats[0])
    adj = [[[] for c in range(C)] for r in range(R)]
    for r in range(R):
        for c in range(C):
            for y in range(max(r - 1, 0), min(r + 2, R)):
                for x in range(max(c - 1, 0), min(c + 2, C)):
                    if y == r and x == c:
                        continue
                    if seats[r][c] == 'L':
                        adj[r][c].append((y,x))
    return simulate(seats, adj, 4)

def solve2(seats):
    R,C = len(seats), len(seats[0])
    adj = [[[] for c in range(C)] for r in range(R)]
    dy = [-1,-1,-1,0,0,1,1,1]
    dx = [-1,0,1,-1,1,-1,0,1]

    def ok(r, c):
        return 0 <= r and r < R and 0 <= c and c < C

    for r in range(R):
        for c in range(C):
            for i in range(len(dy)):
                y = r
                x = c
                while True:
                    y += dy[i]
                    x += dx[i]
                    if not ok(y,x):
                        break
                    if seats[y][x] == 'L':
                        adj[r][c].append((y,x))
                        break
    return simulate(seats, adj, 5)

if __name__ == "__main__":
    seats = [l.rstrip() for l in sys.stdin]
    print(solve1(seats))
    print(solve2(seats))