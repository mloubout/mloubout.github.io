---
title: "A large-scale framework in Julia for fast prototyping of seismic inversion algorithms"
etype: 'presentation'
collection: publications
permalink: /publication/2017-01-01-A-large-scale-framework-in-Julia-for-fast-prototyping-of-seismic-inversion-algorithms
date: 2017-01-01
venue: 'A large-scale framework in Julia for fast prototyping of seismic inversion algorithms'
paperurl: 'https://slim.gatech.edu/Publications/Public/Conferences/SINBAD/2017/Fall/witte2017SINBADFals/witte2017SINBADFals.pdf'
citation: ' Philipp Witte,  Mathias Louboutin,  Felix Herrmann, &quot;A large-scale framework in Julia for fast prototyping of seismic inversion algorithms.&quot; A large-scale framework in Julia for fast prototyping of seismic inversion algorithms, 2017.'
---
[Access paper here](https://slim.gatech.edu/Publications/Public/Conferences/SINBAD/2017/Fall/witte2017SINBADFals/witte2017SINBADFals.pdf){:target="_blank"}

We present our progress on a large-scale seismic modeling workflow in Julia for wave-equation based inversion. The software offers a range of high-level abstractions to easily express PDE constrained optimization problems in terms of linear algebra expressions, while utilizing the DSL Devito to symbolically express the underlying PDEs and to generate fast and parallel code for solving them. Data containers and linear operators can be set up without much effort from input SEG-Y data and scale to large-scale 3D applications. This talk provides an overview of the basic functionalities of our software and applications to least squares imaging and 3D FWI.
