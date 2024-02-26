---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# MyST markdown incl. math and code

This is some sample text.

(section-label)=
## A section containing code

Here is a [reference to the intro](intro.md). Here is a reference to [](section-label).

```{code-cell}
print(2 + 2)
```

```{code-cell}
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = x**2

fig, ax = plt.subplots()
ax.plot(x,y)
```

## A section containing math

Random inline math $\alpha=1$ leading to an equation

```{math}
:label: eq-one
\int_0^\alpha f(x) dx = I_\alpha
```
which can be referred to [](eq-one). Here another equation
without number

$$
  \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
$$

