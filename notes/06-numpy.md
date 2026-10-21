# 06. NumPy

Install inside your venv: `python -m pip install numpy`, then `import numpy as np`.

## Key vocabulary
| Term | Meaning | Example | `shape` |
|---|---|---|---|
| scalar | a single number | `5` | `()` |
| vector | a list of numbers | `[1, 2, 3]` | `(3,)` |
| matrix | a table of numbers | 2 rows, 3 columns | `(2, 3)` |
| tensor | an array with 3 or more dimensions | batch of images | `(32, 28, 28)` |
| dimension (`ndim`) | how many axes an array has | matrix -> 2 | |
| shape | length of each axis, as a tuple | `(2, 3)` | |
| axis | one direction of the array: 0 = down rows, 1 = across columns | | |

- A "3-number vector" has shape `(3,)` and `ndim` 1. Don't confuse its size with its dimension.
- Deep learning is mostly arrays (tensors) flowing through operations; knowing the shape at every step is the main skill.

## Arrays
- `np.array([...])`, `np.zeros(shape)`, `np.ones(shape)`, `np.arange(start, stop, step)`, `np.linspace(a, b, n)`, `np.eye(n)`.
- All elements share one `dtype` (`int64`, `float64`; `float32` is common in deep learning).
- `.shape`, `.ndim`, `.size`, `.dtype` describe an array.
- `.reshape(rows, cols)` changes shape without changing data; `-1` means "work it out"; `.flatten()` makes it 1-D.
- Arrays are fast and do math on whole arrays; lists can't.

## Indexing and slicing
- `a[i]`, `a[i, j]`, negatives count from the end.
- Slices are `start:stop:step`; `matrix[rows, cols]` such as `matrix[:, 0]` (first column), `matrix[0:2, 1:3]`.
- Boolean masks filter: `scores[scores > 0.4]`.
- Slices are **views**, not copies: changing one changes the original. Use `.copy()`.

## Vector operations
- `+ - * / **` work element by element; no loops needed.
- Functions: `np.sqrt`, `np.exp`, `np.log`, `np.where(condition, a, b)`.
- Dot product: `a @ b` (multiply matching elements, then add).
- `np.linalg.norm(a)` is the length of a vector; cosine similarity `(a @ b) / (norm(a) * norm(b))` compares embeddings.

## Matrix operations
- `A * B` is element-wise; `A @ B` is matrix multiplication.
- Rule: `(m, n) @ (n, p) -> (m, p)`; the inner sizes must match.
- `A.T` transposes; `np.linalg.inv`, `np.linalg.det`, `np.linalg.solve`.
- A neural-network layer is `output = inputs @ weights + bias`.

## Broadcasting
- NumPy stretches smaller arrays so different shapes can combine.
- Compare shapes from the right; sizes must be equal or one of them must be 1.
- `(2, 3) + (3,)` works; `(2, 3) + (2, 1)` works; `(2, 3) + (2,)` is an error.
- `np.newaxis` or `.reshape` adds an axis to control the direction.

## Aggregation
- `sum`, `mean`, `min`, `max`, `std`, `median`, `argmax`.
- `axis` names the axis that **disappears**: for shape `(2, 3)`, `axis=0` gives shape `(3,)` and `axis=1` gives shape `(2,)`.
- `keepdims=True` keeps the axis so the result still broadcasts.

## Random numbers
- Use `rng = np.random.default_rng(seed=42)` for reproducible results.
- `rng.random(shape)`, `rng.integers(low, high, size)`, `rng.normal(mean, std, size)`, `rng.choice(...)`, `rng.permutation(n)`.
- Random weights and shuffled datasets are everyday ML tasks.

## Practice checklist
- [ ] create a scalar, vector, matrix, and tensor and print their shapes
- [ ] reshape a 1-D array into a matrix
- [ ] slice a row, a column, and a sub-block of a matrix
- [ ] filter an array with a boolean mask
- [ ] compute a dot product and a vector length
- [ ] multiply two matrices and check the output shape
- [ ] add a vector to a matrix using broadcasting
- [ ] compute column and row averages with `axis`
- [ ] generate seeded random data
- [ ] write one dense layer: `inputs @ weights + bias`
