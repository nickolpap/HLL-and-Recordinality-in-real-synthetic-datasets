from hashing import hash_func
import math

HASH_BITS = 32


def _alpha_m(m: int) -> float:
    if m == 16:
        return 0.673
    if m == 32:
        return 0.697
    if m == 64:
        return 0.709
    # m >= 128
    return 0.7213 / (1.0 + 1.079 / m)


def _rho(w: int, max_bits: int) -> int:
    if w == 0:
        return max_bits + 1
    # leading_zeros = max_bits - floor(log2(w)) = max_bits - bit_length
    return max_bits - w.bit_length() + 1


def hll_create(b: int):
    m = 1 << b
    M = [0] * m
    return M, m


def hll_add(M, m: int, x: str, b: int):
    h = hash_func(x)
    # Keep HASH_BITS bits to match the underlying hash output
    h &= (1 << HASH_BITS) - 1

    # j: index (first b bits of h)
    j = h >> (HASH_BITS - b)
    # w: remaining bits
    w = h & ((1 << (HASH_BITS - b)) - 1)

    rho_w = _rho(w, HASH_BITS - b)
    if rho_w > M[j]:
        M[j] = rho_w


def hll_count(M, m: int) -> float:
 
    alpha = _alpha_m(m)

    # Compute harmonic mean
    inv_sum = 0.0
    for v in M:
        inv_sum += 2.0 ** (-v)
    if inv_sum == 0.0:
        return 0.0

    inv_sum = 1.0 / inv_sum
    E = alpha * m * m * inv_sum
    return E