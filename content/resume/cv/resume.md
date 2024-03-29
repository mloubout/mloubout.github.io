---
title: Mathias Thibaut Louboutin
author: 
  \

  Atlanta, GA \

  mathias.louboutin@gmail.com \

  404-451-6131 \

  [mloubout.github.io](mloubout.github.io) \

  [Github](https://github.com/mloubout) \

  [\@louboutjunior](https://twitter.com/Louboutjunior)

company: DevitoCodes Ltd
---

Experience
----------

July 2020– July 2023
:   **Postdoctoral Fellow**: Georgia Institute of Technology, Atlanta, GA

    *High performance/low memory randomized linear algebra for backpropagation based inverse problems*

    *Cloud HPC for separable problems (task parallel)*

    *Supervising the PhD and MSc students*

    *Managing and developping the software stack for the Lab ([slimgroup])*

    *Machine learning for geophysical and medical wave-equation based inverse problems*

    *HPC for machine learning*

    *Geological Carbon Storage seismic monitoring*


Computational experience
----------

Open Source
:   **[Devito]**: A symbolic domain specific language (DSL) for stencil computation with just-in-time compilation and code generation. Achieves state of the art performance while providing a high-level mathematical interface to the users for the development of stencil based applications.
:   **[JUDI]**: Linear algebra high level API for wave-equation based inversion. This pacage is built on top of Devito to have high performance wave-equation solvers. A new additional Azure batch extension was developped for scalability [JUDI4Cloud].
:   **[XConv]**: High performance low memory convolutional layer. This repository implements both in julia (for Flux.jl) and in python (for pytorch) a convolutional layer that has virtually a zero memory imprnt for training using randomized linear algebra to compute an unbiased estimate of the gradient with respect to the weights. Additionaly, a byte only implementation of the ReLU layer leads to memry reduction by a factor of X2 for full networks.
:   **[dfno]**: Model parallel (MPI model decomposition) implementation of Fourier Neural Operators for PyTorch. Extension of distdl, a model parallel extension of PyTorch.
:   **[InvertibleNetworks.jl]**: Native Julia implementation of invertible networks for variational inference, generative models and normalizing flows.


Programming Languages
:   **Python:** Main programming language for the development of [Devito] and machine learning applications.
:   **Julia:** Heavy development of research software at  Georgia Tech ([slimgroup]) in Julia
:   **docker** Developped and automatized the deployement of [Devito] and [JUDI] images through CI (github actions).
:   Knowledge of **C**, **Linux**, **Bash**, **PyTorch**, **Azure**, **Latex**, **Markdown**, **Matlab**, **MPI**, **OPenMP**, **OpenACC**

HPC
:   **[Devito]:** Weak and strong scaling benchmarks of [Devito] on on-premise (Imperical college) and Cloud (Azure) hardware.
:   **[JUDI]:** Implementation and deployment at scale of [JUDI] on clusters and Azure Batch (up 300 nodes).
:   **Optimum (2015-2018):** Early PhD 50 nodes cluster. Development of parallel Matlab seismic inverse problem algorithms (FWI/RTM). 
:   **YEMOJA (2017-2018):** Part of a collaboration with SENAI-CIMANTEC. Scaling of our Matlab and Julia framework to hundred of nodes.
:   **Cloud (2018-):** Serverless and clusterless framework for task parallel inverse problems on AWS and Azure.
:   **Perlmutter (2022-):** Scaling of MPI-parallel Fourier Neural Operator on Perlmutter (and previously Summit).

Education
---------

2018–2020
:   **PhD, Computer Science**; Georgia Institute of Technology, Atlanta, GA

    *Thesis title: Modeling for inversion in exploration geophysics*  [Link](https://slim.gatech.edu/content/modeling-inversion-exploration-geophysics)

    *Numerical and computational methods for large scale simulation based inverse problems and machine learning*

2013–2018
:   **PhD, Earth Science**; University of British Columbia, Canada

    *Transfered to Georgia Institute of Technology in January 2018 following my supervior new position there.*

2016 Feb-Aug
:   **Visiting PhD, Computer Science**; Impertial College London, UK

    *Automatic code generation for geophysical exploration applications with finite differences*

2011–2013
:   **MSc, Applied Mathematics**; Universite de Rennes 1, Rennes, France

    *Valedictorian*

    *Required coursework*: Calculus, Numerical Methods, PDE Resolution, Opti- mization, C/C++ Computing, Mathematics Modeling and Simulation, Finite Element Method*

    *Elective coursework*: Fluid Mechanics, Continuum Mechanics and Thermo- mechanics, Bio-mechanics, Geophysics Modeling*

2008–2011
:   **BSc, Aeronautical Engineering,** ENSICA-ISAE, Toulouse, France

    *Leading French Aeronautical Engineering School.*

    *Required coursework*: Mathematics, Mechanics, Continuum Mechanics, Struc- tures Mechanics, Signal Processing, Thermodynamics, Fluid Mechanics, Java progamming*

    *Elective coursework*: Estimation Methods, Earth Observation Satellites, Microwaves Processing*

2006–2008
:   **Classe Preparatoires**; Lycee Chateaubriand, Rennes, France

    *Advanced undergraduate preparatory program for national ranking entry exam.*


Internships
----------

Summer 2013
:   **Research internship**; ONERA, Toulouse, France

    *Scattering patterns of atmospheric dust clouds analysis with the Discrete Dipole Approximation (DDA) method.*

Summer 2012
:   **Research internship**; INRIA, Grenoble, France

    *Intern in NANO-D department at INRIA-Grenoble. L2-SVM for protein interactions. Runtime and accuracy improvement of the C implementation and algorithmic development.*

Summer 2011
:   **Internship, Aeroconseil**, Toulouse, France

    *Developed an interface for aerodynamics calculus in JAVA. Reading and implementation of Excel and Scilab scripts through the interface.*


Additonal skills
----------------------------------------

* Languages:

     * French (native speaker)
     * English (Advanced, PhD in USA)

* Miscelanous CS:

     * Linux, Shell script, Latex, Markdown, Github, Unix, Matlab

[Devito]:https://github.com/devitocodes/devito
[slimgroup]:https://github.com/slimgroup
[JUDI]:https://github.com/slimgroup/JUDI.jl
[JUDI4Cloud]:https://github.com/slimgroup/JUDI.jl
[XConv]:https://github.com/slimgroup/XConv
[InvertibleNetworks.jl]:https://github.com/slimgroup/InvertibleNetworks.jl
[dfno]:https://github.com/slimgroup/dfno
