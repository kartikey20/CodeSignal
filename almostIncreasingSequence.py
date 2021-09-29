def almostIncreasingSequence(sequence):
    removed, max, previousMax,  = 0, 0, 0
    for s in sequence:
        if not max or s > max:
            previousMax, max = max, s
        elif not previousMax or s > previousMax:
            if removed:
                return False
            removed, max = 1, s
        else:
            if removed:
                return False
            removed = 1
    return True
