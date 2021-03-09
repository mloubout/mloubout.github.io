---
title: "A large-scale framework for symbolic implementations of seismic inversion algorithms in Julia"
collection: publications
permalink: /publication/2019-03-01-A-large-scale-framework-for-symbolic-implementations-of-seismic-inversion-algorithms-in-Julia
excerpt: '(Geophysics)'
date: 2019-03-01
venue: 'A large-scale framework for symbolic implementations of seismic inversion algorithms in Julia'
paperurl: 'https://slim.gatech.edu/Publications/Public/Journals/Geophysics/2019/witte2018alf/witte2018alf.pdf'
citation: ' Philipp Witte,  Mathias Louboutin,  Navjot Kukreja,  Fabio Luporini,  Michael Lange,  Gerard Gorman,  Felix Herrmann, &quot;A large-scale framework for symbolic implementations of seismic inversion algorithms in Julia.&quot; A large-scale framework for symbolic implementations of seismic inversion algorithms in Julia, 2019.'
---
(Geophysics)

[Access paper here](https://slim.gatech.edu/Publications/Public/Journals/Geophysics/2019/witte2018alf/witte2018alf.pdf){:target="_blank"}

Writing software packages for seismic inversion is a very challenging task, since problems such as full-waveform inversion or least-squares imaging are both algorithmically and computationally demanding due to the large number of unknown parameters and the fact that we are propagating waves over many wavelengths. Software frameworks therefore need to combine both versatility and performance to provide geophysicists with the means and flexibility to implement complex algorithms that scale to exceedingly large 3D problems. Following these principles, we introduce the Julia Devito Inversion framework, an open-source software package in Julia for large-scale seismic modeling and inversion based on Devito, a domain-specific language compiler for automatic code generation. The framework consists of matrix-free linear operators for implementing seismic inversion algorithms that closely resembles the mathematical notation, a flexible resilient parallelization and an interface to Devito for generating optimized stencil code to solve the underlying wave equations. In comparison to many manually optimized industry codes written in low-level languages, our software is built on the idea of independent layers of abstractions and user interfaces with symbolic operators, making it possible to manage both the complexity of algorithms and performance optimizations, while preserving modularity, which allows for a level of expressiveness needed to formulate a broad range of wave-equation-based inversion problems. Through a series of numerical examples, we demonstrate that this allows users to implement algorithms for waveform inversion and imaging as simple Julia scripts that scale to large-scale 3D problems; thus providing a truly performant research and production framework.
