from zipf_stream import generate_zipf_stream
from hyperloglog import hll_create, hll_add, hll_count


def main():
    N = 100_000
    n = 10_000
    alpha_values = [0.0, 1.0, 2.0]

    b_values = [6, 7, 8, 9, 10]

    for alpha in alpha_values:
        print(f"Zipf stream (HLL): N={N}, n={n}, alpha={alpha}")
        # One stream per alpha
        Z = generate_zipf_stream(N=N, n=n, alpha=alpha, seed=0)
        true_n = len(set(Z))

        for b in b_values:
            m = 1 << b
            M, m = hll_create(b)

            for z in Z:
                hll_add(M, m, str(z), b)

            est = hll_count(M, m)
            rel_err = abs(est - true_n) / true_n if true_n > 0 else 0.0

            print(
                f" b = {b:2d}, m = {m:4d} | "
                f"est = {est:.2f} | rel.err = {rel_err:.4f}"
            )

        print()


if __name__ == "__main__":
    main()
