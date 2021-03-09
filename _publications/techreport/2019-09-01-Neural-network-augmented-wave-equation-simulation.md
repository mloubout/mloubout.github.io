---
title: "Neural network augmented wave-equation simulation"
collection: publications
permalink: /publication/2019-09-01-Neural-network-augmented-wave-equation-simulation
date: 2019-09-01
venue: 'Neural network augmented wave-equation simulation'
paperurl: 'https://slim.gatech.edu/Publications/Public/TechReport/2019/siahkoohi2019TRnna/siahkoohi2019TRnna.html'
citation: ' Ali Siahkoohi,  Mathias Louboutin,  Felix Herrmann, &quot;Neural network augmented wave-equation simulation.&quot; Neural network augmented wave-equation simulation, 2019.'
---
[Access paper here](https://slim.gatech.edu/Publications/Public/TechReport/2019/siahkoohi2019TRnna/siahkoohi2019TRnna.html){:target="_blank"}

Accurate forward modeling is important for solving inverse problems. An inaccurate wave-equation simulation, as a forward operator, will offset the results obtained via inversion. In this work, we consider the case where we deal with incomplete physics. One proxy of incomplete physics is an inaccurate discretization of Laplacian in simulation of wave equation via finite-difference method. We exploit intrinsic one-to-one similarities between timestepping algorithm with Convolutional Neural Networks (CNNs), and propose to intersperse CNNs between low-fidelity timesteps. Augmenting neural networks with low-fidelity timestepping algorithms may allow us to take large timesteps while limiting the numerical dispersion artifacts. While simulating the wave-equation with low-fidelity timestepping algorithm, by correcting the wavefield several time during propagation, we hope to limit the numerical dispersion artifact introduced by a poor discretization of the Laplacian. As a proof of concept, we demonstrate this principle by correcting for numerical dispersion by keeping the velocity model fixed, and varying the source locations to generate training and testing pairs for our supervised learning algorithm.
