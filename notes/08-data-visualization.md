# 08. Data Visualization

Install inside your venv: `python -m pip install matplotlib`, then `import matplotlib.pyplot as plt`.
Goal: understand how AI/ML experiments are visualized, not become a charting specialist.

## Matplotlib basics
- **Figure** = the whole canvas; **Axes** = one chart on it. `fig, ax = plt.subplots()` gives both.
- Draw with `ax.plot(...)`, `ax.bar(...)`, `ax.scatter(...)`, `ax.hist(...)`, then `plt.show()`.
- Label every chart: `ax.set_title(...)`, `ax.set_xlabel(...)`, `ax.set_ylabel(...)`, `ax.legend()` (needs `label=` on each line).
- Several charts: `fig, axes = plt.subplots(1, 2, figsize=(10, 4))`, then `fig.tight_layout()`.
- Save with `fig.savefig("name.png", dpi=150, bbox_inches="tight")`; `plt.close(fig)` frees memory.
- Prefer the `ax.*` (object) style over `plt.*` shortcuts; it scales to subplots.
- `plt.show()` blocks until you close the window.

## Which chart for what
| Chart | Use it to see | AI/ML example |
|---|---|---|
| line | change over time or steps | training loss per epoch |
| bar | compare categories | accuracy per model |
| histogram | distribution of one number | prediction scores, feature values |
| box plot | median, spread, outliers | latency per model |
| scatter | relationship between two numbers | actual vs predicted, two features |
| heatmap (`imshow`) | a matrix as colors | confusion matrix |

## Distributions
- A distribution shows how often each value appears.
- `ax.hist(data, bins=30)`: too few bins hides detail, too many shows noise.
- Normal (bell curve) data has mean about equal to the median; skewed data has its mean pulled toward the long tail.
- Box plot: box = middle 50%, line = median, whiskers = typical range, dots = outliers.
- Check feature distributions before training: outliers, skew, and class balance.

## Scatter plots
- Each dot is one row; `ax.scatter(x, y, alpha=0.7)`.
- Trend line: `np.polyfit(x, y, 1)`; correlation: `np.corrcoef(x, y)` (-1 to 1; correlation is not causation).
- Colored by group, a scatter shows classes in feature space; if a line can separate them, a simple model works.
- Actual vs predicted: dots on the diagonal = perfect predictions.

## Training curves
- Plot loss (and accuracy) per epoch for training **and** validation data.
- Loss falling = learning. Flat from the start = learning rate too small or a bug. Zig-zagging = learning rate too large.
- **Overfitting:** training loss keeps falling while validation loss rises; the gap is the warning. Fixes: more data, regularization, smaller model, early stopping.
- **Underfitting:** both losses high and flat.
- One line per experiment (for example one per learning rate) compares runs.

## Honest charts
- Label axes and units; a truncated y-axis (`set_ylim`) exaggerates differences, so say so.
- Use the same scale when comparing charts side by side (`sharey=True`).
- Pandas plots with matplotlib: `df["col"].plot.hist()`, `df.plot.bar()`.

## Chapter experiments (in `08-data-visualization/experiments/`)
- `training_curves.py` - healthy run, overfitting, loss and accuracy together, learning-rate comparison (fake data until phase 09).
- `model_comparison.py` - average accuracy bars, grouped bars, accuracy vs latency, confusion matrix.

## Practice checklist
- [ ] draw a labeled line chart with a legend
- [ ] draw a bar chart comparing categories
- [ ] put two charts in one figure with subplots
- [ ] save a figure to a PNG
- [ ] plot a histogram and change the number of bins
- [ ] draw a scatter plot with a trend line
- [ ] color a scatter plot by class
- [ ] plot train and validation loss and identify overfitting
- [ ] draw a confusion matrix and compute accuracy from it
