---
title: "Raising the abstraction to separate concerns: enabling different physics for geophysical exploration"
collection: publications
permalink: /publication/2017-02-03-01-Raising-the-abstraction-to-separate-concerns-enabling-different-physics-for-geophysical-exploration
excerpt: '(SIAM Conference on Computational Science and Engineering, Atlanta)'
date: 2017-02-03-01
venue: 'Raising the abstraction to separate concerns: enabling different physics for geophysical exploration'
paperurl: 'https://slim.gatech.edu/Publications/Public/Conferences/SIAM/2017/louboutin2017SIAMras/louboutin2017SIAMras_pres.mov'
citation: ' Mathias Louboutin,  Michael Lange,  Navjot Kukreja,  Fabio Luporini,  Felix Herrmann,  Gerard Gorman, &quot;Raising the abstraction to separate concerns: enabling different physics for geophysical exploration.&quot; Raising the abstraction to separate concerns: enabling different physics for geophysical exploration, 2017.'
---
(SIAM Conference on Computational Science and Engineering, Atlanta)

[Access paper here](https://slim.gatech.edu/Publications/Public/Conferences/SIAM/2017/louboutin2017SIAMras/louboutin2017SIAMras_pres.mov){:target="_blank"}

Full-waveform inversion is a PDE-constrained optimisation problem involving massive amounts of data (petabytes) and large numbers of unknowns (O(10^9)). This well known compute-intensive and data-intensive is extremely challenging for several reasons. First, there is the complexity of having to handle extremely large data volumes with metadata related to experimental details in the field, and the discretization of the unknown earth parameters and approximate physics. Second, reduced or adjoint-state methods call for computationally intensive PDE solves for each source experiment (of which there are thousands) for each iteration of a gradient-based optimization scheme. The talks will give an overview how carefully chosen layers of abstraction can help manage both the complexity and scale of inversion while still achieving the high degree of computational performance required to make full-waveform a practical tool. Specifically, the presentations will focus on domain specific stencil language for time-stepping methods to solve various types of wave equations and on abstracts for large-scale parallel optimization frameworks.
