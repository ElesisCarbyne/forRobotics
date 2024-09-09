import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

rect = plt.Rectangle((0, 0), 2, 1, color="brown", alpha=0.75)
rect2 = plt.Rectangle((0, 1), 2, 1, color="gray", alpha=1)
circ = plt.Circle((1, 1.5), 0.25, color="yellow")
line = plt.Line2D([0, 2], [1, 1], color="black", linewidth=5)

y1 = np.linspace(0.5, 1.5, 20)
y2 = np.linspace(1.5, 0.5, 20)
y = np.concatenate((y1, y2))

for i in range(len(y)):
    circ = plt.Circle((1, y[i]), 0.25, color="yellow") # 해가 위로 올라갔다 내려갔다 하는 애니메이션을 구현한다

    ax.add_patch(rect)
    ax.add_patch(rect2)
    ax.add_patch(circ)
    ax.add_line(line)

    plt.gca().set_aspect("equal")
    plt.ylim(0, 2)
    plt.xlim(0, 2)

    plt.pause(0.05)
    circ.remove()
    # clear_output(wait=True)

plt.close()