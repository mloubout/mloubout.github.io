---
title: "The importance of transfer learning in seismic modeling and imaging"
etype: 'article'
collection: publications
permalink: /publication/2019-01-01-The-importance-of-transfer-learning-in-seismic-modeling-and-imaging
excerpt: '(Accepted in GEOPHYSICS)'
date: 2019-01-01
venue: 'The importance of transfer learning in seismic modeling and imaging'
paperurl: 'https://slim.gatech.edu/Publications/Public/Journals/Geophysics/2019/siahkoohi2019itl/siahkoohi2019itl.html'
citation: ' Ali Siahkoohi,  Mathias Louboutin,  Felix Herrmann, &quot;The importance of transfer learning in seismic modeling and imaging.&quot; The importance of transfer learning in seismic modeling and imaging, 2019.'
---
(Accepted in GEOPHYSICS)

[Access paper here](https://slim.gatech.edu/Publications/Public/Journals/Geophysics/2019/siahkoohi2019itl/siahkoohi2019itl.html){:target="_blank"}

Accurate forward modeling is essential for solving inverse problems in exploration seismology. Unfortunately, it is often not possible to afford being physically or numerically accurate. To overcome this conundrum, we make use of raw and processed data from nearby surveys. We propose to use this data, consisting of shot records or velocity models, to pre-train a neural network to correct for the effects of, for instance, the free surface or numerical dispersion, both of which can be considered as proxies for incomplete or inaccurate physics. Given this pre-trained neural network, we apply transfer learning to finetune this pre-trained neural network so it performs well on its task of mapping low-cost, but low-fidelity, solutions to high-fidelity solutions for the current survey. As long as we can limit ourselves during finetuning to using only a small fraction of high-fidelity data, we gain processing the current survey while using information from nearby surveys. We demonstrate this principle by removing surface-related multiples and ghosts from shot records and the effects of numerical dispersion from migrated images and wave simulations
