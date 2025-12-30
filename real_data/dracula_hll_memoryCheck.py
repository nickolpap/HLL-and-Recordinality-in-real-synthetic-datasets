from datasets import load_dataset
from hyperloglog import hll_create, hll_add, hll_count
import math


def main():
    Z, true_n = load_dataset("dracula")

    # Different m = 2^b
    b_values = [6, 7, 8, 9, 10]  # m = 64, 128, 256, 512, 1024
    R = 30  # number of runs per m

    print("Dataset: dracula")
    print(f"True n: {true_n}")
    print()

    for b in b_values:
        m = 1 << b

        ests = []

        for _ in range(R):
            # New sketch on each run (same hash function)
            M, m = hll_create(b)

            for z in Z:
                hll_add(M, m, z, b)

            est = hll_count(M, m)
            ests.append(est)

        # Empirical mean and standard error SE = sqrt(Var[ȷn]) / E[ȷn]
        mean_est = sum(ests) / R
        var_est = sum((e - mean_est) ** 2 for e in ests) / R
        std_est = math.sqrt(var_est)
        SE = std_est / mean_est if mean_est != 0 else 0.0

        # Mean relative error
        mean_rel = abs(mean_est - true_n) / true_n if true_n > 0 else 0.0

        print(
            f" b = {b:2d}, m = {m:4d} | "
            f"mean est = {mean_est:.2f} | SE = {SE:.4f} | "
            f"mean rel.err = {mean_rel:.4f}"
        )

    print()


if __name__ == "__main__":
    main()