import random
import math


def generate_zipf_stream(N, n, alpha, seed=None):
    if seed is not None:
        random.seed(seed)

    # Compute normalization constant c_n
    if alpha == 0:
        # Uniform distribution over {1,...,n}
        probs = [1.0 / n] * n
    else:
        weights = [1.0 / (i ** alpha) for i in range(1, n + 1)]
        Z = sum(weights)
        probs = [w / Z for w in weights]

    cdf = []
    cum = 0.0
    for p in probs:
        cum += p
        cdf.append(cum)

    def sample_one():
        u = random.random()
        for i, c in enumerate(cdf):
            if u <= c:
                return i + 1
        return n

    stream = [sample_one() for _ in range(N)]
    return stream
