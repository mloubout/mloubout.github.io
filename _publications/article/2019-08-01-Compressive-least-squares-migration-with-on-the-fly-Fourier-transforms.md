---
title: "Compressive least-squares migration with on-the-fly Fourier transforms"
etype: 'article'
collection: publications
permalink: /publication/2019-08-01-Compressive-least-squares-migration-with-on-the-fly-Fourier-transforms
excerpt: '(Geophysics)'
date: 2019-08-01
venue: 'Compressive least-squares migration with on-the-fly Fourier transforms'
paperurl: 'https://slim.gatech.edu/Publications/Public/Journals/Geophysics/2019/witte2018cls/witte2018cls.pdf'
citation: ' Philipp Witte,  Mathias Louboutin,  Fabio Luporini,  Gerard Gorman,  Felix Herrmann, &quot;Compressive least-squares migration with on-the-fly Fourier transforms.&quot; Compressive least-squares migration with on-the-fly Fourier transforms, 2019.'
---
(Geophysics)

[Access paper here](https://slim.gatech.edu/Publications/Public/Journals/Geophysics/2019/witte2018cls/witte2018cls.pdf){:target="_blank"}

Least-squares reverse-time migration is a powerful approach for true amplitude seismic imaging of complex geological structures, but the successful application of this method is currently hindered by its enormous computational cost, as well as high memory requirements for computing the gradient of the objective function. We tackle these problems by introducing an algorithm for low-cost sparsity-promoting least-squares migration using on-the-fly Fourier transforms. We formulate the least-squares migration objective function in the frequency domain and compute gradients for randomized subsets of shot records and frequencies, thus significantly reducing data movement and the number of overall wave equations solves. By using on-the-fly Fourier transforms, we can compute an arbitrary number of monochromatic frequency-domain wavefields with a time-domain modeling code, instead of having to solve individual Helmholtz equations for each frequency, which quickly becomes computationally infeasible when moving to high frequencies. Our numerical examples demonstrate that compressive imaging with on-the-fly Fourier transforms provides a fast and memory-efficient alternative to time-domain imaging with optimal checkpointing, whose memory requirements for a fixed background model and source wavelet is independent of the number of time steps. Instead, memory and additional computational cost grow with the number of frequencies and determine the amount of subsampling artifacts and crosstalk. In contrast to optimal checkpointing, this offers the possibility to trade both memory and computational cost for image quality or a larger number of iterations and is advantageous in new computing environments such as the cloud, where compute is often cheaper than memory and data movement.
