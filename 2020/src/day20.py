import sys, re

def top(grid):
    return "".join(grid[0])

def bottom(grid):
    return "".join(grid[-1])

def left(grid):
    return "".join(grid[i][0] for i in range(len(grid)))

def right(grid):
    return "".join(grid[i][-1] for i in range(len(grid)))

def canonical(row):
    return min(row, row[::-1])

def all_canonical(g):
    return map(canonical, (top(g), bottom(g), left(g), right(g)))

def solve1(tiles, edge_freq, edge_to_tiles):
    ans = 1
    for id, g in tiles.items():
        num_unique = sum(edge_freq[c] == 1 for c in all_canonical(g))
        if num_unique == 2:
            ans *= id
    return ans

def all_variations(grid):
    transposed = False
    while(True):
        yield grid
        grid = grid[::-1]
        yield grid
        for r in range(len(grid)):
            grid[r] = grid[r][::-1]
        yield grid
        grid = grid[::-1]
        yield grid
        if transposed:
            return
        transposed = True
        for r in range(1,len(grid)):
            for c in range(r):
                grid[r][c], grid[c][r] = grid[c][r], grid[r][c]

def grid_print(g):
    for r in g:
        print(r)

def solve2(tiles, edge_freq, edge_to_tiles):
    first = next(iter(tiles.values()))
    SIDE, SIDE2 = len(first), len(first[0])
    assert(SIDE == SIDE2) # else transposing is trickier
    r,c,n = 0,0,0
    tilemap = []
    tilemap_ids = []
    used = set()
    for i in range(len(tiles)):
        if c == 0:
            tilemap.append([])
            tilemap_ids.append([])
        id = None
        tile = None
        if r == 0:
            if c == 0:
                id = next(i for i in tiles.keys() if sum(edge_freq[c] == 1 for c in all_canonical(tiles[i])) == 2)
                tile = next(v for v in all_variations(tiles[id]) if edge_freq[canonical(top(v))] == 1 and edge_freq[canonical(left(v))] == 1)
            else:
                cand = edge_to_tiles[canonical(right(tilemap[r][c-1]))]
                id = next(i for i in cand if i not in used)
                tile = next(v for v in all_variations(tiles[id]) if left(v) == right(tilemap[r][c-1]) and edge_freq[canonical(top(v))] == 1)
        else:
            if c == 0:
                cand = edge_to_tiles[canonical(bottom(tilemap[r-1][c]))]
                id = next(i for i in cand if i not in used)
                tile = next(v for v in all_variations(tiles[id]) if edge_freq[canonical(left(v))] == 1 and bottom(tilemap[r-1][c]) == top(v))
            else:
                cand = edge_to_tiles[canonical(bottom(tilemap[r-1][c]))]
                id = next(i for i in cand if i not in used)
                tile = next(v for v in all_variations(tiles[id]) if right(tilemap[r][c-1]) == left(v) and bottom(tilemap[r-1][c]) == top(v))

        tilemap[-1].append(tile)
        tilemap_ids[-1].append(id)
        used.add(id)

        edge = canonical(right(tile))
        if (edge_freq[edge] == 1):
            c = 0
            r += 1
        else:
            c += 1

    S2 = SIDE - 2
    R,C = len(tilemap) * S2, len(tilemap[0]) * S2

    grid = [['.' for c in range(C)] for r in range(R)]
    for r in range(len(tilemap)):
        for c in range(len(tilemap[0])):
            for y in range(S2):
                for x in range(S2):
                    if tilemap[r][c][y+1][x+1] == '#':
                        grid[r * S2 + y][c * S2 + x] = '#'

    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   " ]

    MR = len(monster)
    MC = len(monster[0])

    for v in all_variations(grid):
        for r in range(len(v)-MR+1):
            for c in range(len(v[0])-MC+1):
                ok = True
                for mr in range(MR):
                    for mc in range(MC):
                        if monster[mr][mc] == '#' and v[r+mr][c+mc] == '.':
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    for mr in range(MR):
                        for mc in range(MC):
                            if monster[mr][mc] == '#':
                                v[r + mr][c + mc] = 'Z'

    return sum(v[r][c] == '#' for r in range(R) for c in range(C))

if __name__ == "__main__":
    inp = [l.rstrip() for l in sys.stdin]
    N = len(inp[1])
    at = 0
    tiles = {}
    while at < len(inp):
        id = int(re.search(r"Tile (\d+):", inp[at]).group(1))
        at += 1
        grid = []
        for i in range(0, N):
            grid.append(list(inp[at+i]))
        at += N+1
        tiles[id] = grid

    edge_freq = {}
    edge_to_tiles = {}

    for id,g in tiles.items():
        edges = list(map(canonical, (top(g), bottom(g), left(g), right(g))))
        for c in edges:
            edge_freq[c] = edge_freq.setdefault(c, 0) + 1
            if c not in edge_to_tiles:
                edge_to_tiles[c] = [id]
            else:
                edge_to_tiles[c].append(id)

    print(solve1(tiles, edge_freq, edge_to_tiles))
    print(solve2(tiles, edge_freq, edge_to_tiles))