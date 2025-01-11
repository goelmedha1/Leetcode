def getSpikeSpread(x: int) -> int:
    """
    Computes the spikeSpread for a single activityIndex value x.
    spikeSpread is defined as the max gap between consecutive set bits (1s)
    in x's binary representation, counting the zeros strictly between them.
    If x has only one set bit, returns -1.
    """
    positions = []
    pos = 0
    
    # Collect positions of set bits from right to left
    while x > 0:
        if (x & 1) == 1:
            positions.append(pos)
        x >>= 1
        pos += 1
    
    # If only one set bit, spikeSpread = -1
    if len(positions) < 2:
        return -1
    
    # Otherwise compute max((p_{i+1} - p_i) - 1)
    max_gap = 0
    for i in range(len(positions) - 1):
        gap = (positions[i+1] - positions[i]) - 1
        if gap > max_gap:
            max_gap = gap
    
    return max_gap

def getTopKViralPosts(activityIndex, k):
    """
    Returns an array of the top k posts (activityIndex values),
    sorted by descending spikeSpread, then by descending activityIndex.
    """
    # 1) Build list of (value, spikeSpread)
    with_spread = []
    for val in activityIndex:
        spread = getSpikeSpread(val)
        with_spread.append((val, spread))
    
    # 2) Sort in descending order of spikeSpread, then activityIndex
    #    i.e. sort key = (-spread, -val)
    with_spread.sort(key=lambda x: (x[1], x[0]), reverse=True)
    
    # 3) Extract the first k activityIndex values
    top_k = [post[0] for post in with_spread[:k]]
    return top_k

# --------------- 
# Quick Demo:

# Example 1
arr1 = [11, 3, 4, 9, 7]
k1 = 3
print(getTopKViralPosts(arr1, k1))  
# Expected: [9, 11, 7]

# Example 2
arr2 = [10, 13, 5, 18]
k2 = 3
print(getTopKViralPosts(arr2, k2))
# Expected: [18, 13, 10]