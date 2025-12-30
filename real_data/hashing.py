import randomhash

_rfh = randomhash.RandomHashFamily(count=1)


def hash_func(x: str) -> int:
    # randomhash returns 32-bit integers; we mask into 64 bits if needed
    h32 = _rfh.hash(x)
    return h32 & ((1 << 64) - 1)
