"""Datasets: a standard way to hand data (inputs and labels) to PyTorch."""

import torch
from torch.utils.data import Dataset, TensorDataset, random_split

# A Dataset answers two questions:
#   len(dataset)      -> how many samples are there?
#   dataset[index]    -> give me sample number `index` (usually (input, label))

# --- simplest: wrap tensors you already have ---------------------------------
features = torch.rand(100, 3)  # 100 samples, 3 features each
labels = torch.randint(0, 2, (100,))  # 100 labels: class 0 or 1

simple = TensorDataset(features, labels)
print(len(simple))  # 100
x, y = simple[0]
print(x.shape, y)  # torch.Size([3]) and a label

# --- custom Dataset: subclass and define __len__ and __getitem__ -------------
class HoursDataset(Dataset):
    """Predict an exam score from hours studied (a tiny regression problem)."""

    def __init__(self, n_samples=200, seed=0):
        generator = torch.Generator().manual_seed(seed)
        self.hours = torch.rand(n_samples, 1, generator=generator) * 10  # shape (n, 1)
        noise = torch.randn(n_samples, 1, generator=generator) * 3
        self.scores = 40 + 5 * self.hours + noise  # score rises with hours

    def __len__(self):
        return len(self.hours)

    def __getitem__(self, index):
        return self.hours[index], self.scores[index]  # one sample: (input, target)


dataset = HoursDataset()
print(len(dataset))
hours, score = dataset[0]
print(f"sample 0: hours={hours.item():.2f} score={score.item():.1f}")

# --- why a class? Data often must be loaded lazily ---------------------------
# For images or text, __getitem__ would open ONE file and convert it to a tensor
# when asked, so the whole dataset never has to sit in memory at once.
class TextLengthDataset(Dataset):
    """Labels short/long messages; text is turned into numbers on demand."""

    def __init__(self, texts):
        self.texts = texts

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        text = self.texts[index]
        features = torch.tensor([len(text), text.count(" ") + 1], dtype=torch.float32)
        label = torch.tensor(1 if len(text) > 20 else 0)
        return features, label


texts = TextLengthDataset(["hi", "a much longer message than the others", "ok thanks"])
print(texts[1])

# --- split into train / validation / test ------------------------------------
# Train on one part, check progress on a second, report final quality on a third.
# Never evaluate on data the model trained on: it would just memorize.
train_set, val_set = random_split(
    dataset, [0.8, 0.2], generator=torch.Generator().manual_seed(42)
)
print(len(train_set), len(val_set))  # 160 40

# Next: dataloaders.py turns a Dataset into batches for training.
