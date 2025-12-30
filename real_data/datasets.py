def load_dataset(name):
    txt_path = name + ".txt"
    dat_path = name + ".dat"

    #Read .txt as stream of tokens
    Z = []
    with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
            words = line.split()
            Z.extend(words)

    #True cardinality = number of lines in .dat
    true_n = 0
    with open(dat_path, "r", encoding="utf-8") as f:
        for _ in f:
            true_n += 1

    return Z, true_n
