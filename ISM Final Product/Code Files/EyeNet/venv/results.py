import matplotlib
import matplotlib.pyplot as plt
from datascience import Table
import numpy as np

t = Table().with_columns("who", [1, 2, 3, 4, 5], "am", [1, 2, 3, 4, 5])
plt.switch_backend("TkAgg")
plt.plot(t.column("who"))
plt.show()