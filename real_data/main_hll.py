from datasets import load_dataset
from hyperloglog import hll_create, hll_add, hll_count


def main():
    datasets = [
        "dracula", "crusoe", "iliad",
        "mare-balena", "midsummer-nights-dream",
        "quijote", "valley-fear", "war-peace"
    ]

    b = 10  # m = 2^b registers

    for name in datasets:
        M, m = hll_create(b)

        Z, true_n = load_dataset(name)

        for z in Z:
            hll_add(M, m, z, b)

        est = hll_count(M, m)
        rel_err = abs(est - true_n) / true_n if true_n > 0 else 0.0

        print(f"Dataset: {name}")
        print(f"  True n      = {true_n}")
        print(f"  HLL (m={m}) = {est:.2f}")
        print(f"  rel. error  = {rel_err:.4f}")
        print()


if __name__ == "__main__":
    main()
