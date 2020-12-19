import sys, functools

def calc_rule_lengths(dict_rules, at):
    vis = set()
    def calc(at):
        if type(at) == str:
            return set([len(at)])
        if at in vis:
            return set([-1])
        vis.add(at)
        res = set()
        for id_list in dict_rules[at][0]:
            ans = set()
            for id in id_list:
                ans2 = calc(id)
                if -1 in ans2:
                    res = set([-1])
                if not len(ans):
                    ans = ans2
                else:
                    ans3 = set()
                    for a in ans:
                        for b in ans2:
                            ans3.add(a + b)
                    ans = ans3
            if -1 in res:
                break
            res |= ans
        dict_rules[at][1].update(res)
        vis.remove(at)
        return res
    calc(at)

def solve(word, rules, start):

    @functools.lru_cache()
    def matches(word, rule_id):
        if type(rule_id) == str:
            return word == rule_id
        # optionally end check if lenght is impossible for rule
        if -1 not in rules[rule_id][1] and len(word) not in rules[rule_id][1]:
            return False
        rule = rules[rule_id][0]
        if type(rule) == list:
            for id_list in rule:
                if len(id_list) == 3:
                    for i in range(1, len(word)-1):
                        for j in range(i+1, len(word)):
                            if matches(word[:i], id_list[0]) and matches(word[i:j], id_list[1]) and matches(word[j:], id_list[2]):
                                return True
                elif len(id_list) == 2:
                    for i in range(1, len(word)):
                        if matches(word[:i], id_list[0]) and matches(word[i:], id_list[1]):
                            return True
                elif matches(word, id_list[0]):
                    return True
        else:
            return rule == word

        return False

    return matches(word, 0)

def solve1(words, rules):
    calc_rule_lengths(rules, 0)
    return sum((solve(w, rules, 0) for w in words))

def solve2(words, rules):
    rules[8] = ([[42],[42,8]], set())
    rules[11] = ([[42,31],[42,11,31]], set())
    calc_rule_lengths(rules, 0)
    return sum((solve(w, rules, 0) for w in words))

if __name__ == "__main__":
    inp = [l.rstrip() for l in sys.stdin]
    at = 0
    dict_rules = {}
    while len(inp[at]):
        l = inp[at]
        id_rules = l.split(': ')
        id = int(id_rules[0])
        rules = id_rules[1].split(' | ')
        rule = []
        for r in rules:
            parsed = []
            for x in r.split(' '):
                if x[0] == '"':
                    parsed.append(x[1:-1])
                else:
                    parsed.append(int(x))
            rule.append(parsed)
        dict_rules[id] = (rule, set())
        at += 1
    words = inp[at+1:]

    print(solve1(words, dict_rules))
    print(solve2(words, dict_rules))

