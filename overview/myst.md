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

Here is a [reference to the intro](../intro.md). Here is a reference to [](section-label).

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
:label: eq:one
\int_0^\alpha f(x) dx = I_\alpha
```

see Equation {eq}`eq:one` for details.
Here another equation without number

$$
  \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
$$

## MyST markdown features

### Figures and Tables that can be referenced

To reference a figure in your book, first add a figure and ensure that it has both a name as well as a caption associated with it:

```{figure} ../logo.png
:name: fig:myfig

My figure title.
```

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum non auctor lacus. 
Sed vitae metus cursus, viverra diam vel, interdum ligula. Curabitur sollicitudin nulla non nulla cursus euismod. 

```{table} My table title
:name: tab:mytab

| col 1 | col 2 |
|---|---|
| 3 | 4 |
| 1 | 9 |
| 4 | 2 |
| 3 | 8 |
| 2 | 1 |
```

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum non auctor lacus. 
Sed vitae metus cursus, viverra diam vel, interdum ligula. Curabitur sollicitudin nulla non nulla cursus euismod. 

As shown in {numref}`fig:myfig` and {numref}`tab:mytab`

### Grid of cards

::::{grid}
:gutter: 3

:::{grid-item-card} One!
Here's the first card.
:::

:::{grid-item-card} Two!
Here's the second card.
:::

:::{grid-item-card} Three!
Here's the third card.
:::
::::

### Dropdown content

```{dropdown} Here's my dropdown
And here's my dropdown content
```

### Tab content

````{tab-set}
```{tab-item} Tab 1 title
My first tab
```

```{tab-item} Tab 2 title
My second tab with `some code`!
```
````



