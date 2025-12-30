def recordinality(stream, k, hash_func):
    S = []          # list of (element, hash_value)
    S_elems = set() # to test membership in O(1)
    R = 0

    #Fill S with first k distinct elements
    for z in stream:
        if z in S_elems:
            continue
        h = hash_func(z)
        S.append((z, h))
        S_elems.add(z)
        if len(S) == k:
            R = k  # once S is full for the first time
            break

    # If we never reached k, then the cardinality is exactly len(S)
    if len(S) < k:
        return float(len(S))

    #Process the rest of the stream
    for z in stream:
        if z in S_elems:
            continue

        h = hash_func(z)

        # Find element with minimum hash in S
        min_z, min_h = S[0]
        for (x, hx) in S[1:]:
            if hx < min_h:
                min_z, min_h = x, hx

        # If the new hash is larger, it becomes a new k-record
        if h > min_h:
            # Remove old element from S and S_elems
            S_elems.remove(min_z)
            new_S = []
            for (x, hx) in S:
                if x != min_z or hx != min_h:
                    new_S.append((x, hx))
            S = new_S

            # Insert new element
            S.append((z, h))
            S_elems.add(z)

            # Increase k-record counter
            R += 1

    #Estimator:
    base = 1.0 + 1.0 / k
    Z_est = k * (base ** (R - k + 1) - 1.0)
    return Z_est
