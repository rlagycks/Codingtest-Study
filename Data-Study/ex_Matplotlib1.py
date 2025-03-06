#maplotlib 홈페이지에서 예제로 만들어진 코드
#공부 하면서 수정해볼 계획획

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.