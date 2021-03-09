---
title: "Devito (v3.1.0): an embedded domain-specific language for finite differences and geophysical exploration"
collection: publications
permalink: /publication/2019-01-01-Devito-v310-an-embedded-domain-specific-language-for-finite-differences-and-geophysical-exploration
excerpt: '(Geoscientific Model Development)'
date: 2019-01-01
venue: 'Devito (v3.1.0): an embedded domain-specific language for finite differences and geophysical exploration'
paperurl: 'https://slim.gatech.edu/Publications/Public/Journals/GMD/2019/louboutin2018dae/louboutin2018dae.pdf'
citation: ' Mathias Louboutin,  Michael Lange,  Fabio Luporini,  Navjot Kukreja,  Philipp Witte,  Felix Herrmann,  Paulius Velesko,  Gerard Gorman, &quot;Devito (v3.1.0): an embedded domain-specific language for finite differences and geophysical exploration.&quot; Devito (v3.1.0): an embedded domain-specific language for finite differences and geophysical exploration, 2019.'
---
(Geoscientific Model Development)

[Access paper here](https://slim.gatech.edu/Publications/Public/Journals/GMD/2019/louboutin2018dae/louboutin2018dae.pdf){:target="_blank"}

We introduce Devito, a new domain-specific language for implementing high-performance finite difference partial differential equation solvers. The motivating application is exploration seismology where methods such as Full-Waveform Inversion and Reverse-Time Migration are used to invert terabytes of seismic data to create images of the earth{\textquoteright}s subsurface. Even using modern supercomputers, it can take weeks to process a single seismic survey and create a useful subsurface image. The computational cost is dominated by the numerical solution of wave equations and their corresponding adjoints. Therefore, a great deal of effort is invested in aggressively optimizing the performance of these wave-equation propagators for different computer architectures. Additionally, the actual set of partial differential equations being solved and their numerical discretization is under constant innovation as increasingly realistic representations of the physics are developed, further ratcheting up the cost of practical solvers. By embedding a domain-specific language within Python and making heavy use of SymPy, a symbolic mathematics library, we make it possible to develop finite difference simulators quickly using a syntax that strongly resembles the mathematics. The Devito compiler reads this code and applies a wide range of analysis to generate highly optimized and parallel code. This approach can reduce the development time of a verified and optimized solver from months to days.
