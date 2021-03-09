---
title: "Optimizing the computational performance of time-domain modellingtextendash-leveraging multiple right-hand-sides"
collection: publications
permalink: /publication/2017-01-01-Optimizing-the-computational-performance-of-time-domain-modellingtextendash-leveraging-multiple-right-hand-sides
date: 2017-01-01
venue: 'Optimizing the computational performance of time-domain modellingtextendash-leveraging multiple right-hand-sides'
paperurl: 'https://slim.gatech.edu/Publications/Public/TechReport/2017/louboutin2016OGHPCocp/louboutin2016OGHPCocp.pdf'
citation: ' Mathias Louboutin,  Gerard Gorman,  Felix Herrmann, &quot;Optimizing the computational performance of time-domain modellingtextendash-leveraging multiple right-hand-sides.&quot; Optimizing the computational performance of time-domain modellingtextendash-leveraging multiple right-hand-sides, 2017.'
---
[Access paper here](https://slim.gatech.edu/Publications/Public/TechReport/2017/louboutin2016OGHPCocp/louboutin2016OGHPCocp.pdf){:target="_blank"}

Exploration geophysics heavily relies upon fast solvers for the wave-equation and its adjoint. The main computational cost of a wave-equation solver is to compute the Laplacian, or more complex finite-difference operators, at every time step. The performance of many discretizations is limited by the relatively low operational intensity (number of floating point operations divided by memory traffic) of the finite-difference stencil. Solving the wave-equation for multiple sources/right-hand-sides (RHSs) at once mitigates this problem by increasing the operational intensity. This is implemented by rewriting the classical matrix-vector product into a matrix-matrix product where each column of the second matrix represent the solution wavefield for each given source. This minor modification to the solver is shown to achieve a 2-4 times speedup compared to a single source solver. We concentrate in this paper on acoustic modelling, but our approach can easily be extended to anisotropic or elastic cases for both forward and adjoint modelling.
