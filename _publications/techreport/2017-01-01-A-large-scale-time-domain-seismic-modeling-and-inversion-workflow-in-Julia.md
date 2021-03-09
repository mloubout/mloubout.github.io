---
title: "A large-scale time-domain seismic modeling and inversion workflow in Julia"
etype: 'techreport'
collection: publications
permalink: /publication/2017-01-01-A-large-scale-time-domain-seismic-modeling-and-inversion-workflow-in-Julia
date: 2017-01-01
venue: 'A large-scale time-domain seismic modeling and inversion workflow in Julia'
paperurl: 'https://slim.gatech.edu/Publications/Public/TechReport/2017/witte2016OGHPClst/witte2016OGHPClst.pdf'
citation: ' Philipp Witte,  Mathias Louboutin,  Gerard Gorman,  Felix Herrmann, &quot;A large-scale time-domain seismic modeling and inversion workflow in Julia.&quot; A large-scale time-domain seismic modeling and inversion workflow in Julia, 2017.'
---
[Access paper here](https://slim.gatech.edu/Publications/Public/TechReport/2017/witte2016OGHPClst/witte2016OGHPClst.pdf){:target="_blank"}

We present our initial steps towards the development of a large-scale seismic modeling workflow in Julia that provides a framework for wave equation based inversion methods like full waveform inversion or least squares migration. Our framework is based on the Devito, a finite difference domain specific language compiler that generates highly optimized and parallel code. We develop a flexible workflow that is based on abstract matrixfree linear operators and enables developers to write code that closely resembles the underlying math, while at the same time leveraging highly optimized wave equation solvers, allowing us to solve large-scale three-dimensional inverse problems.
