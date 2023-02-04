
import sys
from collections import deque
"""
from collections import deque

# encode state as a single big number
def encode(n1, n2, l2, pw):
    return n1 * pw[l2] + l2

def score(player1, player2):
    if len(player2) == 0:
        winner = list(player1)
    else:
        winner = list(player2)
    ans = 0
    for i in range(len(winner)):
        ans += winner[i] * (len(winner) - i)

    return ans

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
    return score(p1,p2)

def key(l1, p1, p2):
    res = 0
    for a in p2:
        res *= MX
        res += a
    for a in p1:
        res *= MX
        res += a
    a *= MX
    a += l1
    return a

def solve2(player1,player2):
    global MX
    MX = max(max(player1), max(player1)) + 1
    N = len(player1) + len(player2) + 1
    pw = [1] * (N+1)
    for i in range(1, N+1):
        pw[i] = pw[i-1] * MX
    print(pw)

    global_seen = set()
    dp = {}
    def rec(state_num):
        l2 = state_num % MX
        state_num //= MX
        n2 = state_num % pw[l2]
        state_num //= pw[l1]
        n1 = state_num
        l1 = 0
        while(pw[l1] >= n1):
            l1 += 1


        nonlocal global_seen, dp
        # print("new game", len(global_seen), len(dp))
        k = n2 * pow[l1] +
        if k in dp:
            return dp[k]
        seen = set()
        while len(p1) > 0 and len(p2) > 0:
            k = key(p1, p2)
            if k in seen or k in global_seen:
                global_seen |= seen
                dp[k] = p1 + p2, []
                return dp[k]

            seen.add(k)
            c1, c2 = p1.popleft(), p2.popleft()
            # print(c1, len(p1), c2, len(p2))
            if c1 <= len(p1) and c2 <= len(p2):
                round_win1 = len(rec(p1.copy(), p2.copy())[0]) > 0
            else:
                round_win1 = c1 > c2
            if round_win1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
            k = key(p1,p2)
        dp[k] = p1,p2
        return dp[k]
    return score(*rec(deque(player1), deque(player2)))

if __name__ == "__main__":
    inp = [l.rstrip() for l in sys.stdin]
    inp.append('')
    player1, player2 = [], []
    at = 1
    while len(inp[at]) > 0:
        player1.append(int(inp[at]))
        at += 1
    at += 2
    while len(inp[at]) > 0:
        player2.append(int(inp[at]))
        at += 1

    print(solve1(player1, player2))
    # print(solve2(player1, player2))

"""

def combat(cards1, cards2, recursive):
    combat_states = set()
    while len(cards1) and len(cards2):
        if recursive:
            combat_state = (tuple(cards1), -1, tuple(cards2))
            if combat_state in combat_states:
                return (cards1, 1)
            combat_states.add(combat_state)
        card1 = cards1.popleft()
        card2 = cards2.popleft()
        # recursive combat
        if recursive and len(cards1) >= card1 and len(cards2) >= card2:
            _, winner_num = combat(cards1[:card1], cards2[:card2], recursive)
            winner = cards1 if winner_num == 1 else cards2
        # normal combat
        else:
            winner = cards1 if card1 > card2 else cards2

        if winner == cards1:
            cards1.extend([card1, card2])
        else:
            cards2.extend([card2, card1])
    return (cards2, 2) if len(cards2) else (cards1, 1)


def get_deck_value(deck):
    return sum(c * (i + 1) for i, c in enumerate(reversed(deck)))


def main():
    inp = [l.rstrip() for l in sys.stdin]
    inp.append('')
    player1, player2 = [], []
    at = 1
    while len(inp[at]) > 0:
        player1.append(int(inp[at]))
        at += 1
    at += 2
    while len(inp[at]) > 0:
        player2.append(int(inp[at]))
        at += 1

    # part1
    winning_deck, _ = combat(deque(player1), deque(player2), recursive=False)
    print(get_deck_value(winning_deck))

    # part2
    winning_deck, _ = combat(deque(player1), deque(player2), recursive=True)
    print(get_deck_value(winning_deck))


if __name__ == "__main__":
    main()