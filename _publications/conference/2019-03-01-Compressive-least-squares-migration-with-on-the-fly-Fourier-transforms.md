---
title: "Compressive least squares migration with on-the-fly Fourier transforms"
etype: 'conference'
collection: publications
permalink: /publication/2019-03-01-Compressive-least-squares-migration-with-on-the-fly-Fourier-transforms
excerpt: '(SIAM CSE)'
date: 2019-03-01
venue: 'Compressive least squares migration with on-the-fly Fourier transforms'
citation: ' Philipp Witte,  Mathias Louboutin,  Fabio Luporini,  Gerard Gorman,  Felix Herrmann, &quot;Compressive least squares migration with on-the-fly Fourier transforms.&quot; Compressive least squares migration with on-the-fly Fourier transforms, 2019.'
---
(SIAM CSE)

Use [Google Scholar](https://scholar.google.com/scholar?q=Compressive+least+squares+migration+with+on+the+fly+Fourier+transforms){:target="_blank"} for full citation
Least-squares seismic imaging is an inversion-based approach for accurately imaging the earth{\textquoteright}s subsurface. However, in the time-domain, the computational cost and memory requirements of this approach scale with the size and recording length of the seismic experiment, thus making this approach often prohibitively expensive in practice. To overcome these issues, we borrow ideas from compressive sensing and signal processing and introduce an algorithm for sparsity-promoting seismic imaging using on-the-fly Fourier transforms. By computing gradients and functions values for random subsets of source locations and frequencies, we considerably limit the number of wave equation solves, while on-the-fly Fourier transforms allow computing an arbitrary number of monochromatic frequency-domain wavefields with a time-domain modeling code and without having to solve large-scale Helmholtz equations. The memory requirements of this approach are independent of the number of time steps and solely depend on the number of frequencies, which determine the amount of crosstalk and subsampling artifacts in the image. We show the application of our approach to several large-scale open source data sets and compare the results to a conventional time-domain approach with optimal checkpointing.
