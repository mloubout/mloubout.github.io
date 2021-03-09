---
title: "Temporal blocking of finite-difference stencil operators with sparse &quot;off-the-grid&quot; sources"
collection: publications
permalink: /publication/2020-10-01-Temporal-blocking-of-finite-difference-stencil-operators-with-sparse-off-the-grid-sources
excerpt: 'Submitted to IPDPS'
date: 2020-10-01
venue: 'Temporal blocking of finite-difference stencil operators with sparse &quot;off-the-grid&quot; sources'
paperurl: 'https://arxiv.org/pdf/2010.10248.pdf'
citation: ' George Bisbas,  Fabio Luporini,  Mathias Louboutin,  Rhodri Nelson,  Gerard Gorman,  Paul Kelly, &quot;Temporal blocking of finite-difference stencil operators with sparse &amp;quot;off-the-grid&amp;quot; sources.&quot; Temporal blocking of finite-difference stencil operators with sparse &amp;quot;off-the-grid&amp;quot; sources, 2020.'
---
Submitted to IPDPS

[Access paper here](https://arxiv.org/pdf/2010.10248.pdf){:target="_blank"}

Stencil kernels dominate a range of scientific applications including seismic and medical imaging, image processing, and neural networks. Temporal blocking is a performance optimisation that aims to reduce the required memory bandwidth of stencil computations by re-using data from the cache for multiple time steps. It has already been shown to be beneficial for this class of algorithms. However, optimising stencils for practical applications remains challenging. These computations often include sparsely located operators, not aligned with the computational grid (&quot;off-the-grid&quot;). For example, our work is motivated by sources that inject a wavefield and measurements interpolating grid values. The resulting data dependencies make the adoption of temporal blocking much more challenging. We propose a methodology to inspect these data dependencies and reorder the computation, leading to performance gains in stencil codes where temporal blocking has not been applicable. We implement this novel scheme in the Devito domain-specific compiler toolchain. Devito implements a domain-specific language embedded in Python to generate optimised partial differential equation solvers using the finite-difference method from high-level symbolic problem definitions. We evaluate our scheme using isotropic acoustic, anisotropic acoustic and isotropic elastic wave propagators of industrial significance. Performance evaluation, after auto-tuning, shows that this enables substantial performance improvement through temporal blocking, over highly-optimised vectorized spatially-blocked code of up to 1.6x.
