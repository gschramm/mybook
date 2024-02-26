# %% [markdown]
# # A pure python script containing plots

# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
from functools import partial

# %%
x = np.linspace(-1, 1, 100)
y = x**3

# %% [markdown]
# ## Let's plot the data
# Because plotting is fun

# %%

fig, ax = plt.subplots()
ax.plot(x, y, ".-")
ax.set_title("static plot")
fig.show()

# %% [markdown]
# ## Let's create an animation
# Because animations are fun


# %%
def update_line(frm, line, time, y):
    line.set_data(time[:frm], y[:frm])


# %%
t = np.linspace(0, 2 * np.pi)
x = np.sin(t)

fig2, ax2 = plt.subplots()
ax2.axis([0, 2 * np.pi, -1, 1])
(l,) = ax2.plot(t, x)
ax2.set_title("animated plot")
fig2.show()

# %%
ani = matplotlib.animation.FuncAnimation(
    fig2, partial(update_line, line=l, time=t, y=x), frames=len(t), interval=20
)

from IPython.display import HTML

HTML(ani.to_jshtml())
