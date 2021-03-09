---
title: "Leveraging symbolic math for rapid development of applications for seismic modeling"
etype: 'conference'
collection: publications
permalink: /publication/2017-03-01-Leveraging-symbolic-math-for-rapid-development-of-applications-for-seismic-modeling
excerpt: '(Oil and Gas HPC Conference, Rice University)'
date: 2017-03-01
venue: 'Leveraging symbolic math for rapid development of applications for seismic modeling'
paperurl: 'https://slim.gatech.edu/Publications/Public/Conferences/OGHPC/2017/kukreja2016OGHPClsm/kukreja2016OGHPClsm.pdf'
citation: ' Navjot Kukreja,  Mathias Louboutin,  Michael Lange,  Fabio Luporini,  Gerard Gorman, &quot;Leveraging symbolic math for rapid development of applications for seismic modeling.&quot; Leveraging symbolic math for rapid development of applications for seismic modeling, 2017.'
---
(Oil and Gas HPC Conference, Rice University)

[Access paper here](https://slim.gatech.edu/Publications/Public/Conferences/OGHPC/2017/kukreja2016OGHPClsm/kukreja2016OGHPClsm.pdf){:target="_blank"}

Wave propagation kernels are the core of many commonly used algorithms for inverse problems in exploration geophysics. While they are easy to write and analyze for the simplied cases, the code quickly becomes complex when the physics needs to be made more precise or the performance of these codes is to be optimized. Signicant eort is repeated every time new forms of physics need to be implemented, or a new computing platform to be supported. The use of symbolic mathematics as a domain specic language (DSL) for input, combined with automatic generation of high performance code customized for the target hardware platform is a promising approach to maximize code reuse. Devito is a DSL for nite dierence that uses symbolic mathematics to generate optimized code for wave propagation based on a provided wave equation. It enables rapid application development in a eld where the average time spent on development has historically been in weeks and months. The Devito DSL system is completely wrapped within the Python programming language and the fact that the running code is in C is completely transparent, making it simple to include Devito as part of a larger work ow including multiple applications over a large cluster.
