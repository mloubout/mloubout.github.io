---
title: "Scaling through abstractions textendash high-performance vectorial wave simulations for seismic inversion with Devito"
etype: 'techreport'
collection: publications
permalink: /publication/2020-04-01-Scaling-through-abstractions-textendash-high-performance-vectorial-wave-simulations-for-seismic-inversion-with-Devito
date: 2020-04-01
venue: 'Scaling through abstractions textendash high-performance vectorial wave simulations for seismic inversion with Devito'
paperurl: 'https://slim.gatech.edu/Publications/Public/TechReport/2020/louboutin2020SCsta/louboutin2020SCsta.html'
citation: ' Mathias Louboutin,  Fabio Luporini,  Philipp Witte,  Rhodri Nelson,  George Bisbas,  Jan Thorbecke,  Felix Herrmann,  Gerard Gorman, &quot;Scaling through abstractions textendash high-performance vectorial wave simulations for seismic inversion with Devito.&quot; Scaling through abstractions textendash high-performance vectorial wave simulations for seismic inversion with Devito, 2020.'
---
[Access paper here](https://slim.gatech.edu/Publications/Public/TechReport/2020/louboutin2020SCsta/louboutin2020SCsta.html){:target="_blank"}

[Devito] is an open-source Python project based on domain-specific language and compiler technology. Driven by the requirements of rapid HPC applications development in exploration seismology, the language and compiler have evolved significantly since inception. Sophisticated boundary conditions, tensor contractions, sparse operations and features such as staggered grids and sub-domains are all supported; operators of essentially arbitrary complexity can be generated. To accommodate this flexibility whilst ensuring performance, data dependency analysis is utilized to schedule loops and detect computational-properties such as parallelism. In this article, the generation and simulation of MPI-parallel propagators (along with their adjoints) for the pseudo-acoustic wave-equation in tilted transverse isotropic media and the elastic wave-equation are presented. Simulations are carried out on industry scale synthetic models in a HPC Cloud system and reach a performance of 28TFLOP/s, hence demonstrating Devito{\textquoteright}s suitability for production-grade seismic inversion problems.
