---
title: "Architecture and performance of Devito, a system for automated stencil computation"
etype: 'article'
collection: publications
permalink: /publication/2020-04-01-Architecture-and-performance-of-Devito-a-system-for-automated-stencil-computation
excerpt: '(ACM Trans. Math. Softw.)'
date: 2020-04-01
venue: 'Architecture and performance of Devito, a system for automated stencil computation'
paperurl: 'https://slim.gatech.edu/Publications/Public/Journals/ACMTOMS/2020/luporini2018aap/luporini2018aap.pdf'
citation: ' Fabio Luporini,  Michael Lange,  Mathias Louboutin,  Navjot Kukreja,  Jan H{\&quot;u}ckelheim,  Charles Yount,  Philipp Witte,  Paul Kelly,  Gerard Gorman,  Felix Herrmann, &quot;Architecture and performance of Devito, a system for automated stencil computation.&quot; Architecture and performance of Devito, a system for automated stencil computation, 2020.'
---
(ACM Trans. Math. Softw.)

[Access paper here](https://slim.gatech.edu/Publications/Public/Journals/ACMTOMS/2020/luporini2018aap/luporini2018aap.pdf){:target="_blank"}

Stencil computations are a key part of many high-performance computing applications, such as image processing, convolutional neural networks, and finite-difference solvers for partial differential equations. Devito is a framework capable of generating highly-optimized code given symbolic equations expressed in Python, specialized in, but not limited to, affine (stencil) codes. The lowering process {\textendash} from mathematical equations down to C++ code {\textendash} is performed by the Devito compiler through a series of intermediate representations. Several performance optimizations are introduced, including advanced common sub-expressions elimination, tiling and parallelization. Some of these are obtained through well-established stencil optimizers, integrated in the back-end of the Devito compiler. The architecture of the Devito compiler, as well as the performance optimizations that are applied when generating code, are presented. The effectiveness of such performance optimizations is demonstrated using operators drawn from seismic imaging applications.
