from datasets import load_dataset
from hashing import hash_func
from recordinality import recordinality
import math


def main():
    Z, true_n = load_dataset("dracula")

    # Different sample sizes k
    k_values = [64, 128, 256, 512, 1024]
    R = 30  # number of runs per k

    print("Dataset: dracula")
    print(f"True n: {true_n}")
    print()

    for k in k_values:
        ests = []

        for _ in range(R):
            # Recordinality with the same hash function on each run
            est = recordinality(iter(Z), k=k, hash_func=hash_func)
            ests.append(est)

        # Empirical mean and standard error SE = sqrt(Var[ȷn]) / E[ȷn]
        mean_est = sum(ests) / R
        var_est = sum((e - mean_est) ** 2 for e in ests) / R
        std_est = math.sqrt(var_est)
        SE = std_est / mean_est if mean_est != 0 else 0.0

        # Mean relative error
        mean_rel = abs(mean_est - true_n) / true_n if true_n > 0 else 0.0

        print(
            f" k = {k:4d} | "
            f"mean est = {mean_est:.2f} | SE = {SE:.4f} | "
            f"mean rel.err = {mean_rel:.4f}"
        )

    print()


if __name__ == "__main__":
    main()