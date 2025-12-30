from zipf_stream import generate_zipf_stream
from hashing import hash_func
from recordinality import recordinality


def main():
    # Synthetic stream parameters
    N = 100_000   # stream length
    n = 10_000    # max possible distinct ids (1..n)
    alpha_values = [0.0, 1.0, 2.0]

    k_values = [64, 128, 256, 512, 1024]

    for alpha in alpha_values:
        print(f"Zipf stream (REC): N={N}, n={n}, alpha={alpha}")
        # Generate one stream per alpha
        Z = generate_zipf_stream(N=N, n=n, alpha=alpha, seed=0)
        true_n = len(set(Z))

        for k in k_values:
            est = recordinality(iter(map(str, Z)), k=k, hash_func=hash_func)
            rel_err = abs(est - true_n) / true_n if true_n > 0 else 0.0

            print(
                f" k = {k:4d} | "
                f"est = {est:.2f} | rel.err = {rel_err:.4f}"
            )

        print()


if __name__ == "__main__":
    main()
