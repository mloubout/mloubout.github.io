---
layout: archive
title: "Softwares"
permalink: /softwares/
author_profile: true
---

I am a beleiver in open source softwares. During the course of my PhD I have been faced with numerous interaction with industrial partners that relied heavily on proprietary softwares while expecting impossible thorough and comparative results. I have pushed for open source softwares for years and hpe my track record can make a contribution, even small, towards better computing softwares. You will find below my most relevant work and you can find all my repositories on my [github](https://github.com/mloubout).

# Major contributor

[Devito](https://github.com/devitocodes/devito): 
Finite-difference DSL and just-in-time compiler for high performance stencil computation. This software's interface and high-level API is based on sy,py for symbolic manpulation. The compiler generates high performance C-code and supports standard openMP, MPI, GPU offloading via openacc or openmp and MPI+GPU.

[JUDI](https://github.com/slimgroup/JUDI.jl):
Linear algebra high level API for wave-equation based inversion. This pacage is built on top of Devito to have high performance wave-equation solvers.

[XConv](https://github.com/slimgroup/XConv.jl):
High performance low memory convolutional layer. This repository implements both in julia (for Flux.jl) and in python (for pytorch) a convolutional layer that has virtually a zero memory imprnt for training using randomized linear algebra to compute an unbiased estimate of the gradient with respect to the weights. Additionaly, a byte only implementation of the ReLU layer leads to memry reduction by a factor of X2 ffor full networks.

[TimeProbeSeismic](https://github.com/slimgroup/TimeProbeSeismic.jl):
Seismic inversion via time probing. This method reduces the memory requiremnt of adjoint state by a factor of `X10-X1000` depending on the physical setup while providing similar accuracy than standard adjoint state.

# Contributor

[ExtendedConv](https://github.com/slimgroup/ExtendedConv.jl):
Extended convolution that use spatially constrained varying convolution weight to convexify machine learning loss.

[InvertibleNetworks](https://github.com/slimgroup/InvertibleNetworks.jl):
Julia implementation of invertible networks. Invertible networks are fully reversible and do not need to store intermediate state variable for training making them virtually memory free.


# Minor contributions


[Sympy](https://github.com/sympy/sympy):
Minor pull request contributions mostly related to bugs found through [Devito](https://github.com/devitocodes/devito).