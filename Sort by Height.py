def sortByHeight(a):
    def conditional_sort(ls, f):
        y = iter(sorted(w for w in ls if f(w)))
        return [w if not f(w) else next(y) for w in ls]
    return conditional_sort(a, lambda x: x != -1)
