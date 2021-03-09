---
title: "Preconditioned training of normalizing flows for variational inference in inverse problems"
collection: publications
permalink: /publication/2021-01-01-Preconditioned-training-of-normalizing-flows-for-variational-inference-in-inverse-problems
date: 2021-01-01
venue: 'Preconditioned training of normalizing flows for variational inference in inverse problems'
paperurl: 'https://slim.gatech.edu/Publications/Public/Conferences/AABI/2021/siahkoohi2021AABIpto/siahkoohi2020ABIfab.html'
citation: ' Ali Siahkoohi,  Gabrio Rizzuti,  Mathias Louboutin,  Philipp Witte,  Felix Herrmann, &quot;Preconditioned training of normalizing flows for variational inference in inverse problems.&quot; Preconditioned training of normalizing flows for variational inference in inverse problems, 2021.'
---
[Access paper here](https://slim.gatech.edu/Publications/Public/Conferences/AABI/2021/siahkoohi2021AABIpto/siahkoohi2020ABIfab.html){:target="_blank"}

Obtaining samples from the posterior distribution of inverse problems with expensive forward operators is challenging especially when the unknowns involve the strongly heterogeneous Earth. To meet these challenges, we propose a preconditioning scheme involving a conditional normalizing flow (NF) capable of sampling from a low-fidelity posterior distribution directly. This conditional NF is used to speed up the training of the high-fidelity objective involving minimization of the Kullback-Leibler divergence between the predicted and the desired high-fidelity posterior density for indirect measurements at hand. To minimize costs associated with the forward operator, we initialize the high-fidelity NF with the weights of the pretrained low-fidelity NF, which is trained beforehand on available model and data pairs. Our numerical experiments, including a 2D toy and a seismic compressed sensing example, demonstrate that thanks to the preconditioning considerable speed-ups are achievable compared to training NFs from scratch.
