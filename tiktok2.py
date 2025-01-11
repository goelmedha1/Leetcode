def maximizeCreatorSupport(impactValue):
    # Separate positives, zeros, and negatives
    positives = []
    negatives = []
    zeros_count = 0
    
    for v in impactValue:
        if v > 0:
            positives.append(v)
        elif v < 0:
            negatives.append(v)
        else:
            zeros_count += 1  # v == 0
    
    # 1) Sum all positives
    net_impact = sum(positives)
    count = len(positives)  # all positive items are included
    
    # 2) Add all zeros (they won't break positivity as long as net_impact > 0)
    if net_impact > 0:
        count += zeros_count  # each zero keeps net_impact unchanged
    
    # 3) Sort negatives by ascending absolute value, then try to include them greedily
    negatives.sort(key=lambda x: abs(x))
    
    for neg in negatives:
        if net_impact + neg > 0:  # still remains positive
            net_impact += neg
            count += 1
        else:
            # If this negative is too large (in absolute value),
            # none of the larger (more negative) ones will fit either
            # but let's continue just in case there's a less negative item (in a different scenario).
            # Actually, we've sorted ascending, so the next items will be worse.
            # We can break here for efficiency, but it won't affect correctness.
            break
    
    return count