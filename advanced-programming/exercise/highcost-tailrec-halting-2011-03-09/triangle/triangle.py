def maxpath(tree):
    def inner(curr, rest, i):
        if rest == []:
            return [[curr]]
        ncurr, *nrest = rest
        return [[curr] + left for left in inner(ncurr[i], nrest, i)] + [[curr] + right for right in inner(ncurr[i+1], nrest, i+1)]

    paths = inner(tree[0][0], tree[1:], 0)
    return max([sum(path) for path in paths])
