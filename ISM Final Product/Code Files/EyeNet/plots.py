import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

with open(Path("data") / "results-5.txt") as file:
    results_5 = file.read().splitlines()
results_5 = np.ndarray.astype(np.sort(results_5), int)

with open(Path("data") / "results-10.txt") as file:
    results_10 = file.read().splitlines()
results_10 = np.ndarray.astype(np.sort(results_10), int)

with open(Path("data") / "results-15.txt") as file:
    results_15 = file.read().splitlines()
results_15 = np.ndarray.astype(np.sort(results_15), int)

with open(Path("data") / "results-20.txt") as file:
    results_20 = file.read().splitlines()
results_20 = np.ndarray.astype(np.sort(results_20), int)

with open(Path("data") / "results-25.txt") as file:
    results_25 = file.read().splitlines()
results_25 = np.ndarray.astype(np.sort(results_25), int)

with open(Path("data") / "results-30.txt") as file:
    results_30 = file.read().splitlines()
results_30 = np.ndarray.astype(np.sort(results_30), int)

with open(Path("data") / "results-35.txt") as file:
    results_35 = file.read().splitlines()
results_35 = np.ndarray.astype(np.sort(results_35), int)

plt.switch_backend("TkAgg")

plt.hist(results_5, bins=7, histtype="step", label="5 Iterations")
plt.hist(results_10, bins=8, histtype="step", label="10 Iterations")
plt.hist(results_15, bins=6, histtype="step", label="15 Iterations")
plt.hist(results_20, bins=7, histtype="step", label="20 Iterations")
plt.hist(results_25, bins=4, histtype="step", label="25 Iterations")
plt.hist(results_30, bins=7, histtype="step", label="30 Iterations")
plt.hist(results_35, bins=7, histtype="step", label="35 Iterations")
plt.axis([40, 95, 0, 5])
plt.xlabel("Classification Accuracy (%)")
plt.ylabel("Frequency")
plt.title("Impact of Training Iterations on Classification Accuracy")
plt.legend(loc="upper left")
plt.show()

means = np.array([results_5.mean(), results_10.mean(), results_15.mean(), results_20.mean(), results_25.mean(), results_30.mean(), results_35.mean()])
plt.plot([5, 10, 15, 20, 25, 30, 35], means)
plt.axis([5, 35, 0, 100])
plt.xlabel("Number of Training Iterations")
plt.ylabel("Mean Classification Accuracy (%)")
plt.title("Impact of Training Iterations on Mean Classification Accuracy")
plt.show()

with open(Path("data") / "results-50x50.txt") as file:
    results_50x50 = file.read().splitlines()
results_50x50 = np.ndarray.astype(np.sort(results_50x50), int)

with open(Path("data") / "results-60x60.txt") as file:
    results_60x60 = file.read().splitlines()
results_60x60 = np.ndarray.astype(np.sort(results_60x60), int)

with open(Path("data") / "results-70x70.txt") as file:
    results_70x70 = file.read().splitlines()
results_70x70 = np.ndarray.astype(np.sort(results_70x70), int)

with open(Path("data") / "results-80x80.txt") as file:
    results_80x80 = file.read().splitlines()
results_80x80 = np.ndarray.astype(np.sort(results_80x80), int)

with open(Path("data") / "results-90x90.txt") as file:
    results_90x90 = file.read().splitlines()
results_90x90 = np.ndarray.astype(np.sort(results_90x90), int)

plt.switch_backend("TkAgg")

plt.hist(results_50x50, bins=3, histtype="step", label="50x50")
plt.hist(results_60x60, bins=8, histtype="step", label="60x60")
plt.hist(results_70x70, bins=8, histtype="step", label="70x70")
plt.hist(results_80x80, bins=6, histtype="step", label="80x80")
plt.hist(results_90x90, bins=4, histtype="step", label="90x90")
plt.axis([40, 95, 0, 10])
plt.xlabel("Classification Accuracy (%)")
plt.ylabel("Frequency")
plt.title("Impact of Image Size on Classification Accuracy")
plt.legend(loc="upper left")
plt.show()

dimensions = ("50x50", "60x60", "70x70", "80x80", "90x90")
y_pos = np.arange(len(dimensions))
means = [results_50x50.mean(), results_60x60.mean(), results_70x70.mean(), results_80x80.mean(), results_90x90.mean()]

plt.bar(y_pos, means, align="center")
plt.xticks(y_pos, dimensions)
plt.xlabel("Image Size")
plt.ylabel("Mean Classification Accuracy (%)")
plt.title("Impact of Image Size on Mean Classification Accuracy")
plt.show()