# %% [markdown]
# # My Script

# %%
import numpy as np

x = np.linspace(-1, 1, 100)
y = x**3

# %% [markdown]
# ## Let's plot the data
# Because plotting is fun

# %%
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(x, y, ".-")
