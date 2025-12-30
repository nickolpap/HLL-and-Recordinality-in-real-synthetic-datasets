# HLL-and-Recordinality-in-real-synthetic-datasets

Project comparing **HyperLogLog** and **Recordinality** for distinct-count (cardinality) estimation on real text datasets and synthetic Zipf streams.

## Files

##Used in both real and syntetic data
- `hyperloglog.py` – HyperLogLog implementation.
- `recordinality.py` – Recordinality implementation.
- `hashing.py` – Hash functions.

##Used in real data
- `datasets.py` – Configuration of dataset.
- `main_hll.py` – Runs HLL with fixed `m = 1024` on all real datasets.
- `main_rec.py` – Runs Recordinality with fixed `k = 1024` on all real datasets.
- `dracula_hll_memoryCheck.py` – HLL on `dracula` for multiple `m`, reports mean estimate and mean relative error.
- `dracula_rec_memoryCheck.py` – Same as above for Recordinality and `k`.
  
##Used in synthtic data
- `zipf_stream.py` – Generator for synthetic Zipf streams.
- `synth_hll.py` – HLL on synthetic Zipf streams for several `m` and Zipf parameters `α`.
- `synth_rec.py` – Recordinality on synthetic Zipf streams for several `k` and `α`.

## Datasets
The real datasets are plain-text novels **not included** in this repository.
Download them from Project Gutenberg:
- Project Gutenberg Free eBooks: https://www.gutenberg.org/


