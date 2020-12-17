import sys

def solve1(grid, cycles):
    pad = cycles + 3
    R,C  = len(grid) + pad * 2, len(grid[0]) + pad * 2
    H = pad * 2 + 1
    g = [[['.' for _ in range(H)] for _ in range(C)] for _ in range(R)]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            g[pad + r][pad + c][H//2 + 1] = grid[r][c]

    total = 0
    for _ in range(cycles):
        g2 = [[['.' for _ in range(H)] for _ in range(C)] for _ in range(R)]
        total = 0
        for r in range(R):
            for c in range(C):
                for h in range(H):
                    n_neighbours = 0
                    for z in [-1,0,1]:
                        if h + z < 0 or h + z >= H:
                            continue
                        for y in [-1,0,1]:
                            if y + r < 0 or y + r >= R:
                                continue
                            for x in [-1,0,1]:
                                if x + c < 0 or x + c >= C:
                                    continue
                                if x == 0 and y == 0 and z == 0:
                                    continue
                                n_neighbours += g[r+y][c+x][h+z] == '#'
                    if g[r][c][h] == '#' and n_neighbours != 2 and n_neighbours != 3:
                        g2[r][c][h] = '.'
                    elif g[r][c][h] == '.' and n_neighbours == 3:
                        g2[r][c][h] = '#'
                    else:
                        g2[r][c][h] = g[r][c][h]
                    total += g2[r][c][h] == '#'
        g = g2

    return total

def solve2(grid, cycles):
    pad = cycles + 3
    R,C  = len(grid) + pad * 2, len(grid[0]) + pad * 2
    H = pad * 2 + 1
    D = pad * 2 + 1
    g = [[[['.' for _ in range(D)] for _ in range(H)] for _ in range(C)] for _ in range(R)]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            g[pad + r][pad + c][H//2 + 1][D//2 + 1] = grid[r][c]

    total = 0
    for _ in range(cycles):
        g2 = [[[['.' for _ in range(D)] for _ in range(H)] for _ in range(C)] for _ in range(R)]
        total = 0
        for r in range(R):
            for c in range(C):
                for h in range(H):
                    for d in range(D):
                        n_neighbours = 0
                        for w in [-1,0,1]:
                            if w + d < 0 or w + d >= D:
                                continue
                            for z in [-1,0,1]:
                                if h + z < 0 or h + z >= H:
                                    continue
                                for y in [-1,0,1]:
                                    if y + r < 0 or y + r >= R:
                                        continue
                                    for x in [-1,0,1]:
                                        if x + c < 0 or x + c >= C:
                                            continue
                                        if x == 0 and y == 0 and z == 0 and w == 0:
                                            continue
                                        n_neighbours += g[r+y][c+x][h+z][d+w] == '#'
                        if g[r][c][h][d] == '#' and n_neighbours != 2 and n_neighbours != 3:
                            g2[r][c][h][d] = '.'
                        elif g[r][c][h][d] == '.' and n_neighbours == 3:
                            g2[r][c][h][d] = '#'
                        else:
                            g2[r][c][h][d] = g[r][c][h][d]
                        total += g2[r][c][h][d] == '#'
        g = g2

    return total



if __name__ == "__main__":
    grid = [l.rstrip() for l in sys.stdin]
    # faster testing locally
    cycles = 2 if len(grid) < 4 else 6
    print(solve1(grid, cycles))
    print(solve2(grid, cycles))