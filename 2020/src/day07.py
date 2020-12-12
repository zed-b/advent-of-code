import sys, re, functools

def solve1(adj, q):
    @functools.lru_cache()
    def dfs(b):
        ans = 1 if b == q else 0
        for _,e in adj[b]:
            ans |= dfs(e)
        return ans
    ans = 0
    for k in adj.keys():
        ans += dfs(k)
    return ans - 1

def solve2(adj, q):
    @functools.lru_cache()
    def dfs(b):
        ans = 1
        for n,e in adj[b]:
            ans += n * dfs(e)
        return ans
    return dfs(q)-1

if __name__ == "__main__":
    q = 'shiny gold'
    adj = {}
    for l in sys.stdin:
        m = re.search(r"(.+) bags contain", l)
        v = m[1]
        m = re.findall(r"(\d+) ([^.,]+) bag(s?)[.,]", l)
        adj[v] = []
        for r in m:
            adj[v].append((int(r[0]),r[1]))
    print(solve1(adj, q))
    print(solve2(adj, q))