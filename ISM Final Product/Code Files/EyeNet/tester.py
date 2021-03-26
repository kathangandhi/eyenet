import numpy as np

sample = np.random.random_sample(100) * 100
sample = np.array(sample).astype(int)
print(sample)

symptoms_indices = np.arange(0, 1467)
sample = np.random.choice(symptoms_indices, 100)
if(600 in sample):
    print(sample)

zero = np.zeros(5)
one = np.ones(5)
print(np.concatenate([zero, one]))