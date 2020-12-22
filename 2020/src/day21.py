import sys

def bipartite_match(adj, M):
    N = len(adj)
    uvis = [False]*N
    vmatch = [-1]*M
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
    for i in range(M):
        umatch[vmatch[i]] = i
    return umatch

def solve(recipes):
    possible = {}
    all_ing = set()
    all_al = set()
    for ing,al in recipes:
        for a in al:
            all_al.add(a)
            if a not in possible:
                possible[a] = set(ing)
            else:
                possible[a] &= set(ing)
        all_ing |= set(ing)

    all_ing = list(all_ing)
    all_al = list(all_al)

    adj = [[] for _ in range(len(all_ing))]

    for i,al in enumerate(all_al):
        for j,ing in enumerate(all_ing):
            if ing in possible[al]:
                adj[j].append(i)

    umatch = bipartite_match(adj, len(all_al))

    matches = {}
    for u,v in enumerate(umatch):
        if v != -1:
            matches[all_ing[u]] = all_al[v]

    return matches

def solve1(recipes):
    matches = solve(recipes)
    ans = 0
    for ing, al in recipes:
        for i in ing:
            ans += i not in matches
    return ans

def solve2(recipes):
    matches = solve(recipes)
    ing = list(matches.keys())
    return ",".join(sorted(ing,key=lambda x : matches[x]))

if __name__ == "__main__":
    inp = [l.rstrip() for l in sys.stdin]
    recipes = []
    for l in inp:
        ing,al = l[:-1].split(' (contains ')
        ing = ing.split(' ')
        al = al.split(', ')
        recipes.append((ing,al))
    print(solve1(recipes))
    print(solve2(recipes))