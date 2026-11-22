"""DataLoaders: batches, shuffling, and looping over a Dataset."""

import torch
from torch.utils.data import DataLoader, TensorDataset

# A DataLoader wraps a Dataset and hands you BATCHES of samples.
# Why batches? Data is too big to process at once, and a batch gives a good
# enough gradient estimate while keeping memory small and the GPU busy.

features = torch.arange(10, dtype=torch.float32).reshape(10, 1)  # 10 samples
labels = torch.arange(10) % 2  # 0, 1, 0, 1, ...
dataset = TensorDataset(features, labels)

# --- basic loop --------------------------------------------------------------
loader = DataLoader(dataset, batch_size=4)
for batch_number, (x, y) in enumerate(loader):
    print(f"batch {batch_number}: x shape={tuple(x.shape)} y shape={tuple(y.shape)}")
# 10 samples with batch_size=4 -> batches of 4, 4, and 2 (the last one is smaller).
# The batch dimension is ALWAYS the first axis: (batch, ...features).

print("number of batches:", len(loader))  # 3

# --- shuffle: a different order every epoch ----------------------------------
# Shuffle training data so the model doesn't learn the order; keep validation unshuffled.
torch.manual_seed(0)
shuffled = DataLoader(dataset, batch_size=5, shuffle=True)
for epoch in range(2):
    order = [int(v) for x, _ in shuffled for v in x.flatten()]
    print(f"epoch {epoch} order:", order)

# --- drop_last: skip the final incomplete batch ------------------------------
print(len(DataLoader(dataset, batch_size=4, drop_last=True)))  # 2

# --- one batch by hand -------------------------------------------------------
x, y = next(iter(DataLoader(dataset, batch_size=3)))
print(x.shape, y.shape)  # torch.Size([3, 1]) torch.Size([3])

# --- typical training loop skeleton (the real thing is in autograd.py) -------
train_loader = DataLoader(dataset, batch_size=4, shuffle=True)
for epoch in range(2):  # one epoch = one full pass over the data
    for x, y in train_loader:  # one step per batch
        pass  # forward pass, loss, backward pass, optimizer step go here
# Vocabulary: sample (one item) -> batch (a group) -> epoch (all data once).
# 1000 samples, batch_size 100 -> 10 steps per epoch.

# Other useful options:
#   num_workers=2   load data in parallel background processes
#   pin_memory=True faster CPU -> GPU copying
#   (on Windows, num_workers > 0 needs the code under  if __name__ == "__main__":)
