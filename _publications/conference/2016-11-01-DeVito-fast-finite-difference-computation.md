---
title: "DeVito: fast finite difference computation"
etype: 'conference'
collection: publications
permalink: /publication/2016-11-01-DeVito-fast-finite-difference-computation
excerpt: '(Super Computing, Utah)'
date: 2016-11-01
venue: 'DeVito: fast finite difference computation'
paperurl: 'https://slim.gatech.edu/Publications/Public/Conferences/SC/2016/deaguiar2016SCdff/deaguiar2016SCdff_poster.pdf'
citation: ' Marcos Aguiar,  Gerard Gorman,  Felix Herrmann,  Navjot Kukreja,  Michael Lange,  Mathias Louboutin,  Felippe Zacarias, &quot;DeVito: fast finite difference computation.&quot; DeVito: fast finite difference computation, 2016.'
---
(Super Computing, Utah)

[Access paper here](https://slim.gatech.edu/Publications/Public/Conferences/SC/2016/deaguiar2016SCdff/deaguiar2016SCdff_poster.pdf){:target="_blank"}

Seismic imaging, used in energy exploration, is arguably the most compute and data intensive application in the private sector. The commonly used methods involve solving the wave equations numerically using finite difference formulations. Writing optimized code for these applications involves multiple man-years of effort that need to be repeated every time a new development needs to be factored in {\textendash} for every target platform. DeVito is a new tool for performing optimized Finite Difference (FD) computation from high-level symbolic problem definitions. The application developer needs to provide a differential equation in symbolic form. DeVito performs automated code generation and Just-In-Time (JIT) compilation based on this symbolic equation to create and execute highly optimized Finite Difference kernels on multiple computer platforms. DeVito has been designed to be used as part of complex workflows involving data flows across multiple applications over different nodes of a cluster.
