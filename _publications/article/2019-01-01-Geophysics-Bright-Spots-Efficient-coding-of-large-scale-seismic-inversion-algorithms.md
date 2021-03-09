---
title: "Geophysics Bright Spots: Efficient coding of large-scale seismic inversion algorithms"
etype: 'article'
collection: publications
permalink: /publication/2019-01-01-Geophysics-Bright-Spots-Efficient-coding-of-large-scale-seismic-inversion-algorithms
excerpt: '(The Leading Edge)'
date: 2019-01-01
venue: 'Geophysics Bright Spots: Efficient coding of large-scale seismic inversion algorithms'
paperurl: 'https://library.seg.org/doi/10.1190/tle38060482.1'
citation: ' Philipp Witte,  Mathias Louboutin,  Navjot Kukreja,  Fabio Luporini,  Michael Lange,  Gerard Gorman,  Felix Herrmann, &quot;Geophysics Bright Spots: Efficient coding of large-scale seismic inversion algorithms.&quot; Geophysics Bright Spots: Efficient coding of large-scale seismic inversion algorithms, 2019.'
---
(The Leading Edge)

[Access paper here](https://library.seg.org/doi/10.1190/tle38060482.1){:target="_blank"}

In {\textquotedblleft}A large-scale framework for symbolic implementations of seismic inversion algorithms in Julia,{\textquotedblright} Witte et al. describe new developments in how to code complex geophysical algorithms in a concise way. Subsurface seismic imaging and parameter estimation are among the most computationally challenging problems in the scientific community. Codes for solving seismic inverse problems, such as FWI or least-squares reverse time migration (LS-RTM), need to be highly optimized, but at the same time, facilitate the implementation of complex optimization algorithms. Traditionally, production-level codes in the oil and gas industry were exclusively written in low-level languages, such as C or Fortran, with extensive amounts of manual performance optimizations, thus making code maintenance, debugging, and adoption of new algorithms prohibitively challenging. Witte et al. present a paradigm of software engineering for seismic inverse problems based on symbolic user interfaces and code generation with automated performance optimization. Inspired by recent deep learning frameworks, the Julia Devito inversion framework (JUDI; an open-source software package) combines high-level abstractions for expressing seismic inversion algorithms with a domain-specific language compiler called Devito for solving the underlying wave equations. Devito{\textquoteright}s generated code is compiled just in time and outperforms codes with manual performance optimizations. JUDI utilizes Julia{\textquoteright}s high-level parallelization, making the software easily adaptable to a variety of computing environments such as densely connected HPC clusters or the cloud. The numerical examples (Figure 3) demonstrate the ability to implement a variety of complex algorithms for FWI and LS-RTM in a few lines of Julia code and run it on large-scale 3D models. The paper concludes that abstractions and performance are not mutually exclusive, and use of symbolic user interfaces can facilitate the implementation of new and innovative seismic inversion algorithms.
