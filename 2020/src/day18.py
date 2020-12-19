import sys

def solve(l, ops):
    i = 0
    num_stack = [[]]
    op_stack = [[]]
    def apply():
        nonlocal num_stack, op_stack
        arg2 = num_stack[-1].pop()
        arg1 = num_stack[-1].pop()
        op = op_stack[-1].pop()
        num_stack[-1].append(ops[op][1](arg1, arg2))

    while(True):
        if i >= len(l):
            while len(op_stack[-1]):
                apply()
            break
        c = l[i]
        if c in ops:
            while len(op_stack[-1]) and ops[op_stack[-1][-1]][0] <= ops[c][0]:
                apply()
            op_stack[-1].append(c)
        elif c == ' ':
            pass
        elif c == '(':
            num_stack.append([])
            op_stack.append([])
        elif c == ')':
            while len(op_stack[-1]):
                apply()
            num_stack[-2].append(num_stack[-1][0])
            num_stack.pop()
            op_stack.pop()
        else:
            num = 0
            while i < len(l) and '0' <= l[i] and l[i] <= '9':
                num *= 10
                num += int(c)
                i += 1
            num_stack[-1].append(num)
            continue

        i += 1
    return num_stack[-1][0]

def solve1(inp):
    ops = {'+': (1, lambda x,y: x + y), '*': (1, lambda x,y: x * y)}
    return sum((solve(l,ops) for l in inp))

def solve2(inp):
    ops = {'+': (1, lambda x,y: x + y), '*': (2, lambda x,y: x * y)}
    return sum((solve(l,ops) for l in inp))

if __name__ == "__main__":
    inp = [l.rstrip() for l in sys.stdin]
    print(solve1(inp))
    print(solve2(inp))