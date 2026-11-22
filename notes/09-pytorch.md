# 09. PyTorch

Install inside your venv (CPU version): `python -m pip install torch --index-url https://download.pytorch.org/whl/cpu`.
For a GPU build, pick the command at https://pytorch.org/get-started/locally/. Then `import torch`.

## What exactly is a tensor?
- A tensor is a container of numbers arranged along zero or more axes, where every number has the same type.
- Number of axes: 0 = scalar, 1 = vector, 2 = matrix, 3 or more = higher tensors (a stack of tables, a batch of images).
- It is the NumPy array you already know, plus two superpowers:
  1. it can live on a **GPU**, so many numbers are processed in parallel;
  2. it can **remember how it was computed**, so PyTorch can find gradients automatically.
- The shape gives it meaning: `(32, 3, 224, 224)` = 32 images, 3 color channels, 224 high, 224 wide.
- Test yourself: can you explain, without notes, why a batch of 32 grayscale 28x28 images has shape `(32, 1, 28, 28)` and a table of 100 rows by 5 features has shape `(100, 5)`?

## Tensors and shapes
- Create: `torch.tensor([...])`, `zeros`, `ones`, `arange`, `linspace`, `eye`, `rand` (uniform), `randn` (normal), `zeros_like`.
- Attributes: `.shape`, `.ndim`, `.numel()`, `.dtype`, `.device`.
- Default decimal type is `float32` (networks use it: precise enough, fast, half the memory of float64); whole numbers are `int64`.
- Convert: `.float()`, `.long()`, `.to(dtype)`.
- Shape tools: `reshape(3, 4)` (`-1` = work it out), `.T`, `squeeze()`, `unsqueeze(dim)`.
- Indexing and slicing are the same as NumPy; `.item()` turns a one-number tensor into a Python number.
- `torch.from_numpy(a)` and `t.numpy()` share memory with NumPy (CPU only).
- Most PyTorch errors are shape mismatches: print `.shape` often.

## Tensor operations
- Element-wise: `+ - * / **`, `torch.sqrt`, `torch.exp`, `torch.log`.
- Matrix multiply: `a @ b`; `(m, n) @ (n, p) -> (m, p)`.
- Broadcasting works as in NumPy; `inputs @ weights + bias` is one neural-network layer.
- Reductions use `dim` (NumPy's `axis`): `sum`, `mean`, `max`, `argmax`; that dimension disappears.
- Join: `torch.cat` (existing dimension) vs `torch.stack` (new dimension).
- Activations: `relu` (negatives to 0), `sigmoid` (squashes to 0-1), `softmax` (scores to probabilities that sum to 1).
- Operations ending in `_` change the tensor in place; avoid them on tensors that track gradients.

## CPU vs GPU
- CPU: a few powerful cores. GPU: thousands of simple cores, ideal for the parallel math in neural networks.
- Pick a device: `cuda` (NVIDIA), `mps` (Apple), else `cpu`; the same script then runs anywhere.
- `tensor = tensor.to(device)` returns a new tensor; assign it. Create directly with `device=device` to avoid copying.
- Model, inputs, and targets must all be on the same device, or you get a `RuntimeError`.
- Use `.cpu().numpy()` before handing a GPU tensor to NumPy or matplotlib.
- Small jobs can be faster on CPU because copying data to the GPU costs time.

## Datasets
- A `Dataset` answers `len(dataset)` and `dataset[i]` (usually `(input, label)`).
- `TensorDataset(features, labels)` wraps tensors you already have.
- Custom: subclass `Dataset` and write `__len__` and `__getitem__`; load files lazily so the data never needs to fit in memory.
- Split with `random_split(dataset, [0.8, 0.2])`: train on one part, validate on another, test on a third; never judge a model on data it trained on.

## DataLoaders
- A `DataLoader` serves batches from a Dataset: `DataLoader(dataset, batch_size=32, shuffle=True)`.
- The batch is always the first dimension: `(batch, ...features)`; the last batch may be smaller (`drop_last=True` skips it).
- Shuffle training data; do not shuffle validation data.
- Sample -> batch -> epoch (one full pass over the data); 1000 samples at batch size 100 = 10 steps per epoch.

## Automatic differentiation (autograd)
- A **gradient** says how much, and in which direction, the result changes if you nudge a number. Learning = nudging weights to make the loss smaller.
- `requires_grad=True` makes PyTorch track a tensor; `loss.backward()` fills each tracked tensor's `.grad`.
- Update opposite to the gradient: `w -= learning_rate * w.grad` (inside `torch.no_grad()`).
- Gradients **accumulate**: reset them every step (`.grad.zero_()` or `optimizer.zero_grad()`).
- `torch.no_grad()` turns tracking off for evaluation and prediction; `.detach()` cuts a tensor from the graph (needed before `.numpy()`).

## Loss functions and optimizers
- A loss is one number saying how wrong the model is. `MSELoss` for regression; `CrossEntropyLoss` for classification (give it raw scores and class numbers, no softmax first).
- A model such as `nn.Linear(in, out)` holds learnable `parameters()`.
- Optimizers apply the update: `SGD` (simple) and `Adam` (adapts the step per weight; a common default). The learning rate controls the step size.
- The five-step training loop, used by every neural network:
  1. `predictions = model(inputs)`
  2. `loss = loss_function(predictions, targets)`
  3. `optimizer.zero_grad()`
  4. `loss.backward()`
  5. `optimizer.step()`
- `model.eval()` plus `torch.no_grad()` for predicting.
- Scale inputs to small numbers; models train much better.

## Practice checklist
- [ ] explain what a tensor is in your own words
- [ ] create scalar, vector, matrix, and image-batch tensors and read their shapes
- [ ] change a tensor's dtype and reshape it
- [ ] multiply two matrices and check the output shape
- [ ] reduce a tensor along a dimension
- [ ] pick a device and move a tensor to it
- [ ] write a custom `Dataset`
- [ ] split a dataset and iterate it with a `DataLoader`
- [ ] compute a gradient with `backward()` and take one manual step
- [ ] fit `y = 2x + 1` with gradient descent by hand
- [ ] write the five-step training loop with `nn.Linear` and an optimizer
