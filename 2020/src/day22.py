import sys
from collections import deque

def solve1(player1,player2):
    p1 = deque(player1)
    p2 = deque(player2)
    while len(p1) > 0 and len(p2) > 0:
        c1,c2 = p1.popleft(), p2.popleft()
        if (c1 > c2):
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    if len(p2) == 0:
        winner = list(p1)
    else:
        winner = list(p2)

    ans = 0
    for i in range(len(winner)):
        ans += winner[i] * (len(winner) - i)

    return ans

if __name__ == "__main__":
    inp = [l.rstrip() for l in sys.stdin]
    inp.append('')
    player1 = []
    player2 = []
    at = 1
    while len(inp[at]) > 0:
        player1.append(int(inp[at]))
        at += 1
    at += 2
    while len(inp[at]) > 0:
        player2.append(int(inp[at]))
        at += 1

    print(solve1(player1,player2))
