from datasets import load_dataset
from hashing import hash_func
from recordinality import recordinality


def main():
    datasets = [
        "dracula", "crusoe", "iliad",
        "mare-balena", "midsummer-nights-dream",
        "quijote", "valley-fear", "war-peace"
    ]

    k = 64  # sample size for Recordinality

    for name in datasets:
        Z, true_n = load_dataset(name)

        est = recordinality(iter(Z), k=k, hash_func=hash_func)
        rel_err = abs(est - true_n) / true_n if true_n > 0 else 0.0

        print(f"Dataset: {name}")
        print(f"  True n       = {true_n}")
        print(f"  REC (k={k})  = {est:.2f}")
        print(f"  rel. error   = {rel_err:.4f}")
        print()


if __name__ == "__main__":
    main()
