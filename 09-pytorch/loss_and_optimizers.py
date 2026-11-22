"""Loss functions, optimizers, and a complete training loop.

This file ties together tensors, datasets, dataloaders, and autograd.
"""

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

# --- loss functions: ONE number saying how wrong the model is ----------------
predictions = torch.tensor([2.5, 0.0, 2.0])
targets = torch.tensor([3.0, -0.5, 2.0])

print(nn.MSELoss()(predictions, targets))  # mean squared error: for regression
print(nn.L1Loss()(predictions, targets))  # mean absolute error

# classification: CrossEntropyLoss takes raw scores (logits) and class numbers
logits = torch.tensor([[2.0, 0.5, 0.1], [0.1, 0.2, 3.0]])  # 2 samples, 3 classes
classes = torch.tensor([0, 2])  # the true class of each sample
print(nn.CrossEntropyLoss()(logits, classes))  # small: both predictions are right
print(nn.CrossEntropyLoss()(logits, torch.tensor([1, 0])))  # big: both are wrong
# Don't apply softmax yourself before CrossEntropyLoss; it does it internally.

# --- a model: layers with learnable weights ----------------------------------
model = nn.Linear(in_features=1, out_features=1)  # output = input * weight + bias
print(model.weight.shape, model.bias.shape)  # (1, 1) and (1,)
print(sum(p.numel() for p in model.parameters()), "parameters")

# --- optimizers: apply the gradient step for you -----------------------------
# SGD:  weight -= learning_rate * gradient          (simple)
# Adam: adapts the step size per weight             (a common default)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# --- the training loop -------------------------------------------------------
torch.manual_seed(0)
xs = torch.rand(200, 1) * 10  # hours studied
ys = 40 + 5 * xs + torch.randn(200, 1) * 3  # score = 40 + 5*hours + noise

# scale inputs: models train much better when numbers are small
xs_scaled = xs / 10

loader = DataLoader(TensorDataset(xs_scaled, ys), batch_size=32, shuffle=True)
model = nn.Linear(1, 1)
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.5)

for epoch in range(100):
    epoch_loss = 0.0
    for x_batch, y_batch in loader:
        predictions = model(x_batch)  # 1. forward pass
        loss = loss_function(predictions, y_batch)  # 2. how wrong?
        optimizer.zero_grad()  # 3. reset old gradients
        loss.backward()  # 4. compute new gradients
        optimizer.step()  # 5. update the weights
        epoch_loss += loss.item() * len(x_batch)
    if epoch % 20 == 0:
        print(f"epoch {epoch:3d} loss={epoch_loss / len(xs_scaled):.2f}")

weight = model.weight.item() / 10  # undo the scaling
print(f"learned: score = {model.bias.item():.1f} + {weight:.2f} * hours   (true: 40 + 5 * hours)")

# --- evaluate and predict ----------------------------------------------------
model.eval()  # switch to evaluation mode (matters for dropout / batch norm later)
with torch.no_grad():  # no gradients needed
    print("predicted score for 6 hours:", model(torch.tensor([[0.6]])).item())

# --- the 5 steps, memorize this pattern --------------------------------------
#   predictions = model(inputs)
#   loss = loss_function(predictions, targets)
#   optimizer.zero_grad()
#   loss.backward()
#   optimizer.step()
# Every neural network, from this line to a large language model, trains this way.
