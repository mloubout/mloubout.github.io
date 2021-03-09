---
title: "Performance prediction of finite-difference solvers for different computer architectures"
etype: 'article'
collection: publications
permalink: /publication/2017-08-01-Performance-prediction-of-finite-difference-solvers-for-different-computer-architectures
excerpt: '(Computers \&amp; Geosciences)'
date: 2017-08-01
venue: 'Performance prediction of finite-difference solvers for different computer architectures'
paperurl: 'https://slim.gatech.edu/Publications/Public/Journals/ComputersAndGeosciences/2016/louboutin2016ppf/louboutin2016ppf.pdf'
citation: ' Mathias Louboutin,  Michael Lange,  Felix Herrmann,  Navjot Kukreja,  Gerard Gorman, &quot;Performance prediction of finite-difference solvers for different computer architectures.&quot; Performance prediction of finite-difference solvers for different computer architectures, 2017.'
---
(Computers \&amp; Geosciences)

[Access paper here](https://slim.gatech.edu/Publications/Public/Journals/ComputersAndGeosciences/2016/louboutin2016ppf/louboutin2016ppf.pdf){:target="_blank"}

The life-cycle of a partial differential equation (PDE) solver is often characterized by three development phases: the development of a stable numerical discretization; development of a correct (verified) implementation; and the optimization of the implementation for different computer architectures. Often it is only after significant time and effort has been invested that the performance bottlenecks of a PDE solver are fully understood, and the precise details varies between different computer architectures. One way to mitigate this issue is to establish a reliable performance model that allows a numerical analyst to make reliable predictions of how well a numerical method would perform on a given computer architecture, before embarking upon potentially long and expensive implementation and optimization phases. The availability of a reliable performance model also saves developer effort as it both informs the developer on what kind of optimisations are beneficial, and when the maximum expected performance has been reached and optimisation work should stop. We show how discretization of a wave-equation can be theoretically studied to understand the performance limitations of the method on modern computer architectures. We focus on the roofline model, now broadly used in the high-performance computing community, which considers the achievable performance in terms of the peak memory bandwidth and peak floating point performance of a computer with respect to algorithmic choices. A first principles analysis of operational intensity for key time-stepping finite-difference algorithms is presented. With this information available at the time of algorithm design, the expected performance on target computer systems can be used as a driver for algorithm design.
