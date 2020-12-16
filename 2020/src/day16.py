import sys, re, functools

def bipartite_match(N, adj):
    uvis = [False]*N
    vmatch = [-1]*N
    def dfs(u):
        if uvis[u]:
            return False
        uvis[u] = True
        for v in adj[u]:
            if vmatch[v] == -1 or dfs(vmatch[v]):
                vmatch[v] = u
                return True
        return False

    for i in range(N):
        uvis = [False]*N
        dfs(i)

    umatch = [-1]*N
    for i in range(N):
        umatch[vmatch[i]] = i
    return umatch

def solve1(tickets, all_diff):
    err_rate = 0
    for t in tickets:
        for n in t:
            if all_diff[n] == 0:
                err_rate += n
    return err_rate

def solve2(tickets, my_ticket, all_diff, diffs, need_sum_of):

    valid_tickets = []

    for t in tickets:
        valid = True
        for n in t:
            if all_diff[n] == 0:
                valid = False
                break
        if valid:
            valid_tickets.append(t)

    N = len(diffs)
    adj = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            valid = True
            for t in valid_tickets:
                if diffs[i][t[j]] == 0:
                    valid = False
                    break
            if valid:
                adj[i].append(j)

    assignment = bipartite_match(N, adj)
    return functools.reduce(lambda x,y: x*y,[my_ticket[assignment[i]] for i in need_sum_of],1)

if __name__ == "__main__":
    inp = [l.rstrip() for l in sys.stdin]
    MX = 1010
    all_diff = [0]*MX
    diffs = []
    at = 0
    need_sum_of = []
    while True:
        if inp[at].find(':') < 0:
            break
        name, ranges = inp[at].split(':')
        res = re.findall(r"(\d+)\-(\d+)", ranges)
        cur_diff = [0]*MX
        for r in res:
            all_diff[int(r[0])] += 1
            all_diff[int(r[1])+1] -= 1
            cur_diff[int(r[0])] += 1
            cur_diff[int(r[1])+1] -= 1

        if (name.startswith('departure')):
            need_sum_of.append(len(diffs))

        for i in range(1, len(cur_diff)):
            cur_diff[i] += cur_diff[i-1]

        diffs.append(cur_diff)
        at += 1

    for i in range(1, len(all_diff)):
        all_diff[i] += all_diff[i-1]

    while not inp[at].startswith("your ticket:"):
        at += 1

    at += 1
    my_ticket = list(map(int,inp[at].split(',')))

    while not inp[at].startswith("nearby tickets:"):
        at += 1

    tickets = []
    err_rate = 0
    for l in inp[at+1:]:
        vals = list(map(int,l.split(',')))
        tickets.append(vals)

    print(solve1(tickets, all_diff))
    print(solve2(tickets, my_ticket, all_diff, diffs, need_sum_of))