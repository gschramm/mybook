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
---
width: 300px
name: fig:myfig
align: center
---
Here is my figure caption!
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

### Algorithms

```{prf:algorithm} Ford–Fulkerson
:label: my-algorithm

**Inputs** Given a Network $G=(V,E)$ with flow capacity $c$, a source node $s$, and a sink node $t$

**Output** Compute a flow $f$ from $s$ to $t$ of maximum value

1. $f(u, v) \leftarrow 0$ for all edges $(u,v)$
2. While there is a path $p$ from $s$ to $t$ in $G_{f}$ such that $c_{f}(u,v)>0$
	for all edges $(u,v) \in p$:

	1. Find $c_{f}(p)= \min \{c_{f}(u,v):(u,v)\in p\}$
	2. For each edge $(u,v) \in p$

		1. $f(u,v) \leftarrow f(u,v) + c_{f}(p)$ *(Send flow along the path)*
		2. $f(u,v) \leftarrow f(u,v) - c_{f}(p)$ *(The flow might be "returned" later)*
```

As shown in {prf:ref}`my-algorithm`.

### Theorems

````{prf:theorem} Orthogonal-Projection-Theorem
:label: my-theorem

Given $y \in \mathbb R^n$ and linear subspace $S \subset \mathbb R^n$,
there exists a unique solution to the minimization problem

```{math}
\hat y := \text{argmin}_{z \in S} \|y - z\|
```

The minimizer $\hat y$ is the unique vector in $\mathbb R^n$ that satisfies

* $\hat y \in S$

* $y - \hat y \perp S$


The vector $\hat y$ is called the **orthogonal projection** of $y$ onto $S$.
````

As stated in {prf:ref}`my-theorem`.

### Embedding a video

![giphy](https://media.giphy.com/media/yoJC2A59OCZHs1LXvW/giphy.gif)
