import group_prediction
from pathlib import Path
import feature_extraction
import training

feature_extraction.extract(Path("retinopathy-dataset-master"))
training.train()

results = []
results.append(group_prediction.sample_testing(Path("retinopathy-dataset-master")))
print(results[0])

with open("results-90x90.txt", "a") as f:
    f.write(str(results[0])+"\n")